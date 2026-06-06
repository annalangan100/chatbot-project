from flask import Flask, render_template, request
import json

from utils.intent_handler import get_response
from utils.memory import load_user_data
from utils.memory_commands import handle_memory_command

app = Flask(__name__)

with open("intents.json", "r") as file:
    intents = json.load(file)

user_data = load_user_data()

chat_history = []

@app.route("/", methods=["GET", "POST"])
def home():

    global chat_history

    response = ""


    if request.method == "POST":

        user_input = request.form["message"].lower()

        memory_response = handle_memory_command(
            user_input,
            user_data
        )

        if memory_response:

            response = memory_response

        else:

            response = get_response(
                user_input,
                intents
            )

        chat_history.append(
            {
                "user": user_input,
                "bot": response
            }
        )

    return render_template(
        "index.html",
        chat_history=chat_history
)


if __name__ == "__main__":
    app.run(debug=True)