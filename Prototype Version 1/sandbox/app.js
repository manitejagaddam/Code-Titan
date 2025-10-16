document.addEventListener('DOMContentLoaded', () => {
  const videos = [
    {id: 1, title: 'JavaScript Basics', channel: 'Code Academy', thumbnail: 'https://via.placeholder.com/120x90?text=JS', desc: 'Learn JS basics'},
    {id: 2, title: 'Advanced CSS', channel: 'Design Hub', thumbnail: 'https://via.placeholder.com/120x90?text=CSS', desc: 'Deep dive into CSS'},
    {id: 3, title: 'Node.js Tutorial', channel: 'Dev Talk', thumbnail: 'https://via.placeholder.com/120x90?text=Node', desc: 'Node.js for beginners'},
    {id: 4, title: 'React Components', channel: 'Front End', thumbnail: 'https://via.placeholder.com/120x90?text=React', desc: 'Building React components'}
  ];
  const subscriptions = [
    {name: 'Code Academy', avatar: 'https://via.placeholder.com/50?text=CA'},
    {name: 'Design Hub', avatar: 'https://via.placeholder.com/50?text=DH'},
    {name: 'Dev Talk', avatar: 'https://via.placeholder.com/50?text=DT'}
  ];
  const videoListEl = document.querySelector('.video-list');
  const subscriptionListEl = document.querySelector('.subscription-list');
  const featuredEl = document.querySelector('.video-placeholder');
  const searchForm = document.querySelector('form[role="search"]');
  function renderVideos(list) {
    videoListEl.innerHTML = '';
    list.forEach(v => {
      const div = document.createElement('div');
      div.className = 'video-item';
      div.innerHTML = `<img src="${v.thumbnail}" alt="${v.title}"><div class="info"><h3>${v.title}</h3><p>${v.channel}</p></div>`;
      videoListEl.appendChild(div);
    });
  }
  function renderSubscriptions() {
    subscriptionListEl.innerHTML = '';
    subscriptions.forEach(s => {
      const div = document.createElement('div');
      div.className = 'subscription-item';
      div.innerHTML = `<img src="${s.avatar}" alt="${s.name}"><p>${s.name}</p>`;
      subscriptionListEl.appendChild(div);
    });
  }
  renderVideos(videos);
  renderSubscriptions();
  featuredEl.innerHTML = `<h3>${videos[0].title}</h3><p>Featured from ${videos[0].channel}</p>`;
  searchForm.addEventListener('submit', e => {
    e.preventDefault();
    const q = searchForm.q.value.toLowerCase();
    const filtered = videos.filter(v => v.title.toLowerCase().includes(q) || v.channel.toLowerCase().includes(q));
    renderVideos(filtered);
  });
});
