import tweepy
from chatterbot import ChatBot
chatbot = ChatBot("Twitter")

from chatterbot.trainers import ListTrainer

auth = tweepy.OAuthHandler('EVt3rEdGtFu8kFvFUCZ9Bkjme','M8kBJb4ZJ096MHkbiRXnms6Vl8oR4YprC1RYkzzAspgl39LTv5')
auth.set_access_token('2244086591-M9vfGQd0FwU0uCELIsYKaBtD7SlfQb61dhv1VBI','jm5I7rypJcZcfZ6kLAiA2xmoQVYOVY6kmWFmH8Q8itrJt')

api = tweepy.API(auth)

results = api.search(q='Copa do Mundo', count=5)



chatbot.set_trainer(ListTrainer)
chatbot.train(results)

while True:
    quest = input('Você: ')
    response = chatbot.get_response(quest)
    
    print('Bot: ', response)



