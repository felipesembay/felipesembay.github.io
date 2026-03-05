document.addEventListener('DOMContentLoaded', () => {
    // Track sections in index.html and index-pt.html
    const sections = document.querySelectorAll('section');
    let sectionTimers = {};

    // Create an Intersection Observer
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            // Get section id or class name
            const sectionId = entry.target.id || entry.target.className.split(' ')[0] || 'unknown-section';

            if (entry.isIntersecting) {
                // Start timer when section becomes visible
                sectionTimers[sectionId] = Date.now();
            } else {
                // End timer when section leaves the viewport
                if (sectionTimers[sectionId]) {
                    const timeSpentSeconds = Math.round((Date.now() - sectionTimers[sectionId]) / 1000);

                    // Only log if the user spent more than 2 seconds viewing the section
                    if (timeSpentSeconds > 2) {
                        gtag('event', 'screen_view_duration', {
                            'screen_name': sectionId,
                            'engagement_time_sec': timeSpentSeconds,
                            'page_path': window.location.pathname
                        });
                    }
                    // Reset timer
                    delete sectionTimers[sectionId];
                }
            }
        });
    }, {
        threshold: 0.5 // Trigger when at least 50% of the section is visible
    });

    // Track all page sections
    sections.forEach(section => {
        observer.observe(section);
    });

    // Use visibilitychange instead of beforeunload to reliably track when the user leaves the page or switches tabs
    document.addEventListener('visibilitychange', () => {
        if (document.visibilityState === 'hidden') {
            Object.keys(sectionTimers).forEach(sectionId => {
                const timeSpentSeconds = Math.round((Date.now() - sectionTimers[sectionId]) / 1000);
                if (timeSpentSeconds > 2) {
                    gtag('event', 'screen_view_duration', {
                        'screen_name': sectionId,
                        'engagement_time_sec': timeSpentSeconds,
                        'page_path': window.location.pathname
                    });
                }
                // Reset timer for if they come back to the tab
                sectionTimers[sectionId] = Date.now();
            });
        } else if (document.visibilityState === 'visible') {
            // Restart timers
            Object.keys(sectionTimers).forEach(sectionId => {
                sectionTimers[sectionId] = Date.now();
            });
        }
    });
});
