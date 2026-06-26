# CodeAlpha Basic Chatbot

A beginner-friendly rule-based chatbot created in Python as part of the CodeAlpha Python Programming Internship.

## Project Overview

PyBot communicates with users through predefined responses. It can answer basic questions, remember the user's name during the conversation, and connect some replies with the previous message using the `last_topic` variable.

This is a console-based chatbot and does not use artificial intelligence, an API, or an internet connection.

## Features

* Responds to greetings such as `hello`, `hi`, and `hey`
* Asks the user how they are feeling
* Responds differently to positive and negative feelings
* Remembers the user's name during the current conversation
* Answers when the user asks for their stored name
* Connects `yes` and `no` responses with the previous question
* Explains basic information about:

  * Python
  * Artificial Intelligence
  * Cybersecurity
  * CodeAlpha
* Displays the current date
* Displays the current time
* Tells simple programming jokes
* Handles empty and unknown messages
* Ends the conversation using `bye`, `goodbye`, `exit`, or `quit`
* Handles `Control + C` safely

## Concepts Used

* Functions
* `if`, `elif`, and `else` conditions
* `while` loop
* Lists
* Variables
* User input and output
* String methods
* Multiple return values
* `datetime` module
* `random` module
* `try-except` exception handling

## Project Files

```text
CodeAlpha_BasicChatbot
├── chatbot.py
└── README.md
```

## Requirements

* Python 3
* VS Code or another Python code editor

No external libraries are required.

## How to Run

1. Download or clone this repository.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run the following command:

```bash
python3 chatbot.py
```

For some Windows systems, use:

```bash
python chatbot.py
```

## Supported Messages

You can try messages such as:

```text
hello
i am good
i am sad
my name is Abdullah
what is my name
what is your name
what can you do
what is python
what is ai
what is cybersecurity
what is codealpha
what time is it
what is the date
tell me a joke
thank you
bye
```

## Sample Conversation

```text
PyBot: Hello! Type 'help' to see what I can do.
PyBot: Type 'bye' to end the chat.

You: hello
PyBot: Hello! How are you today?

You: i am good
PyBot: That is great! What is your name?

You: my name is Abdullah
PyBot: Nice to meet you, Abdullah! What would you like to ask?

You: what is my name
PyBot: Your name is Abdullah.

You: what is python
PyBot: Python is a simple and popular programming language. Would you like to know where it is used?

You: yes
PyBot: Python is used in AI, web development, automation, data science and cybersecurity.

You: bye
PyBot: Goodbye, Abdullah! Have a nice day.
```

## How the Chatbot Works

The `get_response()` function checks the user's message and returns:

1. The chatbot's response
2. The stored user name
3. The current conversation topic

The `last_topic` variable helps the chatbot understand simple follow-up messages such as `yes` and `no`.

The `start_chatbot()` function uses a `while` loop to keep the conversation running until the user enters an exit command.

## Limitations

* The chatbot uses predefined rules and responses.
* It cannot understand every possible question.
* The user's name is remembered only while the program is running.
* It does not use live internet information.
* It is not an AI-powered chatbot.

## Internship Task

This project was completed as **Task 4: Basic Chatbot** for the CodeAlpha Python Programming Internship.

## Author

Muhammad Abdullah 
