import sqlite3

connection = sqlite3.connect(
    "data/responses.db"
)

cursor = connection.cursor()

responses = [
    ("hello", "Hi there!"),
    ("hi", "Hello!"),
    ("bye", "Goodbye!"),
    ("what is python", "Python is a programming language."),
    ("who made you", "I was created by Anna."),
    ("what is your name", "My name is Echo.")
]

cursor.executemany(
    """
    INSERT INTO responses
    (user_input, bot_response)
    VALUES (?, ?)
    """,
    responses
)

connection.commit()

connection.close()

print("Responses added successfully!")