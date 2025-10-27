// Modern Portfolio JavaScript

document.addEventListener('DOMContentLoaded', function() {
    
    // Smooth scrolling for navigation links
    const navLinks = document.querySelectorAll('a[href^="#"]');
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            
            if (targetElement) {
                const offsetTop = targetElement.offsetTop - 80; // Account for fixed navbar
                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });
            }
        });
    });

    // Navbar background change on scroll
    const navbar = document.querySelector('.navbar');
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            navbar.style.background = 'rgba(10, 10, 10, 0.95)';
            navbar.style.boxShadow = '0 4px 20px rgba(0, 0, 0, 0.4)';
        } else {
            navbar.style.background = 'rgba(10, 10, 10, 0.85)';
            navbar.style.boxShadow = '0 4px 16px rgba(0, 0, 0, 0.3)';
        }
    });

    // Animate elements on scroll
    const observerOptions = {
        threshold: 0.12,
        rootMargin: '0px 0px -40px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // ensure the base animation class exists
                if (!entry.target.classList.contains('fade-in-up')) {
                    entry.target.classList.add('fade-in-up');
                }
                // reveal
                entry.target.classList.add('in-view');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Observe elements for animation: include explicit data-anim markers and common cards
    const animateElements = document.querySelectorAll('[data-anim], .skill-card, .project-card, .timeline-item, .contact-item');
    animateElements.forEach(el => observer.observe(el));

    // Skill progress bars animation
    const progressBars = document.querySelectorAll('.progress-bar');
    const skillObserver = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const progressBar = entry.target;
                const width = progressBar.style.width;
                progressBar.style.width = '0%';
                setTimeout(() => {
                    progressBar.style.width = width;
                }, 200);
                skillObserver.unobserve(progressBar);
            }
        });
    }, { threshold: 0.5 });

    progressBars.forEach(bar => {
        skillObserver.observe(bar);
    });

    // Form validation and enhancement
    const contactForm = document.querySelector('form');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            const submitBtn = this.querySelector('button[type="submit"]');
            const originalText = submitBtn.innerHTML;
            
            // Show loading state
            submitBtn.innerHTML = '<span class="loading"></span> Envoi en cours...';
            submitBtn.disabled = true;
            
            // Re-enable after 3 seconds (in case of slow response)
            setTimeout(() => {
                submitBtn.innerHTML = originalText;
                submitBtn.disabled = false;
            }, 3000);
        });
    }

    // Hero content is now always visible (no animation to prevent flicker)
    const heroTitle = document.querySelector('.hero-content h1');
    if (heroTitle) {
        heroTitle.style.opacity = '1';
        heroTitle.style.transform = 'translateY(0)';
    }

    // Subtle parallax effect for hero section
    const heroSection = document.querySelector('.hero-section');
    if (heroSection) {
        window.addEventListener('scroll', throttle(function() {
            const scrolled = window.pageYOffset;
            const rate = scrolled * -0.3;
            heroSection.style.transform = `translateY(${rate}px)`;
        }, 16));
    }

    // Project card hover effects
    const projectCardsHover = document.querySelectorAll('.project-card');
    projectCardsHover.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-10px) scale(1.02)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
    });

    // Skill card interactions
    const skillCards = document.querySelectorAll('.skill-card');
    skillCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            const icon = this.querySelector('i');
            if (icon) {
                icon.style.transform = 'scale(1.2) rotate(5deg)';
            }
        });
        
        card.addEventListener('mouseleave', function() {
            const icon = this.querySelector('i');
            if (icon) {
                icon.style.transform = 'scale(1) rotate(0deg)';
            }
        });
    });

    // Mobile menu enhancement
    const navbarToggler = document.querySelector('.navbar-toggler');
    const navbarCollapse = document.querySelector('.navbar-collapse');
    
    if (navbarToggler && navbarCollapse) {
        navbarToggler.addEventListener('click', function() {
            navbarCollapse.classList.toggle('show');
        });
        
        // Close mobile menu when clicking on a link
        const mobileNavLinks = navbarCollapse.querySelectorAll('.nav-link');
        mobileNavLinks.forEach(link => {
            link.addEventListener('click', function() {
                navbarCollapse.classList.remove('show');
            });
        });
    }

    // Back to top button
    const backToTopBtn = document.createElement('button');
    backToTopBtn.innerHTML = '<i class="fas fa-chevron-up"></i>';
    backToTopBtn.className = 'btn btn-primary position-fixed';
    backToTopBtn.style.cssText = `
        bottom: 30px;
        right: 30px;
        z-index: 1000;
        border-radius: 50%;
        width: 56px;
        height: 56px;
        display: none;
        box-shadow: 0 8px 24px rgba(16, 185, 129, 0.3);
        transition: all 0.3s ease;
    `;
    document.body.appendChild(backToTopBtn);

    window.addEventListener('scroll', function() {
        if (window.scrollY > 300) {
            backToTopBtn.style.display = 'block';
        } else {
            backToTopBtn.style.display = 'none';
        }
    });

    backToTopBtn.addEventListener('click', function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });

    // Loading animation for images (excluding project cards to prevent flicker)
    const images = document.querySelectorAll('img:not(.card-img-top)');
    images.forEach(img => {
        img.style.transition = 'opacity 0.3s ease';

        function show() {
            img.style.opacity = '1';
        }

        if (img.complete && img.naturalWidth !== 0) {
            // already loaded (from cache)
            show();
        } else {
            // not yet loaded
            img.style.opacity = '0';
            img.addEventListener('load', show, { once: true });
            // also handle error case to avoid permanently invisible images
            img.addEventListener('error', function() {
                img.style.opacity = '1';
                img.classList.add('img-error');
            }, { once: true });
        }
    });
    
    // Ensure project card images are always visible
    const projectImages = document.querySelectorAll('.card-img-top');
    projectImages.forEach(img => {
        img.style.opacity = '1';
    });

    // Contact form enhancement
    const formInputs = document.querySelectorAll('input, textarea');
    formInputs.forEach(input => {
        input.addEventListener('focus', function() {
            this.parentElement.classList.add('focused');
        });
        
        input.addEventListener('blur', function() {
            if (!this.value) {
                this.parentElement.classList.remove('focused');
            }
        });
    });

    // Add ripple effect to buttons
    const buttons = document.querySelectorAll('.btn');
    buttons.forEach(button => {
        button.addEventListener('click', function(e) {
            const ripple = document.createElement('span');
            const rect = this.getBoundingClientRect();
            const size = Math.max(rect.width, rect.height);
            const x = e.clientX - rect.left - size / 2;
            const y = e.clientY - rect.top - size / 2;
            
            ripple.style.cssText = `
                position: absolute;
                width: ${size}px;
                height: ${size}px;
                left: ${x}px;
                top: ${y}px;
                background: rgba(255, 255, 255, 0.3);
                border-radius: 50%;
                transform: scale(0);
                animation: ripple 0.6s linear;
                pointer-events: none;
            `;
            
            this.style.position = 'relative';
            this.style.overflow = 'hidden';
            this.appendChild(ripple);
            
            setTimeout(() => {
                ripple.remove();
            }, 600);
        });
    });

    // Add CSS for ripple animation
    const style = document.createElement('style');
    style.textContent = `
        @keyframes ripple {
            to {
                transform: scale(4);
                opacity: 0;
            }
        }
    `;
    document.head.appendChild(style);

    // Animated Counter for Stats
    const statNumbers = document.querySelectorAll('.stat-number');
    const statsObserver = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const target = parseInt(entry.target.getAttribute('data-target'));
                animateCounter(entry.target, target);
                statsObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });

    statNumbers.forEach(stat => {
        statsObserver.observe(stat);
    });

    function animateCounter(element, target) {
        let current = 0;
        const increment = target / 50; // 50 steps
        const duration = 2000; // 2 seconds
        const stepTime = duration / 50;

        const timer = setInterval(() => {
            current += increment;
            if (current >= target) {
                element.textContent = target;
                clearInterval(timer);
            } else {
                element.textContent = Math.floor(current);
            }
        }, stepTime);
    }

    // Project Filters
    const filterBtns = document.querySelectorAll('.filter-btn');
    const projectCards = document.querySelectorAll('.project-card');

    filterBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            // Remove active class from all buttons
            filterBtns.forEach(b => b.classList.remove('active'));
            // Add active class to clicked button
            this.classList.add('active');

            const filter = this.getAttribute('data-filter');

            projectCards.forEach(card => {
                const cardParent = card.closest('.col-lg-4');
                if (filter === 'all') {
                    cardParent.style.display = 'block';
                    setTimeout(() => {
                        card.style.opacity = '1';
                        card.style.transform = 'scale(1)';
                    }, 10);
                } else {
                    // Get technologies from the card
                    const technologies = card.querySelector('.technologies');
                    if (technologies) {
                        const techText = technologies.textContent.toLowerCase();
                        let shouldShow = false;

                        // Simple filter logic based on keywords
                        if (filter === 'web' && (techText.includes('html') || techText.includes('css') || techText.includes('javascript') || techText.includes('react') || techText.includes('vue'))) {
                            shouldShow = true;
                        } else if (filter === 'mobile' && (techText.includes('android') || techText.includes('ios') || techText.includes('flutter') || techText.includes('react native'))) {
                            shouldShow = true;
                        } else if (filter === 'fullstack' && (techText.includes('django') || techText.includes('node') || techText.includes('express') || techText.includes('spring'))) {
                            shouldShow = true;
                        } else if (filter === 'other') {
                            shouldShow = !techText.includes('html') && !techText.includes('react') && !techText.includes('django') && !techText.includes('android');
                        }

                        if (shouldShow) {
                            cardParent.style.display = 'block';
                            setTimeout(() => {
                                card.style.opacity = '1';
                                card.style.transform = 'scale(1)';
                            }, 10);
                        } else {
                            card.style.opacity = '0';
                            card.style.transform = 'scale(0.9)';
                            setTimeout(() => {
                                cardParent.style.display = 'none';
                            }, 300);
                        }
                    }
                }
            });
        });
    });

    // Console welcome message
    console.log('%c🚀 Portfolio Loaded Successfully!', 'color: #10b981; font-size: 18px; font-weight: bold;');
    console.log('%cDeveloped with ❤️ by Othman Ait Taleb', 'color: #9ca3af; font-size: 12px;');
    console.log('%cDesign: Modern & Sophisticated', 'color: #34d399; font-size: 11px;');
});

