function calculateBMI() {
    var gender = document.getElementById("gender").value;
    var age = parseFloat(document.getElementById("age").value);
    var height = parseFloat(document.getElementById("height").value);
    var weight = parseFloat(document.getElementById("weight").value);

    if (isNaN(age) || isNaN(height) || isNaN(weight)) {
        alert("Please enter valid values for age, height, and weight.");
        return;
    }

    var bmi = weight / ((height / 100) * (height / 100));

    var interpretation = "";
    if (bmi < 18.5) {
        interpretation = "Underweight";
    } else if (bmi >= 18.5 && bmi < 24.9) {
        interpretation = "Normal weight";
    } else if (bmi >= 25 && bmi < 29.9) {
        interpretation = "Overweight";
    } else {
        interpretation = "Obese";
    }

    document.getElementById("result").innerHTML = "<p>Your BMI: " + bmi.toFixed(2) + "</p><p>Interpretation: " + interpretation + "</p>";
}