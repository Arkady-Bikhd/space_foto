from dotenv import load_dotenv
from os import environ

load_dotenv()
telegram_token = environ ['TELEGRAM_TOKEN']
tg_chat_id = environ['TG_CHAT_ID']
nasa_api_key = environ['NASA_API_KEY']