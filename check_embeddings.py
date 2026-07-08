import sqlite3


connection = sqlite3.connect(
    "data/responses.db"
)

cursor = connection.cursor()


cursor.execute(
    """
    SELECT
        id,
        user_input,
        LENGTH(embedding)
    FROM responses
    """
)


rows = cursor.fetchall()


for row in rows:
    print(row)


connection.close()