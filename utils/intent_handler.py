import random

def get_response(user_input, intents):

    user_input = user_input.lower()

    for intent in intents.values():

        for pattern in intent["patterns"]:

            if pattern.lower() in user_input:
                return random.choice(intent["responses"])

    return "I don't understand that yet."