// Skills categories interactivity
function initSkillCategories(groupedSkills) {
    if (!groupedSkills) return;

    const categories = Object.keys(groupedSkills);
    const container = document.querySelector('#skill-categories');
    const skillsArea = document.querySelector('#skill-list-area');

    if (!container || !skillsArea) return;
    // If buttons already exist server-side, attach listeners instead of re-creating
    const existingButtons = container.querySelectorAll('.skill-cat-btn');
    if (existingButtons && existingButtons.length > 0) {
        existingButtons.forEach(btn => {
            const cat = btn.dataset.cat;
            btn.addEventListener('click', () => {
                // Clear active
                container.querySelectorAll('.skill-cat-btn').forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                console.log('Category clicked (server button):', cat);
                showSkillsForCategory(cat, groupedSkills[cat]);
            });
        });
    } else {
        // Render category buttons
        container.innerHTML = '';
        categories.forEach((cat, idx) => {
            const btn = document.createElement('button');
            // Use a visible outline color so buttons show on light backgrounds
            btn.className = 'btn btn-outline-primary me-2 skill-cat-btn';
            btn.textContent = cat;
            btn.dataset.cat = cat;
            container.appendChild(btn);

            btn.addEventListener('click', () => {
                // Clear active
                container.querySelectorAll('.skill-cat-btn').forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                console.log('Category clicked (client button):', cat);
                showSkillsForCategory(cat, groupedSkills[cat]);
            });
        });
    }

    function showSkillsForCategory(cat, skills) {
        skillsArea.innerHTML = '';
        if (!skills || skills.length === 0) {
            skillsArea.innerHTML = '<p class="text-muted">Aucune compétence dans cette catégorie.</p>';
            return;
        }

        const row = document.createElement('div');
        row.className = 'row';

        skills.forEach(s => {
            const col = document.createElement('div');
            col.className = 'col-md-6 col-lg-4 mb-3';

            const card = document.createElement('div');
            card.className = 'skill-card p-3 rounded shadow-sm h-100';
            card.style.transition = 'transform 0.35s ease, opacity 0.35s ease';
            card.style.opacity = '0';
            card.style.transform = 'translateY(10px)';
            card.style.color = 'var(--white)';

            const titleRow = document.createElement('div');
            titleRow.className = 'd-flex justify-content-between align-items-center mb-2';

            const name = document.createElement('span');
            name.style.color = 'var(--white)';
            name.innerHTML = `<i class="${s.icon} me-2"></i> ${s.name}`;

            const level = document.createElement('span');
            level.className = 'text-muted';
            level.textContent = s.level + '%';

            titleRow.appendChild(name);
            titleRow.appendChild(level);

            const progress = document.createElement('div');
            progress.className = 'progress';
            const bar = document.createElement('div');
            bar.className = 'progress-bar bg-primary';
            bar.setAttribute('role', 'progressbar');
            bar.style.width = '0%';
            bar.dataset.target = s.level + '%';

            progress.appendChild(bar);

            card.appendChild(titleRow);
            card.appendChild(progress);
            col.appendChild(card);
            row.appendChild(col);

            skillsArea.appendChild(row);

            // animate in
            setTimeout(() => {
                card.style.opacity = '1';
                card.style.transform = 'translateY(0)';
                bar.style.width = bar.dataset.target;
            }, 30);
        });
    }
}

// If grouped skills are present inline on the page, initialize automatically
document.addEventListener('DOMContentLoaded', function() {
    const el = document.getElementById('grouped-skills-json');
    if (el) {
        try {
            const grouped = JSON.parse(el.textContent || '{}');
            initSkillCategories(grouped);
        } catch (e) {
            console.error('Failed to parse grouped skills JSON', e);
        }
    }
});

// Utility functions
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

function throttle(func, limit) {
    let inThrottle;
    return function() {
        const args = arguments;
        const context = this;
        if (!inThrottle) {
            func.apply(context, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    };
}


