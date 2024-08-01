import sqlite3
import hashlib

# Establish a connection to the SQLite database file 'userdata.db'
conn = sqlite3.connect('userdata.db')
# Create a cursor object to interact with the database
cur = conn.cursor()

# Execute a SQL statement to create a table 'userdata' if it doesn't already exist
cur.execute("""
    CREATE TABLE IF NOT EXISTS userdata (
        Id INTEGER PRIMARY KEY,
        username VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL
    )
""")

# Define usernames and passwords with SHA-256 hashing
username1, password1 = "meakmeals3", hashlib.sha256("ManManDookieIT".encode()).hexdigest()
username2, password2 = "2pacsOfGum", hashlib.sha256("50centsForCandy3".encode()).hexdigest()
username3, password3 = "milkymilkM3CSL", hashlib.sha256("IownYou44".encode()).hexdigest()
username4, password4 = "50ShadesofGravy101", hashlib.sha256("3thingsofCheese3".encode()).hexdigest()

# Insert data into the 'userdata' table
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username1, password1))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username2, password2))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username3, password3))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username4, password4))

conn.commit()
