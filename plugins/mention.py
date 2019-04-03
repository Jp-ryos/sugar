# coding:UTF-8

from slackbot.bot import respond_to
from libs import bot_command as bot

@respond_to(r'^[$].*')
def to_bot_mention(message):
	bot.bot_command(message)


