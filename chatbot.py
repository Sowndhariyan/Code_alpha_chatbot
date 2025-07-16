from utils import load_faqs, get_best_match

def run_chatbot():
    faqs = load_faqs()
    print("🤖 FAQ Chatbot (type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Bot: Goodbye!")
            break
        answer = get_best_match(user_input, faqs)
        print(f"Bot: {answer}")

if __name__ == "__main__":
    run_chatbot()