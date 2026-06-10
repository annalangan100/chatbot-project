import sqlite3
import numpy as np
from utils.embeddings import get_embedding


def get_all_responses():
    connection = sqlite3.connect("data/responses.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT user_input, bot_response
        FROM responses
    """)

    data = cursor.fetchall()
    connection.close()

    return data


def get_semantic_response(user_input):

    user_vec = get_embedding(user_input)

    data = get_all_responses()

    best_score = -1
    best_response = None

    for stored_input, bot_response in data:

        stored_vec = get_embedding(stored_input)

        score = np.dot(user_vec, stored_vec) / (
            np.linalg.norm(user_vec) *
            np.linalg.norm(stored_vec)
        )

        if score > best_score:
            best_score = score
            best_response = bot_response

    if best_score < 0.55:
        return "I don't understand that. Can you rephrase?"

    return best_response

def add_response(user_input, bot_response):

    import sqlite3

    connection = sqlite3.connect(
        "data/responses.db"
    )

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO responses
        (
            user_input,
            bot_response
        )
        VALUES (?, ?)
        """,
        (
            user_input,
            bot_response
        )
    )

    connection.commit()
    connection.close()

def get_all_knowledge():

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
            bot_response
        FROM responses
        ORDER BY id DESC
        """
    )

    knowledge = cursor.fetchall()

    connection.close()

    return knowledge

def delete_response(response_id):

    import sqlite3

    connection = sqlite3.connect(
        "data/responses.db"
    )

    cursor = connection.cursor()

    cursor.execute(
        """
        DELETE FROM responses
        WHERE id = ?
        """,
        (response_id,)
    )

    connection.commit()
    connection.close()