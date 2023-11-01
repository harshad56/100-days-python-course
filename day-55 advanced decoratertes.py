from flask import Flask
from decorator import decorator

app = Flask(__name__)


@app.route('/')  # decorter is /
def hello_world():
    return '<h1 style="text-align:center"> Hello, World!</h1>'\
        '<p> this is a para</p>'\
        '<img src="https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_1280.jpg">'


@app.route("/bye")  # decorter is /bye
def say_bye():
    return "Bye"


@app.route("/<name>/<int:number>")
def great(name, number):
    return f'Hi there {name} ,you are age is {number} year old'


if __name__ == "__main__":

    # debug mode used  for run changes
    app.run(debug=True)
