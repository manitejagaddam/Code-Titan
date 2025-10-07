"use strict";

const taskForm = document.getElementById("taskForm");
const taskIdInput = document.getElementById("task-id");
const taskTitleInput = document.getElementById("task-title");
const taskDescInput = document.getElementById("task-desc");
const addTaskBtn = document.getElementById("add-task-btn");
const cancelBtn = document.getElementById("cancel-btn");
const tasksList = document.getElementById("tasks");

function getTasks() {
  const data = localStorage.getItem("tasks");
  return data ? JSON.parse(data) : [];
}
function setTasks(tasks) {
  localStorage.setItem("tasks", JSON.stringify(tasks));
}
function renderTasks() {
  const tasks = getTasks();
  tasksList.innerHTML = "";
  tasks.forEach(task => {
    const li = document.createElement("li");
    li.dataset.id = task.id;
    li.innerHTML = `
      <strong>${task.title}</strong>
      <p>${task.desc || ""}</p>
      <button class="edit-btn" aria-label="Edit task">Edit</button>
      <button class="delete-btn" aria-label="Delete task">Delete</button>
    `;
    tasksList.appendChild(li);
  });
}
function clearForm() {
  taskIdInput.value = "";
  taskTitleInput.value = "";
  taskDescInput.value = "";
  taskTitleInput.focus();
}
function handleAddTaskClick() {
  clearForm();
}
function handleCancelClick() {
  clearForm();
}
function handleFormSubmit(e) {
  e.preventDefault();
  const id = taskIdInput.value;
  const title = taskTitleInput.value.trim();
  const desc = taskDescInput.value.trim();
  if (!title) return;
  const tasks = getTasks();
  if (id) {
    const index = tasks.findIndex(t => t.id === id);
    if (index > -1) tasks[index] = { id, title, desc };
  } else {
    const newTask = { id: Date.now().toString(), title, desc };
    tasks.push(newTask);
  }
  setTasks(tasks);
  renderTasks();
  clearForm();
}
function handleTasksListClick(e) {
  const li = e.target.closest("li");
  if (!li) return;
  const id = li.dataset.id;
  const tasks = getTasks();
  if (e.target.classList.contains("edit-btn")) {
    const task = tasks.find(t => t.id === id);
    if (task) {
      taskIdInput.value = task.id;
      taskTitleInput.value = task.title;
      taskDescInput.value = task.desc;
      taskTitleInput.focus();
    }
  } else if (e.target.classList.contains("delete-btn")) {
    const filtered = tasks.filter(t => t.id !== id);
    setTasks(filtered);
    renderTasks();
  }
}
document.addEventListener("DOMContentLoaded", () => {
  renderTasks();
  addTaskBtn.addEventListener("click", handleAddTaskClick);
  cancelBtn.addEventListener("click", handleCancelClick);
  taskForm.addEventListener("submit", handleFormSubmit);
  tasksList.addEventListener("click", handleTasksListClick);
});