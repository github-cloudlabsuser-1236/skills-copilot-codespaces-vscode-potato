// Function to convert Celsius to Fahrenheit
function celsiusToFahrenheit(celsius) {
    return (celsius * 9/5) + 32;
}

// Example usage
const celsius = 25;
const fahrenheit = celsiusToFahrenheit(celsius);
console.log(`${celsius}°C is equal to ${fahrenheit}°F`);


const temperatures = [0, 10, 20, 30, 40];
temperatures.forEach(temp => {
    const converted = celsiusToFahrenheit(temp);
    console.log(`${temp}°C is equal to ${converted}°F`);
});



