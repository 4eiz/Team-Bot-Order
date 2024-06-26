CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    wallet TEXT
);

CREATE TABLE IF NOT EXISTS requests (
    id INTEGER PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS requests_urls (
    id INTEGER PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY,
    text TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS fillials (
    id INTEGER PRIMARY KEY,
    url TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS urls (
    id INTEGER PRIMARY KEY,
    trial_url TEXT NOT NULL,
    trial_monitoring TEXT NOT NULL,
    paid_url TEXT NOT NULL,
    paid_monitoring TEXT NOT NULL
);