import os
import random
import requests

import fake_useragent
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from pyowm import OWM


def get_city_temp(city: str):
    """Возвращает текущую температуру и как она ощущается"""
    load_dotenv()

    api_key = os.getenv('API_KEY')

    owm = OWM(api_key)
    mgr = owm.weather_manager()

    try:
        observation = mgr.weather_at_place(city)
    except Exception as e:
        print(e)
    else:
        w = observation.weather

        temp_json = w.temperature('celsius')

        temp = temp_json.get('temp')
        temp_feel = temp_json.get('feels_like')

    return (temp, temp_feel)


def get_city_image_url(city: str) -> str:

    user = fake_useragent.UserAgent().random
    header = {
        'user-agent': user,
    }
    URL = 'https://yandex.ru/images/search?text='

    response = requests.get(f'{URL}{city}', headers=header)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')

        div = soup.find(
            'div', {'class': 'page-layout__content-wrapper b-page__content'})

        images = div.find_all('img')

    return f'https:{random.choice(images)["src"]}'


if __name__ == '__main__':
    get_city_image_url('Екатеринбург')
