# external_favicons.py
# Append site favicons to external links and cache icons locally.
# Requires no extra deps (uses stdlib). If BeautifulSoup is installed, it’ll use it; otherwise falls back to regex.

from __future__ import annotations

import os
import re
import ssl
import urllib.parse
import urllib.request

from pelican import signals


UA = "Pelican-FaviconFetcher/1.0"
DEFAULT_ICON_DIR = "favicons"  # URL/path segment under OUTPUT_PATH


def _domain_key(netloc: str) -> str:
    """Collapse a netloc to a stable key: strip port, auth, and 'www.'; reduce subdomains."""
    host = netloc.split("@")[-1].split(":")[0].strip().lower()
    if host.startswith("www."):
        host = host[4:]
    parts = host.split(".")
    # Naive eTLD+1 fallback (tldextract would be better but we avoid extra deps)
    if len(parts) >= 3:
        host = ".".join(parts[-2:])
    return host


def _infer_ext(content_type: str | None, url: str) -> str:
    if content_type:
        ct = content_type.lower()
        if "svg" in ct:
            return ".svg"
        if "png" in ct:
            return ".png"
        if "jpeg" in ct or "jpg" in ct:
            return ".jpg"
        if "x-icon" in ct or "vnd.microsoft.icon" in ct or "ico" in ct:
            return ".ico"
    path_ext = os.path.splitext(urllib.parse.urlparse(url).path)[1]
    return path_ext or ".ico"


def _download_icon_for(host: str, cache_dir: str, timeout: int, use_google_fallback: bool) -> str | None:
    """Try fetching /favicon.ico, /favicon.png, or /favicon.jpg. Optionally fall back to Google S2 service."""
    ctx = ssl.create_default_context()
    for candidate_host in (host, f"www.{host}" if not host.startswith("www.") else host):
        for path in ("/favicon.ico", "/favicon.png", "/favicon.jpg"):
            url = f"https://{candidate_host}{path}"
            try:
                req = urllib.request.Request(url, headers={"User-Agent": UA})
                with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
                    if resp.status == 200:
                        ext = _infer_ext(resp.getheader("Content-Type"), url)
                        fname = f"{host}{ext}"
                        fpath = os.path.join(cache_dir, fname)
                        os.makedirs(cache_dir, exist_ok=True)
                        with open(fpath, "wb") as f:
                            f.write(resp.read())
                        return fname
            except Exception:
                pass

    if use_google_fallback:
        # Google S2 favicon service (returns PNG). If you’d rather avoid third-party,
        # set FAVICON_USE_GOOGLE_FALLBACK = False in settings.
        url = f"https://www.google.com/s2/favicons?domain={host}&sz=64"
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
                if resp.status == 200:
                    fname = f"{host}.png"
                    fpath = os.path.join(cache_dir, fname)
                    os.makedirs(cache_dir, exist_ok=True)
                    with open(fpath, "wb") as f:
                        f.write(resp.read())
                    return fname
        except Exception:
            pass

    return None


def _existing_icon_filename(host: str, cache_dir: str) -> str | None:
    for ext in (".ico", ".png", ".svg", ".jpg", ".jpeg"):
        candidate = os.path.join(cache_dir, f"{host}{ext}")
        if os.path.exists(candidate):
            return os.path.basename(candidate)
    return None


def _image_url(settings: dict, icon_dir_url_segment: str, filename: str) -> str:
    prefix = f"/{icon_dir_url_segment}"
    return f"{prefix}/{filename}"


def _cache_dir(settings: dict, icon_dir_url_segment: str) -> str:
    # If user provided FAVICON_CACHE_DIR (absolute or relative), honor it.
    custom = settings.get("FAVICON_CACHE_DIR")
    outdir = settings.get("OUTPUT_PATH", "output")
    if custom:
        return custom if os.path.isabs(custom) else os.path.join(outdir, custom)
    # Default: write to OUTPUT_PATH/<icon_dir_url_segment> so the files end up in the generated site.
    return os.path.join(outdir, icon_dir_url_segment)


def _is_external(href: str, our_domain: str | None) -> bool:
    try:
        u = urllib.parse.urlparse(href)
    except Exception:
        return False
    if u.scheme not in ("http", "https"):
        return False
    if not u.netloc:
        return False
    if our_domain and _domain_key(u.netloc) == _domain_key(our_domain):
        return False
    return True


