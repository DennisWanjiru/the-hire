from flask import Flask, redirect, request, render_template, url_for
from employee import Employee

app = Flask(__name__)

employees = []


@app.route('/')
def root():
    return redirect(url_for('index'))


@app.route('/index')
def index():
    return render_template('index.html', employees=employees)


@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        new_employee = Employee(request.form.get('name'), request.form.get('email'), request.form.get('category'), request.form.get('password'))
        employees.append(new_employee)

        return redirect(url_for('index'))

    return render_template('signup.html')


@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True)
