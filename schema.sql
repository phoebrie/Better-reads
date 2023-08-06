DROP TABLE IF EXISTS reviews;

CREATE TABLE
    reviews (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        rating INTEGER NOT NULL,
        content TEXT NOT NULL
    );