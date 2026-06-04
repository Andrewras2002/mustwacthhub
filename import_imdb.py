import sqlite3
import csv

conn = sqlite3.connect("movies.db")
cur = conn.cursor()

with open("imdb_top_1000.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for i, row in enumerate(reader):
        cur.execute("""
    INSERT OR IGNORE INTO movies
    (movie_id, title, year, genre, imdb_rating, runtime)
    VALUES (?, ?, ?, ?, ?, ?)
""", (
            str(i),
            row["Series_Title"],
            row["Released_Year"],
            row["Genre"],
            row["IMDB_Rating"],
            row["Runtime"]
))

conn.commit()
conn.close()

print("Imported movies from imdb_top_1000.csv")