import requests
from getimageslib import get_image
import argparse

def main():
    
    id = create_parser_link()
    try:    
        fetch_spacex_last_launch(id)
    except requests.exceptions.HTTPError:
        print('Неверная ссылка на запуск SpaceX')
    

def get_spacex_launch_links(id):

    url = f'https://api.spacexdata.com/v3/launches/{id}'
    response = requests.get(url)    
    if response.ok:
        return response.json()['links']['flickr_images']
    else:
        return list()


def get_spacex_launch_links_latest():

    url = 'https://api.spacexdata.com/v5/launches/latest'
    response = requests.get(url)
    response.raise_for_status()
    return response.json()['links']['flickr']['original']


def fetch_spacex_last_launch(id):
    
    default_id = 66
    images_links = get_spacex_launch_links(id)
    if not images_links:
        print(f'Фотографий запуска с номером {id} не найдено.')
        print('Осуществляется поиск фотогрфий последнего запуска.')
        images_links = get_spacex_launch_links_latest()        
        if not images_links:
            print('Фотографии последнего запуска не найдены.')
            print('Загружаются фотографии запуска по умолчанию.')
            images_links = get_spacex_launch_links(default_id)
    dir = 'images'
    for link_number, link in enumerate(images_links):
        image_file = f'spacex{link_number}.jpg'        
        get_image(link, image_file, dir)


def create_parser_link():

    parcer = argparse.ArgumentParser(
        description='Программа скачивает фотографии запусков SpaceX'
    )
    parcer.add_argument('id', help='Введите номер запуска')
    args = parcer.parse_args()

    return args.id


if __name__ == "__main__":
    
    main()