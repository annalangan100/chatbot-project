print("Chatbot started!")
print("Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if user_input == "bye":
        print("Bot: Goodbye!")
        break

    elif user_input == "hello":
        print("Bot: Hello!")

    elif user_input == "how are you":
        print("Bot: I'm doing well, thanks for asking!")

    elif user_input == "what is your name":
        print("Bot: My name is ChatBot.")

    else:
        print("Bot: I don't understand that yet.")