import telegram
from telegram.error import NetworkError
from pathlib import Path
from random import shuffle
from time import sleep
import argparse
from getimageslib import get_telegram_token, get_tg_chat_id
from retry import retry


def main():

    post_delay_time = create_parser_delay_time()    
    telegram_bot = telegram.Bot(get_telegram_token())
    post_image(telegram_bot, post_delay_time)
    

def post_image(bot, post_delay_time=14400):       
    
    @retry(NetworkError, tries=3, delay=1, backoff=5)
    def post_image_file(image_files, current_file):       
        with open(image_files[current_file], 'rb') as file:
            bot.send_photo(chat_id=get_tg_chat_id(), photo=file)
                
        

    image_files = (path.resolve() for path in Path(Path.cwd()).glob("**/*") 
                    if path.suffix in {".png", ".gif", ".jpg", ".jpeg"})
    image_files = list(map(str, image_files))
    shuffle(image_files) 
    current_file = 0
    
    while True:        
        try:
            post_image_file(image_files, current_file)
        except NetworkError:
            print('Ошибка подключения')
            break    
        sleep(post_delay_time)
        current_file += 1
                         


def create_parser_delay_time():

    parser = argparse.ArgumentParser(
        description='Программа загружает в телеграмм-канал фотографии'
    )
    parser.add_argument('-t', '--dtime', default=14400, help='Введите время задержки загрузки файла в секундах')
    args = parser.parse_args()

    return int(args.dtime)


if __name__ == "__main__":

    main()