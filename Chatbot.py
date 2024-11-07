import random

def get_response(user_input):
    responses = {
        "hello": ["Hi!", "Hello!", "Hey there!", "Hi, how can I help you?"],
        "how are you": ["I'm good, thank you!", "I'm doing great!", "I'm feeling fine!"],
        "bye": ["Goodbye!", "See you later!", "Bye, have a great day!"]
    }
    
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    
    return "I'm sorry, I don't understand."

def main():
    print("Chatbot: Hello! How can I help you today?")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye!")
            break
        else:
            print(f"Chatbot: {get_response(user_input)}")

if __name__ == "__main__":
    main()
