# Космический Телеграм

Автоматизирует сбор фотографий космоса и загружает их в Telegram-канал

## Общее описание

Проект состоит из четырёх отдельных сервисов. Три сервиса осуществляют автоматизированный сбор фотографий
космоса, четвёртый сервис публикует фотографии в Telegram-канал.

### Автоматизированный сбор фотографий

#### Сбор фотографий с запусков SpaceX

Для сбора фотографий с запусков SpaceX нужно указать номер запуска первым аргументом

```
python fetch_spacex_images.py 55
```

Если запуска SpaceX под таким номером не существует, будут загружены фотографии с последнего запуска

#### Сбор фотографий с сайта NASA

Для загрузки фотографий с сайта NASA вначале необходимо получить ключ API key для работы с API NASA: [Сайт NASA] (https://api.nasa.gov/)
API key выглядит как строка наподобие следующей: 'z0lvPbvoXdFG0ofUnWbmTHR0r1Xchf2dA7IYIBEi'
Полученный API key нужно присвоить переменной `API_KEY` в файле `.env`. Содержимое файла должно выглядеть примерно так
```.env
API_KEY=ВАШ_API-key
```

Сбор фотографий с сайта NASA выролняется следующим образом

```
python fetch_nasa_images.py
```

#### Сбор фотографий от EPIC

Для загрузки фотографий  от EPIC вначале необходимо получить ключ API key для работы с API EPIC: [Сайт NASA] (https://api.nasa.gov/)
API key выглядит как строка наподобие следующей: 'z0lvPbvoXdFG0ofUnWbmTHR0r1Xchf2dA7IYIBEi'
Полученный API key нужно присвоить переменной `API_KEY` в файле `.env`. Содержимое файла должно выглядеть примерно так
```.env
API_KEY=ВАШ_API-key
```

Сбор фотографий от EPIC выролняется следующим образом

```
python fetch_epic_image.py
```

### Публикация фотографий в Telegram

Для публикации фотографий в Telegram необходимо вначале создфть бота в Telegram и получить его токен.
На странице [Bots: An introduction for developers] (https://core.telegram.org/bots) описан процесс
создания бота. 
Полученный токен нужно присвоить переменной `TOKEN` в файле `.env`. Содержимое файла должно выглядеть примерно так
```.env
TOKEN=ВАШ_ТОКЕН
```
Затем нужно создать Telegram-канал и установить созданного бота администратором канала. Процесс создания канала
представлен на странице [Channels FAQ] (https://telegram.org/faq_channels#q-what-39s-a-channel).
Для публикации фотографий нужно указать первым парметром время в секундах 

```python
python post_image_telegram.py -t 600 
```

Если время не указано, по умолчанию фотографии публикуются каждые 4 часа

#### Установить зависимости

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
Рекомендуется использовать [virtualenv/env](https://docs.python.org/3/library/venv.html) для изоляции проекта

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).



