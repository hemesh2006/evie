from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot instance
chatbot = ChatBot(
    'SimpleBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
)

# Train the chatbot with the ChatterBot Corpus data
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on the English language corpus
trainer.train("chatterbot.corpus.english")

# Start the conversation with the chatbot
print("Hello! I am SimpleBot. Type 'exit' to stop the conversation.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    
    # Get a response from the chatbot
    response = chatbot.get_response(user_input)
    print("SimpleBot:", response)
