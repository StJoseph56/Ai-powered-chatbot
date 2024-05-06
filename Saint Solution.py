import random

# Define responses
responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you?": ["I'm doing well, thank you!", "I'm great, thanks for asking!", "I'm good, how about you?"],
    "bye": ["Goodbye!", "See you later!", "Bye! Have a great day!"]
}

# Define a function to generate responses
def generate_response(user_input):
    if user_input.lower() in responses:
        return random.choice(responses[user_input.lower()])
    else:
        return "I'm sorry, I don't understand that."

# Start chatting
print("Chatbot: Hi there! How can I help you today?")

while True:
    # Get user input
    user_input = input("You: ")

    # Generate response
    response = generate_response(user_input)

    # Print response
    print("Chatbot:", response)
