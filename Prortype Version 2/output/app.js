const tasks = JSON.parse(localStorage.getItem('tasks')) || [];
let currentFilter = 'all';

document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('add-task-form');
  const input = document.getElementById('new-task-input');
  const tasksList = document.getElementById('tasks-list');
  const viewAll = document.getElementById('view-all');
  const viewActive = document.getElementById('view-active');
  const viewCompleted = document.getElementById('view-completed');

  const saveTasks = () => localStorage.setItem('tasks', JSON.stringify(tasks));

  const render = () => {
    const filtered = tasks.filter(task => {
      if (currentFilter === 'active') return !task.completed;
      if (currentFilter === 'completed') return task.completed;
      return true;
    });

    tasksList.innerHTML = '';
    filtered.forEach(task => {
      const li = document.createElement('li');
      li.setAttribute('data-id', task.id);
      const checkbox = document.createElement('input');
      checkbox.type = 'checkbox';
      checkbox.checked = task.completed;
      checkbox.addEventListener('change', () => {
        task.completed = checkbox.checked;
        saveTasks();
        render();
      });
      const label = document.createElement('label');
      label.textContent = task.title;
      li.appendChild(checkbox);
      li.appendChild(label);
      tasksList.appendChild(li);
    });
  };

  form.addEventListener('submit', e => {
    e.preventDefault();
    const title = input.value.trim();
    if (!title) return;
    const task = { id: Date.now().toString(), title, completed: false };
    tasks.push(task);
    saveTasks();
    input.value = '';
    render();
  });

  viewAll.addEventListener('click', e => {
    e.preventDefault();
    currentFilter = 'all';
    render();
  });
  viewActive.addEventListener('click', e => {
    e.preventDefault();
    currentFilter = 'active';
    render();
  });
  viewCompleted.addEventListener('click', e => {
    e.preventDefault();
    currentFilter = 'completed';
    render();
  });

  render();
});