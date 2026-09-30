# 🤖 CodeAlpha Basic Chatbot
# Developed as part of CodeAlpha Python Programming Internship


def get_response(user_input):
    user_input = user_input.strip().lower()

    if user_input in ["hello", "hi", "hey"]:
        return "Hello! 👋 How can I help you?"

    elif "how are you" in user_input:
        return "I'm doing great! Thanks for asking. 😊"

    elif "your name" in user_input:
        return "I'm CodeAlpha Bot, your simple Python chatbot. 🤖"

    elif "what can you do" in user_input:
        return "I can respond to a few predefined questions and have a simple conversation with you."

    elif "who created you" in user_input or "who made you" in user_input:
        return "I was created as a Python project for the CodeAlpha Internship."

    elif "python" in user_input:
        return "Python is a beginner-friendly programming language used for many different applications."

    elif "thank" in user_input:
        return "You're welcome! 😊"

    elif user_input in ["bye", "exit", "quit"]:
        return "Goodbye! 👋 Have a great day!"

    else:
        return "Sorry, I don't understand that yet. Try asking me something else."


def chatbot():
    print("=" * 45)
    print("        🤖 CODEALPHA BASIC CHATBOT")
    print("=" * 45)
    print("Type 'bye' to exit the chatbot.\n")

    while True:
        user_input = input("You: ")

        response = get_response(user_input)
        print("Bot:", response)

        if user_input.strip().lower() in ["bye", "exit", "quit"]:
            break


# Start the chatbot
chatbot()