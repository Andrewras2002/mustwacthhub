DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS movies;
DROP TABLE IF EXISTS watchlist;
DROP TABLE IF EXISTS streaming_services;
DROP TABLE IF EXISTS available_on;

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

CREATE TABLE streaming_services (
    service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
);

CREATE TABLE available_on (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    movie_id TEXT,
    service_id INTEGER,
    FOREIGN KEY(movie_id) REFERENCES movies(movie_id),
    FOREIGN KEY(service_id) REFERENCES streaming_services(service_id)
);

INSERT INTO users (username) VALUES ('Andrew');

INSERT INTO streaming_services (name) VALUES
('Netflix'),
('HBO Max'),
('Disney+'),
('Amazon Prime');