const deleteButton = document.querySelector('[data-delete]')
const equalsButtons = document.querySelector('[data-equals]')
const clearButton = document.querySelector('[data-all-clear]')
const numberButtons = document.querySelectorAll('[data-number]')
const operationButtons = document.querySelectorAll('[data-operator]')

/*--- TELA ---*/
const currentOperandText = document.querySelector('[data-current-operand]')
const previousOperandText = document.querySelector('[data-previous-operand]')


/*--- FUNÇÃO (limpar) ---*/
class Calculator{
    constructor(previousOperandText, currentOperandText) {
        this.previousOperandText = previousOperandText;
        this.currentOperandText = currentOperandText;
        this.clear()
    }

    formatDisplayNumber(number){
        const stringNumber = number.toString();

        const integerDigits = parseFloat(stringNumber.split(".")[0])
        const decimalDigits = stringNumber.split('.')[1]

        let integerDisplay;

        if (isNaN(integerDigits)) {
            integerDisplay = "";
        } else {
            integerDisplay = integerDigits.toLocaleString("en", {
                maximumFractionDigit: 0,
            });
        }

        if (decimalDigits != null) {
            return `${integerDisplay}.${decimalDigits}`;
        } else {
            return integerDisplay;
        }
    }

    delete(){
        this.currentOperand = this.currentOperand.toString().slice(0, -1);
    }

    calculate(){
        let result;

        const _previousOperand = parseFloat(this.previousOperand)
        const _currentOperand = parseFloat(this.currentOperand)

        if (isNaN(_previousOperand) || isNaN(_currentOperand)) return;

        switch (this.operation) {
            case '+':
                result = _previousOperand + _currentOperand;
                break;

            case '-':
                result = _previousOperand - _currentOperand;
                break;

            case '÷':
                result = _previousOperand / _currentOperand;
                break;

            case '*':
                result = _previousOperand * _currentOperand;
                break;

            default:
                return;
        }

        this.currentOperand = result
        this.operation = undefined;
        this.previousOperand = "";
    }

    chooseOperation(operation){
        if (this.currentOperand == '') return;

        if (this.previousOperand != '') {
            this.calculate()
        }

        this.operation = operation;

        this.previousOperand = this.currentOperand;
        this.currentOperand = "";
    }

    appendNumber(number) {
        if (this.currentOperand.includes(".") && number == ".") return;
        
        this.currentOperand = `${this.currentOperand}${number.toString()}`;
    }

    clear() {
        this.previousOperand = "";
        this.currentOperand = "";
        this.operation = undefined;
    }

    updateDisplay() {
        this.previousOperandText.innerText = `${this.formatDisplayNumber(this.previousOperand)} ${this.operation || ""}`;
        this.currentOperandText.innerText = this.formatDisplayNumber(this.currentOperand);
    }
}

const calculator = new Calculator(
    previousOperandText,
    currentOperandText
);

for (const numberButton of numberButtons) {
    numberButton.addEventListener('click', () => {
        calculator.appendNumber(numberButton.innerText);
        calculator.updateDisplay();
    });
}

for (const operationButton of operationButtons) {
    operationButton.addEventListener('click', () => {
        calculator.chooseOperation(operationButton.innerText);
        calculator.updateDisplay();
    });
}

clearButton.addEventListener('click', () => {
    calculator.clear()
    calculator.updateDisplay();
})

equalsButtons.addEventListener('click', () => {
    calculator.calculate();
    calculator.updateDisplay();
})

deleteButton.addEventListener('click', () => {
    calculator.delete();
    calculator.updateDisplay();
})