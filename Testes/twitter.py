from chatterbot import ChatBot
import logging

TWITTER = {
    "CONSUMER_KEY": "EVt3rEdGtFu8kFvFUCZ9Bkjme",
    "CONSUMER_SECRET": "M8kBJb4ZJ096MHkbiRXnms6Vl8oR4YprC1RYkzzAspgl39LTv5",
    "ACCESS_TOKEN": "2244086591-M9vfGQd0FwU0uCELIsYKaBtD7SlfQb61dhv1VBI",
    "ACCESS_TOKEN_SECRET": "jm5I7rypJcZcfZ6kLAiA2xmoQVYOVY6kmWFmH8Q8itrJt"
}

logging.basicConfig(level=logging.INFO)

chatbot = ChatBot(
    "TwitterBot",
    logic_adapters=[
        "chatterbot.logic.BestMatch"
    ],
    input_adapter="chatterbot.input.TerminalAdapter",
    output_adapter="chatterbot.output.TerminalAdapter",
    database="./twitter-database.db",
    twitter_consumer_key=TWITTER["CONSUMER_KEY"],
    twitter_consumer_secret=TWITTER["CONSUMER_SECRET"],
    twitter_access_token_key=TWITTER["ACCESS_TOKEN"],
    twitter_access_token_secret=TWITTER["ACCESS_TOKEN_SECRET"],
    trainer="chatterbot.trainers.TwitterTrainer"
)

chatbot.train()

chatbot.logger.info('Trained database generated successfully!')

while True:
    resq = input('Você: ')

    resp = chatbot.get_response(resq)

    print('Bot: ', resp)
