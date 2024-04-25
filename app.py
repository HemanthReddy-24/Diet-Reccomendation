from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# Load the dataset
data = pd.read_csv('diet_dataset.csv')

# Data Preprocessing
# (e.g., handle missing values, encode categorical variables)

# Feature Engineering
# (e.g., calculate BMI)

# Train the model
X = data[['age', 'weight(kg)', 'height(m)', 'gender']]  # Features
y = data['calories_to_maintain_weight']  # Target variable
model = LinearRegression()
model.fit(X, y)

@app.route('/')
def index():
    return render_template('calorie.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get user input from the request
    input_data = request.get_json()

    # Extract input values
    age = input_data['age']
    weight = input_data['weight']
    height = input_data['height']
    gender = input_data['gender']

    # Encode gender
    gender_encoded = 1 if gender.lower() == 'male' else 0

    # Make prediction
    new_data = pd.DataFrame({'age': [age], 'weight(kg)': [weight], 'height(m)': [height], 'gender': [gender_encoded]})
    predicted_calories = model.predict(new_data)

    # Return the predicted result
    return jsonify({'predicted_calories': predicted_calories[0]})


if __name__ == '__main__':
    app.run(debug=True)
