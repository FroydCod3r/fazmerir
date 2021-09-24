import telebot
from datetime import datetime

APIKEY = "CALL ME IN PV BITCHS"

bot = telebot.TeleBot(APIKEY)

def diaDoSalario():
    now = datetime.now()
    dia_atual = now.day
    diaRestante = 30-dia_atual
    return diaRestante

def verify(mensagem):
    if mensagem.text == '/salario':
        return True
    else:
        return False
    # return True

#decorator
#@bot.message_handler(commands=["salario"])
@bot.message_handler(func=verify)
def responder(mensagem):
    bot.reply_to(mensagem, "Falta apenas {} dias para o FAZ ME RIR".format(diaDoSalario()))

bot.polling()
