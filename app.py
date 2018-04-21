from flask import Flask, redirect, url_for
from employee import Employee

app = Flask(__name__)

employees = []


@app.route('/')
def root():
    return redirect(url_for('signup'))


@app.route('/signup')
def signup():
    return 'Sign Up'


@app.route('/login')
def login():
    return 'Log in'


if __name__ == "__main__":
    app.run(debug=True)
