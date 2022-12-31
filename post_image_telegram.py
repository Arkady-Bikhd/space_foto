import telegram
from telegram.error import NetworkError
from pathlib import Path
from random import shuffle
from time import sleep
import argparse
from dotenv import load_dotenv
from os import environ
from retry import retry


def main():

    load_dotenv()
    post_delay_time = create_parser_delay_time()
    telegram_token = environ['TELEGRAM_TOKEN'] 
    tg_chat_id = environ['TG_CHAT_ID']   
    telegram_bot = telegram.Bot(telegram_token)
    post_image(telegram_bot, tg_chat_id, post_delay_time)
    
@retry(NetworkError, tries=3, delay=1, backoff=5)
def post_image_file(image_files, current_file, tg_chat_id, bot):           
    with open(image_files[current_file], 'rb') as file:
            bot.send_photo(chat_id=tg_chat_id, photo=file)


def post_image(bot, tg_chat_id, post_delay_time=14400):      
    
    
    image_files = (path.resolve() for path in Path.cwd().glob("**/*") 
                    if path.suffix in {".png", ".gif", ".jpg", ".jpeg"})
    image_files = list(map(str, image_files))    
    shuffle(image_files) 
    current_file = 0
    
    while True:        
        try:
            post_image_file(image_files, current_file, tg_chat_id, bot)
        except NetworkError:
            print('Ошибка подключения')                
        sleep(post_delay_time)
        current_file += 1
                         


def create_parser_delay_time():

    parser = argparse.ArgumentParser(
        description='Программа загружает в телеграмм-канал фотографии'
    )
    parser.add_argument('-t', '--dtime', default=14400, type=int, 
        help='Введите время задержки загрузки файла в секундах')
    args = parser.parse_args()

    return args.dtime


if __name__ == "__main__":

    main()