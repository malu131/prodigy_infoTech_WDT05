import requests
from django.shortcuts import render

def weather_view(request):
    city = request.GET.get('city')  # Get city from query parameters
    weather = None
    error_message = None

    if city:  # Only fetch weather if a city is provided
        api_key = '124d266c677b60076806b7194a89d66b'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            weather = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
            }
        else:
            error_message = data.get('message', 'No result found')

    return render(request, 'weather.html', {'weather': weather, 'error_message': error_message})
