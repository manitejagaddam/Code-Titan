/* app.js – Todo List CRUD */

// ---------------------------
// Utility helpers
// ---------------------------
const generateId = () => Date.now().toString();

const saveToLocalStorage = todos => localStorage.setItem('todos', JSON.stringify(todos));

const loadFromLocalStorage = () => {
  const data = localStorage.getItem('todos');
  return data ? JSON.parse(data) : [];
};

// ---------------------------
// State
// ---------------------------
let todos = loadFromLocalStorage();

// ---------------------------
// Rendering
// ---------------------------
const todoListEl = document.getElementById('todo-list');
const renderTodos = () => {
  todoListEl.innerHTML = '';
  todos.forEach(todo => {
    const li = document.createElement('li');
    li.className = 'todo-item';
    li.dataset.id = todo.id;

    const span = document.createElement('span');
    span.className = 'todo-text';
    span.textContent = todo.text;
    span.style.textDecoration = todo.completed ? 'line-through' : 'none';

    const completeBtn = document.createElement('button');
    completeBtn.className = 'complete-btn';
    completeBtn.ariaLabel = 'Mark complete';
    completeBtn.textContent = '✓';

    const editBtn = document.createElement('button');
    editBtn.className = 'edit-btn';
    editBtn.ariaLabel = 'Edit todo';
    editBtn.textContent = '✎';

    const deleteBtn = document.createElement('button');
    deleteBtn.className = 'delete-btn';
    deleteBtn.ariaLabel = 'Delete todo';
    deleteBtn.textContent = '✕';

    li.append(span, completeBtn, editBtn, deleteBtn);
    todoListEl.appendChild(li);
  });
};

// ---------------------------
// CRUD operations
// ---------------------------
const addTodo = text => {
  const newTodo = { id: generateId(), text, completed: false };
  todos.push(newTodo);
  saveToLocalStorage(todos);
  renderTodos();
};

const deleteTodo = id => {
  todos = todos.filter(todo => todo.id !== id);
  saveToLocalStorage(todos);
  renderTodos();
};

const toggleComplete = id => {
  todos = todos.map(todo => {
    if (todo.id === id) return { ...todo, completed: !todo.completed };
    return todo;
  });
  saveToLocalStorage(todos);
  renderTodos();
};

const editTodo = (id, newText) => {
  todos = todos.map(todo => {
    if (todo.id === id) return { ...todo, text: newText };
    return todo;
  });
  saveToLocalStorage(todos);
  renderTodos();
};

// ---------------------------
// Event listeners
// ---------------------------
document.getElementById('todo-form').addEventListener('submit', e => {
  e.preventDefault();
  const input = document.getElementById('new-todo-input');
  const text = input.value.trim();
  if (!text) return;
  addTodo(text);
  input.value = '';
});

todoListEl.addEventListener('click', e => {
  const li = e.target.closest('.todo-item');
  if (!li) return;
  const id = li.dataset.id;

  if (e.target.matches('.complete-btn')) {
    toggleComplete(id);
  } else if (e.target.matches('.delete-btn')) {
    deleteTodo(id);
  } else if (e.target.matches('.edit-btn')) {
    startEdit(li, id);
  }
});

function startEdit(li, id) {
  const span = li.querySelector('.todo-text');
  const currentText = span.textContent;
  const input = document.createElement('input');
  input.type = 'text';
  input.className = 'edit-input';
  input.value = currentText;
  input.style.width = '70%';
  span.replaceWith(input);
  input.focus();

  const finish = newText => {
    input.replaceWith(span);
    editTodo(id, newText);
  };

  // Save on Enter
  input.addEventListener('keydown', e => {
    if (e.key === 'Enter') finish(input.value.trim() || currentText);
  });

  // Save on blur
  input.addEventListener('blur', () => finish(input.value.trim() || currentText));
}

// Initial render
renderTodos();
