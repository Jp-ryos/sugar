from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply

#from libs import my_functions

@respond_to(r'.+')
def mention_func(message):
    print("Hello")
    text = message.body['text']
    msg = "オウム返しします" + text
    message.reply(msg)


@listen_to('')
def listen_func(message):
    message.send('listen')
    message.reply('you?')
