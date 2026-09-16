import sqlite3

from flask import Flask, redirect, render_template, request, url_for

all_books = [
    {
        "title": "Harry Potter and the chamber of secret",
        "author": "J.K. Rowling",
        "rating": 9,
    }
]

db = sqlite3.connect("books-collection.db")
cursor = db.cursor()

# cursor.execute(
#    "CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, "
#  "author varchar(250) NOT NULL, rating FLOAT NOT NULL)"
# )

cursor.execute(
    "INSERT INTO books (title, author, rating) "
    "VALUES ('Harry Potter', 'J. K. Rowling', 9.3)"
)

cursor.execute(
    "INSERT INTO books (title, author, rating) "
    "VALUES ('The Hobbit', 'J.R.R. Tolkien', 8.7)"
)

db.commit()
db.close()

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        new_book = {
            "title": request.form["title"],
            "author": request.form["author"],
            "rating": request.form["rating"],
        }
        all_books.append(new_book)

        return redirect(url_for("index"))

    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)
