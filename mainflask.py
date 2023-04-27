from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

storage = {'Alain', 'Peter', 'John'}

@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/helloform')
def hello_form():
    return render_template("helloform.html")


@app.route('/hello')
@app.route('/hello/<username>')
def hello_user(username=None):

    if not username:
        username = "World"

    storage.add(username)
    return render_template("hello.html", userparam=username, names=storage)


@app.route('/helloaction', methods=['POST', 'GET'])
def hello_action():
    if request.method == 'POST':
        username = request.form["user"]
        storage.add(username)

        return render_template("hello.html", userparam=username, names=storage)


@app.route('/erase/<username>')
def hello_erase(username="World"):
    if username in storage:
        storage.remove(username)

    return render_template("hello_delete.html", userparam=username, names=storage)


if __name__ == '__main__':
    app.run(debug=True)
