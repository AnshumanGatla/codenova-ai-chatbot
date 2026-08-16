print("Welcome to AI Chatbot!")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    if user == "hello" or user == "hi" or user == "hey":
        print("Bot: Hello! How can I help you?")

    elif "your name" in user:
        print("Bot: I am CodeNova AI Chatbot.")

    elif "how are you" in user:
        print("Bot: I am doing great!")

    elif "help" in user:
        print("Bot: I can answer simple questions about myself.")

    elif "what can you do" in user:
        print("Bot: I can answer simple questions and have a basic conversation.")

    elif user == "bye":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand that.")