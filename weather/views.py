
from django.shortcuts import render
from weather.services import get_city_image_url, get_city_temp


def get_weather(request):
    context = {}

    if request.GET.get('city'):
        city = request.GET.get('city')

        try:
            temp, temp_feel = get_city_temp(city)

        except Exception as e:
            print(e)

        else:
            try:
                image_url = get_city_image_url(city)
            except Exception as e:
                print(e)
            else:
                context['image_url'] = image_url
            print(image_url)
            context['temp'] = round(temp)
            context['temp_feel'] = round(temp_feel)
            context['city'] = city

    return render(request, 'weather/weather_index.html', context)
