from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Bonjour, World!</p>"


@app.route("/bye")
def say_bye():
    return "<p>Bye</p>"


# adding variable name to route
@app.route("/username/<name>")
def greet_username(name):
    return f"<p>Hello, {name}</p>"


if __name__ == "__main__":
    app.run(debug=True)
