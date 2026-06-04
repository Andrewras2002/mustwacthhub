import sqlite3
import re
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

def db():
    conn = sqlite3.connect("movies.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def index():
    conn = db()
    movies = conn.execute("SELECT * FROM movies LIMIT 200").fetchall()
    conn.close()
    return render_template("index.html", movies=movies)


@app.route("/add_watchlist/<movie_id>", methods=["POST"])
def add_watchlist(movie_id):
    status = request.form["status"]

    conn = db()
    conn.execute(
        "INSERT INTO watchlist (user_id, movie_id, status) VALUES (1, ?, ?)",
        (movie_id, status)
    )
    conn.commit()
    conn.close()

    return redirect("/")


@app.route("/watchlist")
def watchlist():
    conn = db()
    watchlist = conn.execute("""
        SELECT watchlist.id, movies.title, movies.year, movies.genre,
               watchlist.status, watchlist.personal_rating, watchlist.review
        FROM watchlist
        JOIN movies ON watchlist.movie_id = movies.movie_id
        WHERE watchlist.user_id = 1
    """).fetchall()
    conn.close()

    return render_template("watchlist.html", watchlist=watchlist)


@app.route("/rate_watchlist/<int:id>", methods=["POST"])
def rate_watchlist(id):
    personal_rating = request.form.get("personal_rating")
    review = request.form.get("review")

    conn = db()
    conn.execute("""
        UPDATE watchlist
        SET personal_rating = ?, review = ?
        WHERE id = ?
    """, (personal_rating, review, id))
    conn.commit()
    conn.close()

    return redirect("/watchlist")


@app.route("/delete_watchlist/<int:id>")
def delete_watchlist(id):
    conn = db()
    conn.execute("DELETE FROM watchlist WHERE id = ?", (id,))
    conn.commit()
    conn.close()

    return redirect("/watchlist")


@app.route("/search")
def search():
    pattern = request.args.get("pattern", "")

    conn = db()
    movies = conn.execute("SELECT * FROM movies").fetchall()
    conn.close()

    results = []

    for m in movies:
        text = f"{m['title']} {m['genre']}"
        try:
            if re.search(pattern, text, re.IGNORECASE):
                results.append(m)
        except:
            pass

    return render_template("index.html", movies=results)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)