from chatterbot import ChatBot

bot = ChatBot('Test', trainer='chatterbot.trainers.ChatterBotCorpusTrainer')

bot.train('chatterbot.corpus.portuguese')

while True:
    resq = input('Você: ')

    resp = bot.get_response(resq)

    print('Bot: ', resp)
