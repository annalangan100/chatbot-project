import sqlite3

connection = sqlite3.connect(
    "data/responses.db"
)

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS responses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_input TEXT NOT NULL,
    bot_response TEXT NOT NULL
)
""")

connection.commit()

connection.close()

print("Database created successfully!")