def _append_icon_via_bs4(html: str, settings: dict, our_domain: str | None) -> str:
    from bs4 import BeautifulSoup  # optional dependency

    icon_dir_url_segment = settings.get("FAVICON_DIR", DEFAULT_ICON_DIR).strip("/")

    cache_dir = _cache_dir(settings, icon_dir_url_segment)
    download_enabled = settings.get("FAVICON_DOWNLOAD", True)
    timeout = int(settings.get("FAVICON_TIMEOUT", 5))
    use_google_fallback = bool(settings.get("FAVICON_USE_GOOGLE_FALLBACK", True))
    size = int(settings.get("FAVICON_IMG_SIZE", 16))
    css_class = settings.get("FAVICON_IMG_CLASS", "ext-favicon")

    soup = BeautifulSoup(html, "html.parser")
    for a in soup.find_all("a", href=True):
        if a.get("data-no-favicon") is not None:
            continue
        if a.find("img"):
            # Link already contains an image; skip to avoid double icons.
            continue

        href = a["href"]
        if not _is_external(href, our_domain):
            continue

        host = _domain_key(urllib.parse.urlparse(href).netloc)
        filename = _existing_icon_filename(host, cache_dir)
        if not filename and download_enabled:
            filename = _download_icon_for(host, cache_dir, timeout, use_google_fallback)

        if not filename:
            continue

        img = soup.new_tag(
            "img",
            src=_image_url(settings, icon_dir_url_segment, filename),
            alt=f"{host} favicon",
            loading="lazy",
        )
        img["class"] = css_class
        img["width"] = img["height"] = str(size)

        # Insert a NBSP so the icon never wraps to the next line, then the icon
        a.append("\u00A0")
        a.append(img)

    return str(soup)


# Simple regex fallback if BeautifulSoup isn't available.
_A_TAG_RE = re.compile(r'(<a\b[^>]*href="([^"]+)"[^>]*>)(.*?)(</a>)', re.I | re.S)


def _append_icon_via_regex(html: str, settings: dict, our_domain: str | None) -> str:
    icon_dir_url_segment = settings.get("FAVICON_DIR", DEFAULT_ICON_DIR).strip("/")
    cache_dir = _cache_dir(settings, icon_dir_url_segment)
    download_enabled = settings.get("FAVICON_DOWNLOAD", True)
    timeout = int(settings.get("FAVICON_TIMEOUT", 5))
    use_google_fallback = bool(settings.get("FAVICON_USE_GOOGLE_FALLBACK", True))
    size = int(settings.get("FAVICON_IMG_SIZE", 16))
    css_class = settings.get("FAVICON_IMG_CLASS", "ext-favicon")

    def repl(m: re.Match) -> str:
        start, href, inner, end = m.groups()

        # crude skip: if inner already contains an <img>, leave as-is
        if re.search(r"<img\b", inner, re.I):
            return m.group(0)

        if not _is_external(href, our_domain):
            return m.group(0)

        host = _domain_key(urllib.parse.urlparse(href).netloc)
        filename = _existing_icon_filename(host, cache_dir)
        if not filename and download_enabled:
            filename = _download_icon_for(host, cache_dir, timeout, use_google_fallback)
        if not filename:
            return m.group(0)

        src = _image_url(settings, icon_dir_url_segment, filename)
        img_tag = f' <img class="{css_class}" src="{src}" alt="{host} favicon" width="{size}" height="{size}" loading="lazy" />'
        return f"{start}{inner}{img_tag}{end}"

    return _A_TAG_RE.sub(repl, html)


def _process_content(content):
    if not getattr(content, "_content", None):
        return

    settings = getattr(content, "settings", {}) or {}
    siteurl = (settings.get("SITEURL") or "").strip()
    our_domain = urllib.parse.urlparse(siteurl).netloc if siteurl else None

    # Only touch HTML content
    html = content._content
    if "<a " not in html.lower():
        return

    try:
        # Prefer BeautifulSoup if available
        import bs4  # noqa: F401
        content._content = _append_icon_via_bs4(html, settings, our_domain)
    except Exception:
        # Fall back to regex
        content._content = _append_icon_via_regex(html, settings, our_domain)


def register():
    signals.content_object_init.connect(_process_content)
