document.addEventListener('DOMContentLoaded', () => {
  const navLinks = document.querySelectorAll('nav a');
  const sections = document.querySelectorAll('main section');

  const style = document.createElement('style');
  style.textContent = `
    nav a.active{color:#007bff;font-weight:bold;}
    #scrollTop{position:fixed;bottom:20px;right:20px;padding:10px;font-size:1.2rem;display:none;cursor:pointer;background:#007bff;color:#fff;border:none;border-radius:4px;}
  `;
  document.head.appendChild(style);

  const scrollTopBtn = document.createElement('button');
  scrollTopBtn.id = 'scrollTop';
  scrollTopBtn.textContent = '↑';
  document.body.appendChild(scrollTopBtn);

  const observer = new IntersectionObserver(
    entries => {
      entries.forEach(entry => {
        const id = entry.target.id;
        const link = document.querySelector(`nav a[href="#${id}"]`);
        if (link) link.classList.toggle('active', entry.isIntersecting && entry.intersectionRatio > 0.5);
      });
    },
    { threshold: 0.5 }
  );
  sections.forEach(sec => observer.observe(sec));

  navLinks.forEach(link => {
    link.addEventListener('click', e => {
      e.preventDefault();
      const target = document.querySelector(link.getAttribute('href'));
      if (target) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
  });

  window.addEventListener('scroll', () => {
    scrollTopBtn.style.display = window.scrollY > 300 ? 'block' : 'none';
  });

  scrollTopBtn.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
});