import json

from utils.intent_handler import get_response
from utils.logger import log_conversation

with open("intents.json", "r") as file:
    intents = json.load(file)

print("Chatbot started!")
print("Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    response = get_response(user_input, intents)

    print("Bot:", response)

    log_conversation(user_input, response)

    if user_input == "bye":
        break