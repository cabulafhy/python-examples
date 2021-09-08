from chatterbot import ChatBot

bot = ChatBot("meuBot")

while True:
    user_input = input()
    bot_response = bot.get_response(user_input)
    print(bot_response)