def chatbot():
    print("Chatbot: Hello! Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello" or user_input == "hi":
            print("Chatbot: Hello! How can I help you?")
        
        elif "your name" in user_input:
            print("Chatbot: I am a rule-based chatbot.")
        
        elif "help" in user_input:
            print("Chatbot: I can answer simple questions like greetings or my details.")
        
        elif user_input == "exit":
            print("Chatbot: Goodbye! Have a nice day.")
            break
        
        else:
            print("Chatbot: Sorry, I didn't understand that.")

chatbot()