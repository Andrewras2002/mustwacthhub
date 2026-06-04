DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS movies;
DROP TABLE IF EXISTS watchlist;

CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT
);

CREATE TABLE movies (
    movie_id TEXT PRIMARY KEY,
    title TEXT,
    year INTEGER,
    genre TEXT,
    imdb_rating REAL,
    runtime TEXT
);

CREATE TABLE watchlist (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    movie_id TEXT,
    status TEXT,
    personal_rating INTEGER,
    review TEXT,
    FOREIGN KEY(user_id) REFERENCES users(user_id),
    FOREIGN KEY(movie_id) REFERENCES movies(movie_id)
);