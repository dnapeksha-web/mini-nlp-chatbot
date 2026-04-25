import nltk
from nltk.tokenize import word_tokenize

def chatbot():
    print("🤖 AI Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        # Exit condition
        if "bye" in user_input or "exit" in user_input:
            print("🤖 AI Chatbot: Goodbye! 👋")
            break

        # Tokenize input
        words = word_tokenize(user_input)

        # Intent detection using keywords
        if any(word in words for word in ["hello", "hi", "hey"]):
            print("🤖 AI Chatbot: Hello there! 😊")

        elif any(word in words for word in ["how", "are", "you"]):
            print("🤖 AI Chatbot: I'm doing great! Thanks for asking 😄")

        elif any(word in words for word in ["name"]):
            print("🤖 AI Chatbot: I'm your mini AI chatbot 🤖")

        elif any(word in words for word in ["help"]):
            print("🤖 AI Chatbot: I can chat with you! Try greetings or questions.")

        elif any(word in words for word in ["weather"]):
            print("🤖 AI Chatbot: I can't check real weather yet, but it's always sunny in code ☀️")

        else:
            print("🤖 AI Chatbot: Hmm... I didn't understand that. Try something else!")

# Run chatbot
chatbot()