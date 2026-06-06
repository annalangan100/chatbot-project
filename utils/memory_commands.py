from utils.memory import save_user_data


def handle_memory_command(user_input, user_data):

    if user_input.startswith("my name is "):

        name = user_input.replace("my name is ", "")

        user_data["name"] = name

        save_user_data(user_data)

        return f"Nice to meet you {name}"


    if user_input == "what is my name":

        if "name" in user_data:
            return f"Your name is {user_data['name']}"

        return "I don't know your name yet."


    if user_input.startswith("my favorite color is "):

        color = user_input.replace(
            "my favorite color is ",
            ""
        )

        user_data["favorite_color"] = color

        save_user_data(user_data)

        return (
            f"I'll remember that your favorite color is "
            f"{color}"
        )


    if user_input == "what is my favorite color":

        if "favorite_color" in user_data:
            return (
                f"Your favorite color is "
                f"{user_data['favorite_color']}"
            )

        return (
            "I don't know your favorite color yet."
        )


    if user_input.startswith(
        "my favorite language is "
    ):

        language = user_input.replace(
            "my favorite language is ",
            ""
        )

        user_data["favorite_language"] = language

        save_user_data(user_data)

        return (
            f"I'll remember that your favorite language is "
            f"{language}"
        )


    if user_input == "what is my favorite language":

        if "favorite_language" in user_data:

            return (
                f"Your favorite language is "
                f"{user_data['favorite_language']}"
            )

        return (
            "I don't know your favorite language yet."
        )

    return None