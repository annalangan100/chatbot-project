import json


def load_user_data():
    with open("data/user_data.json", "r") as file:
        return json.load(file)


def save_user_data(data):
    with open("data/user_data.json", "w") as file:
        json.dump(data, file, indent=4)