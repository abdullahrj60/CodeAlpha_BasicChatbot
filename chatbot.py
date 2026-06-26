# basic chatbot
from datetime import datetime
import random

def get_response(message, user_name, last_topic):
    message = message.lower().strip()

    if message in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye! Have a nice day.", user_name, "exit"

    elif message in ["hello", "hi", "hey"]:
        return "Hello! How are you today?", user_name, "feeling"
    if last_topic == "feeling":
        if message in ["good", "great", "fine", "i am good", "i am fine"]:
            return "That is great! What is your name?", user_name, "name"

        elif message in ["bad", "sad", "not good", "i am sad"]:
            return (
                "I am sorry to hear that. Would you like to hear a joke?",
                user_name,
                "joke_offer"
            )
    if last_topic == "name":
        if message.startswith("my name is "):
            user_name = message.replace("my name is ", "").title()

            return (
                f"Nice to meet you, {user_name}! What would you like to ask?",
                user_name,
                "general"
            )

        return (
            "Please write your name like this: my name is Abdullah",
            user_name,
            "name"
        )
    if last_topic == "joke_offer":
        if message in ["yes", "yeah", "sure", "ok", "okay"]:
            jokes = [
                "Why do programmers prefer dark mode? Because light attracts bugs!",
                "Why was the computer cold? Because it left its Windows open!"
            ]

            return (
                random.choice(jokes) + " Do you feel better now?",
                user_name,
                "after_joke"
            )

        elif message in ["no", "nope"]:
            return (
                "No problem. You can ask me something else.",
                user_name,
                "general"
            )

    if last_topic == "after_joke":
        if message in ["yes", "better", "a little"]:
            return (
                "I am glad to hear that! What would you like to ask next?",
                user_name,
                "general"
            )

        elif message in ["no", "not really"]:
            return (
                "I understand. I hope you feel better soon.",
                user_name,
                "general"
            )
    if last_topic == "python_followup":
        if message in ["yes", "yeah", "sure", "ok", "okay"]:
            return (
                "Python is used in AI, web development, automation, "
                "data science and cybersecurity.",
                user_name,
                "general"
            )

        elif message in ["no", "nope"]:
            return "No problem. Ask me something else.", user_name, "general"

    if last_topic == "ai_followup":
        if message in ["yes", "yeah", "sure", "ok", "okay"]:
            return (
                "Examples of AI include chatbots, recommendation systems "
                "and image recognition.",
                user_name,
                "general"
            )

        elif message in ["no", "nope"]:
            return "No problem. Ask me something else.", user_name, "general"
    if message.startswith("my name is "):
        user_name = message.replace("my name is ", "").title()

        return (
            f"Nice to meet you, {user_name}! How can I help you?",
            user_name,
            "general"
        )

    elif message in ["what is my name", "do you know my name"]:
        if user_name:
            return f"Your name is {user_name}.", user_name, "general"

        return (
            "You have not told me your name yet. What is your name?",
            user_name,
            "name"
        )
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
    
    elif message == "what is python":
        return (
            "Python is a simple and popular programming language. "
            "Would you like to know where it is used?",
            user_name,
            "python_followup"
        )

    elif message in ["what is ai", "what is artificial intelligence"]:
        return (
            "AI allows computers to perform tasks that usually require "
            "human intelligence. Would you like an example?",
            user_name,
            "ai_followup"
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
