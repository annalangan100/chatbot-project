print("Chatbot started!")

while True:
    user_input = input("You: ")

    if user_input.lower() == "bye":
        print("Bot: Goodbye!")
        break

    print("Bot: You said:", user_input)