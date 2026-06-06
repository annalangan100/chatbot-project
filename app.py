from flask import Flask, render_template, request
import json

from utils.intent_handler import get_response

app = Flask(__name__)

with open("intents.json", "r") as file:
    intents = json.load(file)

@app.route("/", methods=["GET", "POST"])
def home():

    response = ""

    if request.method == "POST":

        user_input = request.form["message"].lower()

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