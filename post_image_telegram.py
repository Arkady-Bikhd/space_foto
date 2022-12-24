import telegram
from dotenv import load_dotenv
from os import getenv
from pathlib import Path
from random import shuffle
from time import sleep
import argparse


def main():

    load_dotenv()
    post_delay_time = create_parser_delay_time()
    telegram_token = getenv('TELEGRAM_TOKEN')
    telegram_bot = telegram.Bot(telegram_token)
    post_image(telegram_bot, post_delay_time)
    




if __name__ == "__main__":

    main()