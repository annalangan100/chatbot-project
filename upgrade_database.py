import sqlite3

connection = sqlite3.connect(
    "data/responses.db"
)

cursor = connection.cursor()

try:

    cursor.execute(
        """
        ALTER TABLE responses
        ADD COLUMN embedding TEXT
        """
    )

    print(
        "Embedding column added."
    )

except sqlite3.OperationalError:

    print(
        "Embedding column already exists."
    )

connection.commit()
connection.close()