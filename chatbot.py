import json

from utils.intent_handler import get_response
from utils.logger import log_conversation
from utils.memory import load_user_data, save_user_data
from utils.memory_commands import (
    handle_memory_command
)

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

    memory_response = handle_memory_command(
        user_input,
        user_data
    )

    if memory_response:

        print("Bot:", memory_response)

        log_conversation(
            user_input,
            memory_response
        )

        continue

    response = get_response(user_input, intents)

    print("Bot:", response)

    log_conversation(user_input, response)

    if user_input == "bye":
        break