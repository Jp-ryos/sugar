from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply
from datetime import datetime
import re

NOW = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
TOKEN = '|'

def decode(message):
    return message.body['text']

@respond_to(r'^[$].*')
def bot_mention(message):
    text = decode(message).replace(' ', TOKEN)
    print(text)

    if re.search(r'[|]', text) is not None:
        print("arg command")
        arg_command(message, text)
    else:
        none_arg_command(message, text)


def arg_command(message, text):
    word, arg = text.split(TOKEN)

    if word in "$echo":
        message.reply(arg)

    else :
        message.reply("unknown word :" + word)

def none_arg_command(message, text):

    if text in "$timestamp":
        print("Hello")
        NOW = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        message.reply("現在の日時は\n" + NOW)

    else :
        message.reply("unknown word :" + word)

