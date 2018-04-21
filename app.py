from flask import Flask, redirect, render_template, url_for
from employee import Employee

app = Flask(__name__)

employees = []


@app.route('/')
def root():
    return redirect(url_for('signup'))


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True)
