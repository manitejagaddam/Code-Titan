// app.js
document.addEventListener('DOMContentLoaded', () => {
    const display = document.getElementById('display');
    const buttons = document.querySelector('.buttons');

    buttons.addEventListener('click', e => {
        const target = e.target;
        if (!target.matches('button')) return;

        const action = target.dataset.action;
        const value  = target.dataset.value;

        if (action === 'clear') {
            display.value = '';
        } else if (action === 'delete') {
            display.value = display.value.slice(0, -1);
        } else if (action === 'calculate') {
            try {
                const expr = display.value
                    .replace(/÷/g, '/')
                    .replace(/×/g, '*');
                // evaluate safely
                const result = eval(expr);
                display.value = result;
            } catch {
                display.value = 'Error';
            }
        } else if (value) {
            display.value += value;
        }
    });
});
