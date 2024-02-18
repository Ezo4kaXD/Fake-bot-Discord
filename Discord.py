import os
os.system("title ServerBot")
import requests
from colorama import Fore, Style, init

init(autoreset=True)

def print_red_bold(text: str) -> None:
    print(Fore.RED + Style.BRIGHT + text + Fore.RESET + Style.RESET_ALL)


def print_green(text):
    print(Fore.GREEN + text + Fore.RESET)

def send_discord_message(webhook_url, message):
    data = {
        "content": message
    }
    response = requests.post(webhook_url, json=data)

    if response.status_code != 204:
        print(response.text)

    else:
        print(response.text)

def main():
    webhook_url = "WEBHOOK"

    art = """
  ░██╗░░░░░░░██╗███████╗██████╗░██╗░░██╗░█████╗░░█████╗░██╗░░██╗░██████╗
  ░██║░░██╗░░██║██╔════╝██╔══██╗██║░░██║██╔══██╗██╔══██╗██║░██╔╝██╔════╝
  ░╚██╗████╗██╔╝█████╗░░██████╦╝███████║██║░░██║██║░░██║█████═╝░╚█████╗░
  ░░████╔═████║░██╔══╝░░██╔══██╗██╔══██║██║░░██║██║░░██║██╔═██╗░░╚═══██╗
  ░░╚██╔╝░╚██╔╝░███████╗██████╦╝██║░░██║╚█████╔╝╚█████╔╝██║░╚██╗██████╔╝
  ░░░╚═╝░░░╚═╝░░╚══════╝╚═════╝░╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░
    """

    print_red_bold(art)

    return webhook_url

if __name__ == "__main__":
    webhook_url = main()

    while True:
        message = input("  Message:")

        if message.lower() == 'Exit':
            break

        if message.lower() == 'cls':
            os.system("cls")

        send_discord_message(webhook_url, message)
