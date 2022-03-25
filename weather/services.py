import requests
import random

from bs4 import BeautifulSoup
import fake_useragent


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
