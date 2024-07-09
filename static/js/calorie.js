function predictCalories() {
    // Get input values
    var age = document.getElementById("age").value;
    var weight = document.getElementById("weight").value;
    var height = document.getElementById("height").value;
    var gender = document.getElementById("gender").value;

    // Prepare data to send to server
    var data = {
        age: parseFloat(age),
        weight: parseFloat(weight),
        height: parseFloat(height),
        gender: gender
    };

    // Send data to server
    fetch('/predict_calories', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        // Display predicted result
        document.getElementById('result').innerHTML = 'Predicted Calories to Maintain Weight: ' + data.predicted_calories;
    })
    .catch(error => console.error('Error:', error));
}