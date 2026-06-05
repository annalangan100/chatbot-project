import random


def get_response(user_input, intents):
    for intent in intents.values():

        if user_input in intent["patterns"]:
            return random.choice(intent["responses"])

    return "I don't understand that yet."