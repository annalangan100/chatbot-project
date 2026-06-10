import sqlite3

connection = sqlite3.connect(
    "data/responses.db"
)

cursor = connection.cursor()

cursor.execute(
    "SELECT COUNT(*) FROM responses"
)

count = cursor.fetchone()[0]

connection.close()

print(
    f"Number of responses: {count}"
)