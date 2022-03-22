import os

from django.shortcuts import render

from dotenv import load_dotenv
from pyowm import OWM


def get_weather(request):
    context = {}

    if request.GET.get('city'):
        city = request.GET.get('city')

        load_dotenv()

        api_key = os.getenv('API_KEY')

        owm = OWM(api_key)
        mgr = owm.weather_manager()

        try:
            observation = mgr.weather_at_place(city)
        except:
            pass
        else:
            w = observation.weather

            temp_json = w.temperature('celsius')

            temp = temp_json.get('temp')
            temp_feel = temp_json.get('feels_like')

            context['temp'] = temp
            context['temp_feel'] = temp_feel

    return render(request, 'weather/weather_index.html', context)
