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
    

def post_image(bot, post_delay_time=14400):       
    
    dir_images = getenv('DIR_IMAGES')
    image_files = (path.resolve() for path in Path(dir_images).glob("**/*") 
                    if path.suffix in {".png", ".gif", ".jpg", ".jpeg"})
    image_files = list(map(str, image_files))
    shuffle(image_files)

    chat_id = getenv('CHAT_ID')
    current_file = 0
    while True:
        bot.send_photo(chat_id=chat_id, photo=open(image_files[current_file], 'rb'))
        sleep(post_delay_time)
        current_file += 1


def create_parser_delay_time():

    parcer = argparse.ArgumentParser(
        description='Программа загружает в телеграмм-канал фотографии'
    )
    parcer.add_argument('dtime', help='Введите время задержки загрузки файла в секундах')
    args = parcer.parse_args()

    return int(args.dtime)


if __name__ == "__main__":

    main()