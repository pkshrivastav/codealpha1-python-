import random

def chatbot_response(user_input):
    responses = {
        "hello": ["Hi there!", "Hello!", "Hey!"],
        "how are you": ["I'm doing great, thank you!", "I'm just a bot, but I'm functioning properly!", "All systems go!"],
        "what are you doing":["no nothing " , "eatting "],
        "are you ok":["yes i am ok ", "no i am not ok "],
        "are you mad":["no i am not a mad ", "what ", "where is your mind ","yes i am mad "],
        "what are you eatting":["roti sabaji ", "dosa sabhar ","chaval dal"],
        "who are you":[" radha ","sita","pk" ,"nahi bataungi "],
        "bye": ["Goodbye!", "See you later!", "Take care!"],
        "default": ["I'm not sure how to respond to that.", "Can you rephrase that?", "I don't understand."]
       
    }
    
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return random.choice(responses["default"])

def main():
    print("Chatbot: Hello! How can I help you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye!")
            break
        response = chatbot_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()