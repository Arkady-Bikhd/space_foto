import telegram
from telegram.error import NetworkError
from pathlib import Path
from random import shuffle
from time import sleep
import argparse
from getimageslib import get_telegram_token, get_tg_chat_id


def main():

    post_delay_time = create_parser_delay_time()    
    telegram_bot = telegram.Bot(get_telegram_token())
    post_image(telegram_bot, post_delay_time)
    

def post_image(bot, post_delay_time=14400):       
    
    image_files = (path.resolve() for path in Path(Path.cwd()).glob("**/*") 
                    if path.suffix in {".png", ".gif", ".jpg", ".jpeg"})
    image_files = list(map(str, image_files))
    shuffle(image_files) 
    current_file = 0
    network_error = 0
    while True:        
        try:
            with open(image_files[current_file], 'rb') as file:
                bot.send_photo(chat_id=get_tg_chat_id(), photo=file)
            sleep(post_delay_time)
            current_file += 1
        except NetworkError:            
            if not network_error:
                sleep(1)
                network_error += 1                
            elif network_error < 3:
                sleep(10)
                network_error += 1                
            else:
                print('Ошибка подключения')                
                break                       


def create_parser_delay_time():

    parser = argparse.ArgumentParser(
        description='Программа загружает в телеграмм-канал фотографии'
    )
    parser.add_argument('-t', '--dtime', default=14400, help='Введите время задержки загрузки файла в секундах')
    args = parser.parse_args()

    return int(args.dtime)


if __name__ == "__main__":

    main()