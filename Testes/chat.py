from chatterbot import ChatBot
chatbot = ChatBot("Ron Obvious")

from chatterbot.trainers import ListTrainer

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

chatbot.set_trainer(ListTrainer)
chatbot.train(conversation)

while True:
    quest = input('Você: ')
    response = chatbot.get_response(quest)
    
    print('Bot: ', response)
