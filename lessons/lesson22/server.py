from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def receive_data():
    username = request.form.get("name", "")
    userpassword = request.form.get("password", "")

    return "<p>Thank you!!!</p>"


if __name__ == "__main__":
    app.run(debug=True)
