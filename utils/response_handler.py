def get_response(user_input, responses):
    if user_input in responses:
        return responses[user_input]

    return "I don't understand that yet."