import morph from "https://esm.sh/micromorph";

function getNodeKey(el) {
    return el.dataset && el.dataset.key ? el.dataset.key : null;
}

function scrollToHash(hash) {
    if (!hash) return;
    const id = decodeURIComponent(hash.replace(/^#/, ''));
    const el = document.getElementById(id) || document.querySelector(`[name="${id}"]`);
    if (el) el.scrollIntoView({ behavior: 'auto', block: 'start' });
}

async function navigate(url, push = true, hash = "") {
    const res = await fetch(url, { headers: { "X-Requested-With": "micromorph" } });
    const html = await res.text();
    const doc = new DOMParser().parseFromString(html, "text/html");

    morph(document, doc, { getNodeKey });

    if (push) {
        // Preserve hash if present
        const u = new URL(url, location.href);
        history.pushState(null, "", u.pathname + u.search + (hash || u.hash));
    }

    // If there’s a hash, scroll to it after morph
    const finalHash = hash || new URL(url, location.href).hash;
    if (finalHash) {
        // Wait a tick so layout has settled
        requestAnimationFrame(() => scrollToHash(finalHash));
    } else {
        // Default scroll behavior for normal page nav
        window.scrollTo({ top: 0, left: 0 });
    }
}

// If you have a fixed header, add CSS so anchors aren’t hidden:
// :where(h1,h2,h3,h4,h5,h6,[id]) { scroll-margin-top: 80px; }  /* adjust to header height */

document.addEventListener("click", (e) => {
    const a = e.target.closest('a[href]');
    if (!a) return;

    const external = a.origin !== location.origin;
    if (a.target || a.hasAttribute("download") || external || e.defaultPrevented) return;

    const href = a.getAttribute('href') || "";
    const url = new URL(href, location.href);

    // 1) Same-page hash link: don’t fetch, just scroll
    if (url.origin === location.origin && url.pathname === location.pathname && url.hash) {
        e.preventDefault();
        // Update the hash in the URL bar without reloading
        history.pushState(null, "", url.hash);
        scrollToHash(url.hash);
        return;
    }

    // 2) Normal nav (possibly with a hash to another page)
    e.preventDefault();
    navigate(url.href, true, url.hash);
});

window.addEventListener("popstate", () => {
    // Handle back/forward, including hash-only history entries
    const { pathname, search, hash } = location;
    // If only the hash changed on the same page, just scroll
    if (pathname === window.__lastPathname) {
        scrollToHash(hash, false);
    } else {
        navigate(location.href, false, hash);
    }
    window.__lastPathname = pathname;
});

// Remember last pathname to detect hash-only history steps
window.__lastPathname = location.pathname;
