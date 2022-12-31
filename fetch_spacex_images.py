import requests
from getimageslib import get_image
import argparse

def main():
    
    spacex_id = create_parser_link()
    try:    
        fetch_spacex_last_launch(spacex_id)
    except requests.exceptions.HTTPError:
        print('Неверная ссылка на запуск SpaceX')
    

def get_spacex_launch_links(spacex_id=0, latest=False):

    if latest:
        url = 'https://api.spacexdata.com/v5/launches/latest'
        response = requests.get(url)
        response.raise_for_status()
        return response.json()['links']['flickr']['original']
    else: 
        url = f'https://api.spacexdata.com/v3/launches/{spacex_id}'
        response = requests.get(url)    
        if response.ok:
            return response.json()['links']['flickr_images']
        


def fetch_spacex_last_launch(spacex_id):
    
    default_id = 66
    images_links = get_spacex_launch_links(spacex_id)
    if not images_links:
        print(f'Фотографий запуска с номером {spacex_id} не найдено.')
        print('Осуществляется поиск фотогрфий последнего запуска.')
        images_links = get_spacex_launch_links(latest=True)        
        if not images_links:
            print('Фотографии последнего запуска не найдены.')
            print('Загружаются фотографии запуска по умолчанию.')
            images_links = get_spacex_launch_links(default_id)
    image_dir = 'images'
    for link_number, link in enumerate(images_links):
        image_file = f'spacex{link_number}.jpg'        
        get_image(link, image_file, image_dir)


def create_parser_link():

    parser = argparse.ArgumentParser(
        description='Программа скачивает фотографии запусков SpaceX'
    )
    parser.add_argument('-n', '--number', default='66', help='Введите номер запуска')
    args = parser.parse_args()

    return args.number


if __name__ == "__main__":
    
    main()