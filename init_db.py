import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    #schema = f.read()
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO reviews (title, author, rating, content) VALUES (?, ?, ?, ?)",
            ('Children of Time', 'Adrian Tchaikovsky', 5, 'This book was an excellent first foray into the space opera genre.')
            )

cur.execute("INSERT INTO reviews (title, author, rating, content) VALUES (?, ?, ?, ?)", 
            ('The Dinner Guest', 'B.P. Walter', 5, 'What really set this book apart was the characters, even when the plot was slow I wanted to learn more about them.')
            )

connection.commit()
connection.close()