const display = document.getElementById('display');
let currentOperand = '0';
let previousOperand = '';
let operator = null;

function updateDisplay() {
  display.textContent = currentOperand;
}

function resetCalculator() {
  currentOperand = '0';
  previousOperand = '';
  operator = null;
  updateDisplay();
}

function deleteDigit() {
  if (currentOperand.length === 1 || (currentOperand.length === 2 && currentOperand.startsWith('-'))) {
    currentOperand = '0';
  } else {
    currentOperand = currentOperand.slice(0, -1);
  }
  updateDisplay();
}

function appendDigit(digit) {
  if (currentOperand === '0') {
    currentOperand = digit;
  } else {
    currentOperand += digit;
  }
  updateDisplay();
}

function appendDecimal() {
  if (!currentOperand.includes('.')) {
    currentOperand += '.';
  }
  updateDisplay();
}

function setOperator(op) {
  if (operator && previousOperand) {
    compute();
  }
  previousOperand = currentOperand;
  operator = op;
  currentOperand = '0';
  updateDisplay();
}

function compute() {
  if (!operator || !previousOperand) return;
  const prev = parseFloat(previousOperand);
  const current = parseFloat(currentOperand);
  let result;
  switch (operator) {
    case 'divide':
      result = prev / current;
      break;
    case 'multiply':
      result = prev * current;
      break;
    case 'add':
      result = prev + current;
      break;
    case 'subtract':
      result = prev - current;
      break;
    default:
      return;
  }
  if (!isFinite(result)) {
    currentOperand = 'Error';
  } else {
    currentOperand = result.toString();
  }
  previousOperand = '';
  operator = null;
  updateDisplay();
}

function handleButtonClick(e) {
  const btn = e.target;
  const digit = btn.dataset.digit;
  const action = btn.dataset.action;
  const decimal = btn.dataset.decimal;
  if (digit !== undefined) {
    appendDigit(digit);
  } else if (decimal !== undefined) {
    appendDecimal();
  } else if (action !== undefined) {
    switch (action) {
      case 'clear':
        resetCalculator();
        break;
      case 'delete':
        deleteDigit();
        break;
      case 'divide':
      case 'multiply':
      case 'add':
      case 'subtract':
        setOperator(action);
        break;
      case 'equals':
        compute();
        break;
    }
  }
}

document.querySelectorAll('button').forEach(btn => btn.addEventListener('click', handleButtonClick));

resetCalculator();
