// Calculator class to handle operations
class Calculator {
    add(a, b) {
        return a + b;
    }

    subtract(a, b) {
        return a - b;
    }

    multiply(a, b) {
        return a * b;
    }

    divide(a, b) {
        if (b === 0) {
            throw new Error("Division by zero is not allowed.");
        }
        return a / b;
    }
}

// Main function to interact with the user
function main() {
    const calculator = new Calculator();
    const prompt = require('prompt-sync')();

    console.log("Welcome to the Calculator!");
    console.log("Available operations:");
    console.log("1. Add");
    console.log("2. Subtract");
    console.log("3. Multiply");
    console.log("4. Divide");

    const choice = prompt("Enter your choice (1/2/3/4): ");
    const num1 = parseFloat(prompt("Enter the first number: "));
    const num2 = parseFloat(prompt("Enter the second number: "));

    try {
        let result;
        switch (choice) {
            case "1":
                result = calculator.add(num1, num2);
                console.log(`Result: ${result}`);
                break;
            case "2":
                result = calculator.subtract(num1, num2);
                console.log(`Result: ${result}`);
                break;
            case "3":
                result = calculator.multiply(num1, num2);
                console.log(`Result: ${result}`);
                break;
            case "4":
                result = calculator.divide(num1, num2);
                console.log(`Result: ${result}`);
                break;
            default:
                console.log("Invalid choice. Please select a valid operation.");
        }
    } catch (error) {
        console.error(`Error: ${error.message}`);
    }
}

// Run the program
main();