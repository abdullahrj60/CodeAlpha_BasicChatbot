# basic chatbot 

def start_chatbot():
    print("Welcome to PyBot")
    print("Type 'bye' to end the chat.")

    while True:
        message = input("You: ")

        if message.lower() == "bye":
            print("PyBot: Goodbye!")
            break


start_chatbot()
