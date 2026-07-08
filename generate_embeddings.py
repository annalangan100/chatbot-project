import sqlite3
import json

from sentence_transformers import SentenceTransformer


model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


connection = sqlite3.connect(
    "data/responses.db"
)

cursor = connection.cursor()


cursor.execute(
    """
    SELECT
        id,
        user_input
    FROM responses
    WHERE embedding IS NULL
    """
)

rows = cursor.fetchall()


for row in rows:

    response_id = row[0]

    text = row[1]


    embedding = model.encode(
        text
    )


    embedding_json = json.dumps(
        embedding.tolist()
    )


    cursor.execute(
        """
        UPDATE responses
        SET embedding = ?
        WHERE id = ?
        """,
        (
            embedding_json,
            response_id
        )
    )


    print(
        f"Generated embedding for: {text}"
    )


connection.commit()

connection.close()


print(
    "All embeddings generated successfully!"
)