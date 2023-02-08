# Define a list of keywords and corresponding responses
keywords = {
    'greet': 'Hello! How can I help you today?',
    'goodbye': 'Goodbye! Have a great day.',
    'thank you': 'You are welcome!',
    'default': 'Sorry, I do not understand what you are saying.'
}

# Define a function to get the response for a given input
def get_response(input_text):
    for key in keywords:
        if key in input_text.lower():
            return keywords[key]
    return keywords['default']

# Main loop to get user input and print the chatbot's response
while True:
    user_input = input('You: ')
    if user_input.lower() == 'exit':
        break
    print('Chatbot: ' + get_response(user_input))
