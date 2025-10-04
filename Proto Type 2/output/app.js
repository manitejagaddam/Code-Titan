document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('#add-task form');
    const taskList = document.getElementById('task-list');

    form.addEventListener('submit', e => {
        e.preventDefault();
        const titleInput = document.getElementById('task-title');
        const descInput = document.getElementById('task-desc');
        const title = titleInput.value.trim();
        const desc = descInput.value.trim();

        if (!title) return;

        const li = document.createElement('li');
        li.innerHTML = `
            <article>
                <h3>${title}</h3>
                <p>${desc}</p>
                <button type="button" aria-label="Edit task" class="edit-task">Edit</button>
                <button type="button" aria-label="Delete task" class="delete-task">Delete</button>
            </article>
        `;

        taskList.appendChild(li);
        titleInput.value = '';
        descInput.value = '';
    });

    taskList.addEventListener('click', e => {
        const target = e.target;
        if (target.matches('.edit-task')) {
            const article = target.closest('article');
            const title = article.querySelector('h3').textContent;
            const desc = article.querySelector('p').textContent;
            article.dataset.title = title;
            article.dataset.desc = desc;
            article.innerHTML = `
                <label>Title</label>
                <input type="text" class="edit-title" value="${title}">
                <label>Description</label>
                <textarea class="edit-desc">${desc}</textarea>
                <button type="button" class="save-task">Save</button>
                <button type="button" class="cancel-task">Cancel</button>
            `;
        } else if (target.matches('.delete-task')) {
            const li = target.closest('li');
            if (li) li.remove();
        } else if (target.matches('.save-task')) {
            const article = target.closest('article');
            const newTitle = article.querySelector('.edit-title').value.trim() || article.dataset.title;
            const newDesc = article.querySelector('.edit-desc').value.trim() || article.dataset.desc;
            article.innerHTML = `
                <h3>${newTitle}</h3>
                <p>${newDesc}</p>
                <button type="button" aria-label="Edit task" class="edit-task">Edit</button>
                <button type="button" aria-label="Delete task" class="delete-task">Delete</button>
            `;
        } else if (target.matches('.cancel-task')) {
            const article = target.closest('article');
            const title = article.dataset.title;
            const desc = article.dataset.desc;
            article.innerHTML = `
                <h3>${title}</h3>
                <p>${desc}</p>
                <button type="button" aria-label="Edit task" class="edit-task">Edit</button>
                <button type="button" aria-label="Delete task" class="delete-task">Delete</button>
            `;
        }
    });
});