from responses import responses

print("Chatbot started!")
print("Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if user_input in responses:
        print("Bot:", responses[user_input])

        if user_input == "bye":
            break

    else:
        print("Bot: I don't understand that yet.")