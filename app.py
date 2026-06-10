from flask import Flask, render_template, request, redirect

from utils.database import get_semantic_response
from utils.memory import load_user_data
from utils.memory_commands import handle_memory_command
from utils.chat_history import load_chat_history, save_chat_history, clear_chat_history
from utils.database import get_semantic_response, add_response, get_all_knowledge, delete_response

app = Flask(__name__)

user_data = load_user_data()

chat_history = load_chat_history()

@app.route("/clear", methods=["POST"])
def clear():

    global chat_history

    chat_history = []

    clear_chat_history()

    return redirect("/")

@app.route("/admin", methods=["GET", "POST"])
def admin():

    if request.method == "POST":

        user_input = request.form["user_input"]

        bot_response = request.form["bot_response"]

        add_response(
            user_input,
            bot_response
        )
    
    knowledge = get_all_knowledge()

    return render_template(
        "admin.html",
        knowledge=knowledge
    )

@app.route("/delete/<int:response_id>", methods=["POST"])
def delete(response_id):

    delete_response(
        response_id
    )

    return redirect(
        "/admin"
    )

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

            response = get_semantic_response(user_input)

        chat_history.append(
            {
                "user": user_input,
                "bot": response
            }
        )

        save_chat_history(
            chat_history
        )


    return render_template(
        "index.html",
        chat_history=chat_history
    )


if __name__ == "__main__":
    app.run(debug=True)