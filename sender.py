from discord_webhook import DiscordEmbed, DiscordWebhook
from termcolor import colored
import os

os.system("cls")

print(colored("""
░██████╗███████╗███╗░░██╗██████╗░███████╗██████╗░
██╔════╝██╔════╝████╗░██║██╔══██╗██╔════╝██╔══██╗
╚█████╗░█████╗░░██╔██╗██║██║░░██║█████╗░░██████╔╝
░╚═══██╗██╔══╝░░██║╚████║██║░░██║██╔══╝░░██╔══██╗
██████╔╝███████╗██║░╚███║██████╔╝███████╗██║░░██║
╚═════╝░╚══════╝╚═╝░░╚══╝╚═════╝░╚══════╝╚═╝░░╚═╝
""", "green"))



web = input("webhook url: ") 
title = input("title of embed to send: ")
desc = input("description of embed to send: ")

webhook = DiscordWebhook(url=web)
embed1 = DiscordEmbed(title=title, description=desc)
webhook.add_embed(embed1)

response = webhook.execute()

print(colored("sended", "blue"))

input(colored("click enter to end", "yellow"))