import json

from utils.intent_handler import get_response
from utils.logger import log_conversation
from utils.memory import load_user_data, save_user_data

with open("intents.json", "r") as file:
    intents = json.load(file)

user_data = load_user_data()

print("Chatbot started!")
print("Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if user_input == "help":

        response = """
        Available commands:

            - hello
            - hi
            - hey
            - good morning
            - good evening

            - what is your name
            - who made you

            - what is python

            - my name is <your name>
            - what is my name

            - my favorite color is <color>
            - what is my favorite color

            - my favorite language is <language>
            - what is my favorite language

            - help
            - bye
            """

        print("Bot:", response)

        log_conversation(user_input, response)

        continue

    if user_input.startswith("my name is "):

        name = user_input.replace("my name is ", "")

        user_data["name"] = name

        save_user_data(user_data)

        response = f"Nice to meet you {name}"

        print("Bot:", response)

        log_conversation(user_input, response)

        continue

    if user_input == "what is my name":

        if "name" in user_data:
            response = f"Your name is {user_data['name']}"
        else:
            response = "I don't know your name yet."

        print("Bot:", response)

        log_conversation(user_input, response)

        continue
    
    if user_input.startswith("my favorite color is "):

        color = user_input.replace(
            "my favorite color is ",
            ""
        )

        user_data["favorite_color"] = color

        save_user_data(user_data)

        response = f"I'll remember that your favorite color is {color}"

        print("Bot:", response)

        log_conversation(user_input, response)

        continue

    if user_input == "what is my favorite color":

        if "favorite_color" in user_data:
            response = (
                f"Your favorite color is "
                f"{user_data['favorite_color']}"
            )
        else:
            response = (
                "I don't know your favorite color yet."
            )

        print("Bot:", response)

        log_conversation(user_input, response)

        continue

    if user_input.startswith("my favorite language is "):

        language = user_input.replace(
            "my favorite language is ",
            ""
        )

        user_data["favorite_language"] = language

        save_user_data(user_data)

        response = (
            f"I'll remember that your favorite language is "
            f"{language}"
        )

        print("Bot:", response)

        log_conversation(user_input, response)

        continue

    if user_input == "what is my favorite language":

        if "favorite_language" in user_data:

            response = (
                f"Your favorite language is "
                f"{user_data['favorite_language']}"
            )

        else:

            response = (
                "I don't know your favorite language yet."
            )

        print("Bot:", response)

        log_conversation(user_input, response)

        continue


    response = get_response(user_input, intents)

    print("Bot:", response)

    log_conversation(user_input, response)

    if user_input == "bye":
        break