import sqlite3

conn = sqlite3.connect('books.db')

c = conn.cursor()

# create a table
c.execute("""
CREATE TABLE IF NOT EXISTS books (
        title TEXT,
        price REAL,
        link TEXT,
        img_link TEXT
)
""")

