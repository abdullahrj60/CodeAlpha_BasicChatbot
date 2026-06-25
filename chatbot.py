# basic chatbot
def start_chatbot():
    print("=" * 45)
    print("             WELCOME TO PYBOT")
    print("=" * 45)
    print("PyBot: Hello!")
    print("PyBot: Type 'bye' to end the chat.\n")

    while True:
        user_message = input("You: ")
        message = user_message.lower().strip()

        if message in ["bye", "goodbye", "exit", "quit"]:
            print("PyBot: Goodbye! Have a nice day.")
            break

        else:
            print("PyBot: Sorry, I do not understand that.")


start_chatbot()
