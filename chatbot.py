import json

from utils.response_handler import get_response

with open("responses.json", "r") as file:
    responses = json.load(file)

print("Chatbot started!")
print("Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    response = get_response(user_input, responses)

    print("Bot:", response)

    if user_input == "bye":
        break