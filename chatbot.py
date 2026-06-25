# basic chatbot
def get_response(message, user_name, last_topic):
    message = message.lower().strip()

    if message in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye! Have a nice day.", user_name, "exit"

    elif message in ["hello", "hi", "hey"]:
        return "Hello! How are you today?", user_name, "feeling"

    elif message in ["what is your name", "who are you"]:
        return (
            "My name is PyBot. I am a simple rule-based chatbot.",
            user_name,
            "general"
        )

    elif message in ["what can you do", "help"]:
        return (
            "I can talk about Python, AI, cybersecurity, CodeAlpha, "
            "date, time and jokes.",
            user_name,
            "general"
        )

    return (
        "Sorry, I do not understand that. "
        "Type 'help' to see what I can answer.",
        user_name,
        last_topic
    )


def start_chatbot():
    user_name = ""
    last_topic = "start"

    print("=" * 45)
    print("             WELCOME TO PYBOT")
    print("=" * 45)
    print("PyBot: Hello! Type 'help' to see what I can do.")
    print("PyBot: Type 'bye' to end the chat.\n")

    while True:
        user_message = input("You: ")

        response, user_name, last_topic = get_response(
            user_message,
            user_name,
            last_topic
        )

        print("PyBot:", response)

        if last_topic == "exit":
            break


start_chatbot()
