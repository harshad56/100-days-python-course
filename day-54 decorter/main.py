from flask import Flask

app = Flask(__name__)


@app.route('/')  # decorter is /
def hello_world():
    return 'Hello, World!'


@app.route("/bye")  # decorter is /bye
def say_bye():
    return "Bye"


if __name__ == "__main__":
    app.run()
