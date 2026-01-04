(function () {
    const btn = document.getElementById('back-to-top');
    if (!btn) return;

    const showAfter = 400; // px scrolled before showing

    function onScroll() {
        const y = window.scrollY || document.documentElement.scrollTop;
        if (y > showAfter) {
            btn.hidden = false;
            btn.classList.add('is-visible');
        } else {
            btn.classList.remove('is-visible');
            // allow the fade-out to complete before hiding for a11y focus
            setTimeout(() => {
                if (!btn.classList.contains('is-visible')) btn.hidden = true;
            }, 200);
        }
    }

    function scrollToTop() {
        const behavior = 'auto';
        window.scrollTo({ top: 0, behavior });
    }

    window.addEventListener('scroll', onScroll, { passive: true });
    btn.addEventListener('click', scrollToTop);

    // Initial state on load
    onScroll();
})();