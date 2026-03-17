/**
 * GA4 Virtual Pageview Tracker — Felipe Sembay Portfolio
 * Fires a GA4 page_view event whenever a section becomes visible,
 * giving GA4 granular per-section analytics without changing the URL.
 */
(function () {
    'use strict';

    // ── Section map: DOM id → { virtual path EN, virtual path PT } ──────────
    const SECTION_MAP = {
        'hero': { en: '/home', pt: '/pt/inicio' },
        'about': { en: '/about', pt: '/pt/sobre' },
        'resume': { en: '/resume', pt: '/pt/curriculo' },
        'portfolio': { en: '/portfolio', pt: '/pt/portfolio' },
        'services': { en: '/services', pt: '/pt/servicos' },
        'contact': { en: '/contact', pt: '/pt/contato' },
    };

    // ── Detect current language from <html lang> ─────────────────────────────
    const lang = (document.documentElement.lang || 'en').startsWith('pt') ? 'pt' : 'en';

    // ── Time-on-section tracking ─────────────────────────────────────────────
    const sectionEntryTimes = {};  // { sectionId: timestamp }
    const reported = new Set();    // sections whose page_view was already sent

    // ── Fire a GA4 virtual page_view ─────────────────────────────────────────
    function firePageView(sectionId) {
        if (reported.has(sectionId)) return;
        reported.add(sectionId);

        const virtualPath = SECTION_MAP[sectionId][lang];
        const sectionTitle = document.getElementById(sectionId)
            ?.querySelector('h2, h1')?.textContent?.trim() || sectionId;

        if (typeof gtag !== 'function') return;

        gtag('event', 'page_view', {
            page_title: sectionTitle + ' | Felipe Sembay',
            page_location: window.location.origin + virtualPath,
            page_path: virtualPath,
        });

        console.debug('[Analytics] Virtual pageview →', virtualPath);
    }

    // ── Fire a GA4 time_on_section event when leaving ────────────────────────
    function fireTimeOnSection(sectionId, seconds) {
        if (typeof gtag !== 'function' || seconds < 1) return;

        gtag('event', 'time_on_section', {
            section_id: sectionId,
            section_path: SECTION_MAP[sectionId][lang],
            seconds_spent: Math.round(seconds),
        });

        console.debug('[Analytics] Time on section →', sectionId, Math.round(seconds) + 's');
    }

    // ── IntersectionObserver — fires when ≥40% of section is visible ─────────
    const observer = new IntersectionObserver(
        (entries) => {
            entries.forEach((entry) => {
                const id = entry.target.id;
                if (!SECTION_MAP[id]) return;

                if (entry.isIntersecting) {
                    // Section entered → record time and fire page_view
                    sectionEntryTimes[id] = performance.now();
                    firePageView(id);
                } else {
                    // Section left → calculate time spent
                    if (sectionEntryTimes[id]) {
                        const seconds = (performance.now() - sectionEntryTimes[id]) / 1000;
                        fireTimeOnSection(id, seconds);
                        delete sectionEntryTimes[id];
                    }
                }
            });
        },
        {
            threshold: 0.4,   // section must be 40% visible to count
            rootMargin: '0px',
        }
    );

    // ── Observe all mapped sections ──────────────────────────────────────────
    function init() {
        Object.keys(SECTION_MAP).forEach((id) => {
            const el = document.getElementById(id);
            if (el) {
                observer.observe(el);
            }
        });
    }

    // ── Fire remaining time-on-section before page unloads ───────────────────
    window.addEventListener('visibilitychange', () => {
        if (document.visibilityState === 'hidden') {
            Object.entries(sectionEntryTimes).forEach(([id, startTime]) => {
                const seconds = (performance.now() - startTime) / 1000;
                fireTimeOnSection(id, seconds);
            });
        }
    });

    // ── Initialise after DOM is ready ────────────────────────────────────────
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
