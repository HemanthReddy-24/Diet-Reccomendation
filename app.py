from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import json

app = Flask(__name__)

# Load the trained model
model = joblib.load('calorie_model.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/bmi')
def bmi():
    return render_template('bmi.html')

@app.route('/calorie', methods=['GET', 'POST'])
def calorie():
    if request.method == 'POST':
        age = int(request.form['age'])
        height = float(request.form['height'])
        weight = float(request.form['weight'])
        gender = int(request.form['gender'])
        
        # Prepare the input data
        input_data = np.array([[age, height, weight, gender]])
        
        # Make the prediction
        prediction = model.predict(input_data)[0]
        
        return render_template('calorie.html', prediction=prediction)
    return render_template('calorie.html', prediction=None)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/diet', methods=['GET', 'POST'])
def diet():
    if request.method == 'POST':
        if 'json_file' in request.files:
            json_file = request.files['json_file']
            data = json.load(json_file)
            age = data['age']
            height = data['height']
            weight = data['weight']
            gender = data['gender']
        else:
            age = int(request.form['age'])
            height = float(request.form['height'])
            weight = float(request.form['weight'])
            gender = int(request.form['gender'])
        
        # Prepare the input data
        input_data = np.array([[age, height, weight, gender]])
        
        # Make the prediction
        prediction = model.predict(input_data)[0]
        
        return render_template('diet.html', prediction=prediction)
    return render_template('diet.html', prediction=None)

if __name__ == '__main__':
    app.run(debug=True)
