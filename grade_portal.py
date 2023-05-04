from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect

import sqlite3

USER = "admin"
PASSWORD = "password"

app = Flask(__name__)
app.config['SECRET_KEY'] = 'this should be a secret random string'


def get_db_connection():
    """
    Get me a connection to the database
    :return:
    """
    conn = sqlite3.connect('studentquizzes.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def root():
    return render_template("login.html", message=None)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form["user"]
        password = request.form["password"]

        if username == USER and password == PASSWORD:
            return redirect(url_for("dashboard"))
        else:
            return render_template("login.html", message="Wrong User or Password")
    else:
        return render_template("login.html", message=None)


@app.route('/dashboard')
def dashboard():
    quizzes_qry = "select quiz_id, subject, questions, quiz_date from quizzes"

    conn = get_db_connection()
    students = conn.execute("select student_id, first, last from students").fetchall()
    quizzes_dataset = conn.execute(quizzes_qry).fetchall()

    return render_template("dashboard.html", students=students, quizzes=quizzes_dataset)


@app.route('/addstudent', methods=['POST', 'GET'])
def add_student():
    if request.method == 'POST':
        first_name = request.form["first"]
        last_name = request.form["last"]

        conn = get_db_connection()
        conn.execute("INSERT INTO students(FIRST, last) VALUES(?, ?);", (first_name, last_name))
        conn.commit()

        return redirect(url_for("dashboard"))
    else:
        return render_template("add_student.html")


@app.route('/deletestudent/<student_id>')
def delete_student(student_id):
    conn = get_db_connection()
    conn.execute("DELETE from students where student_id = (?);", (student_id,))
    conn.commit()
    return redirect(url_for("dashboard"))


@app.route('/addquizz')
def add_quizz():
    pass


@app.route('/viewresult/<quiz_id>')
def view_quiz_result(quiz_id):

    conn = get_db_connection()
    quiz = conn.execute("select subject, questions, quiz_date from quizzes WHERE quiz_id = (?);", (quiz_id,)).fetchone()
    quiz_results = conn.execute(
        "SELECT s.first, s.last, score FROM students_results r join students s "
        "on r.student_id = s.student_id where r.quiz_id = (?);", (quiz_id,)
    ).fetchall()

    return render_template("quiz_results.html", quiz=quiz, results=quiz_results)


if __name__ == '__main__':
    app.run(debug=True)
