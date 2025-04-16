from agent import chat_agent

print("🤖 Welcome to FitBuddy AI – your Fitness & Nutrition Assistant!")

while True:
    query = input("You: ")
    if query.lower() in ['exit', 'quit']:
        print("Goodbye! Stay fit 🏋️‍♂️🥗")
        break
    response = chat_agent.run(query)
    print("FitBuddy:", response)
