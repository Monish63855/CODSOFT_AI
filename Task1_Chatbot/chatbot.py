import random

def chatbot_response(user_input):
    message = user_input.lower().strip()

    if any(word in message for word in ["hello", "hi", "hey"]):
        return random.choice([
            "Hello! How can I help you?",
            "Hi there! Nice to meet you.",
            "Hey! What can I do for you?"
        ])

    elif "your name" in message or "name" in message:
        return "I am a simple Python chatbot!"

    elif "how are you" in message:
        return "I'm doing great! Thanks for asking."

    elif "help" in message:
        return "I can chat with you. Try saying hello, asking my name, or asking how I am."

    elif "bye" in message or "exit" in message:
        return "Goodbye! Have a nice day!"

    elif "thank" in message:
        return "You're welcome!"

    else:
        return "Sorry, I don't understand that. Can you ask something else?"


print("Chatbot: Hello! I am your chatbot.")
print("Chatbot: Type 'bye' to end the conversation.")

while True:
    user_input = input("You: ")
    
    response = chatbot_response(user_input)
    print("Chatbot:", response)

    if "bye" in user_input.lower() or "exit" in user_input.lower():
        break
