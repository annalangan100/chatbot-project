from flask import Flask, render_template, request
import json

from utils.intent_handler import get_response
from utils.memory import load_user_data
from utils.memory_commands import handle_memory_command

app = Flask(__name__)

with open("intents.json", "r") as file:
    intents = json.load(file)

user_data = load_user_data()

@app.route("/", methods=["GET", "POST"])
def home():

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

    return render_template(
        "index.html",
        response=response
    )


if __name__ == "__main__":
    app.run(debug=True)