# app.py
from flask import Flask, render_template

app = Flask(__name__)

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

@app.route('/calorie')
def calorie():
    return render_template('calorie.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/diet')
def diet():
    return render_template('diet.html')


if __name__ == '__main__':
    app.run(debug=True)
