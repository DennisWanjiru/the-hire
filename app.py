from flask import Flask, redirect, request, render_template, url_for
from employee import Employee

app = Flask(__name__)

employees = [Employee('Dennis Wanjiru', 'denniswanjiru71@gmail.com', 'first', 'password')]


def find_user(email):
    return [user for user in employees if user.email == email]


@app.route('/')
def root():
    return redirect(url_for('login'))


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


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = find_user(email)

        if user != []:
            if password == user[0].password:
                return user[0].name
            return "Incorrect Credentials"
        return "Incorrect Credentials"

    return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True)
