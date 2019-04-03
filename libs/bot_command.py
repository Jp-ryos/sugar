# coding:UTF-8

from slackclient import SlackClient
from datetime import datetime
import re, os, json

NOW = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
API_TOKEN = "xoxb-594906983572-595279130004-yjnInLxKw2u3OYOC3Y8iB8Nl"
ERROR = "このコマンドは見つかりませんでしたorz\nERROR_CODE:109 unknown command : "
ECHO_CODE = 101
TISP_CODE = 102
POLL_CODE = 103
ERROR_CODE = 109
DEFAULT = "Hello World!"
TOKEN = '|'

def decode(message):
	return message.body['text'].replace(' ', TOKEN)

def bot_command(message):
	text = decode(message)

	if re.search(r'[|]', text) is not None:
		word, arg = text.split(TOKEN)
		if arg_command(message, word) == ECHO_CODE:
			message.reply(arg)
		else :
			message.reply(ERROR+ word)
	else :
		val = none_arg_command(message, text) 
		if val == TISP_CODE:
			message.reply(NOW)
		elif val == POLL_CODE:
			pass
		else :
			message.reply(ERROR + text)

def arg_command(message, word):

	if word in "$echo":
		return ECHO_CODE
	else :
		return ERROR_CODE

def none_arg_command(message, word):

	print("Hi!")
	if word in "$timestamp":
		NOW = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
		return TISP_CODE
	elif word in "$poll":
		sc = SlackClient(API_TOKEN)
		
		attachments = [{
			"fallback": "",
			"text": u"説明",
			"callback_id": "",
			"attachment_type": "default",
			"actions": [
				{
					"name": "done",
					"text": "a",
					"type": "button"
				}
			]
		}]
		sc.api_call(
			"chat.postMessage",
			channel="#rasp",
			text="Hello",
			attachments=json.dumps(attachments)
		)
		return POLL_CODE
	else :
		return ERROR_CODE


