from flask import Flask, render_template, request, redirect, send_file

from utils.database import get_semantic_response
from utils.memory import load_user_data
from utils.memory_commands import handle_memory_command
from utils.chat_history import load_chat_history, save_chat_history, clear_chat_history
from utils.database import (
    get_semantic_response, 
    add_response, get_all_knowledge, 
    delete_response, 
    update_response, 
    get_response_by_id, 
    search_knowledge, 
    import_csv, 
    export_csv, 
    get_knowledge_count, 
    get_database_size
)

app = Flask(__name__)

user_data = load_user_data()

chat_history = load_chat_history()

@app.route("/clear", methods=["POST"])
def clear():

    global chat_history

    chat_history = []

    clear_chat_history()

    return redirect("/")

@app.route("/import", methods=["GET", "POST"])
def import_data():

    if request.method == "POST":

        file = request.files["file"]

        file_path = (
            f"uploads/{file.filename}"
        )

        file.save(
            file_path
        )

        import_csv(
            file_path
        )

        return redirect(
            "/admin"
        )

    return render_template(
        "import.html"
    )

@app.route("/export")
def export_data():

    file_path = (
        "exports/knowledge_export.csv"
    )

    export_csv(
        file_path
    )

    return send_file(
        file_path,
        as_attachment=True
    )

@app.route("/admin", methods=["GET", "POST"])
def admin():

    if request.method == "POST":

        user_input = request.form["user_input"]

        bot_response = request.form["bot_response"]

        add_response(
            user_input,
            bot_response
        )
    
    search_term = request.args.get(
        "search",
        ""
    )

    if search_term:

        knowledge = search_knowledge(
            search_term
        )

    else:

        knowledge = get_all_knowledge()

    knowledge_count = (
        get_knowledge_count()
    )

    database_size = (
        get_database_size()
    )

    return render_template(
        "admin.html",
        knowledge=knowledge,
        knowledge_count=knowledge_count,
        database_size=database_size,
        
    )

@app.route("/delete/<int:response_id>", methods=["POST"])
def delete(response_id):

    delete_response(
        response_id
    )

    return redirect(
        "/admin"
    )

@app.route(
    "/edit/<int:response_id>",
    methods=["GET", "POST"]
)
def edit(response_id):

    if request.method == "POST":

        user_input = request.form[
            "user_input"
        ]

        bot_response = request.form[
            "bot_response"
        ]

        update_response(
            response_id,
            user_input,
            bot_response
        )

        return redirect(
            "/admin"
        )

    response = get_response_by_id(
        response_id
    )

    return render_template(
        "edit.html",
        response=response
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