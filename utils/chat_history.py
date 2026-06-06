import json
import os

CHAT_HISTORY_FILE = "data/chat_history.json"


def load_chat_history():

    if os.path.exists(CHAT_HISTORY_FILE):

        with open(
            CHAT_HISTORY_FILE,
            "r"
        ) as file:

            return json.load(file)

    return []


def save_chat_history(chat_history):

    with open(
        CHAT_HISTORY_FILE,
        "w"
    ) as file:

        json.dump(
            chat_history,
            file,
            indent=4
        )