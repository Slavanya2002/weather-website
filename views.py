from django.shortcuts import render # type: ignore

import requests # type: ignore
from django.shortcuts import render # type: ignore
from django.http import JsonResponse # type: ignore

API_KEY = '6e6720e3704948218c4210539242204'  # Weather API key

# Home page view
def index(request):
    return render(request, 'weather/index.html')

# Fetch weather data view
def get_weather(request):
    if request.method == 'GET':
        city = request.GET.get('city', '')
        if city:
            url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=yes"
            response = requests.get(url)
            data = response.json()
            
            # Extract required data
            weather_data = {
                'city_name': f"{data['location']['name']}, {data['location']['region']}",
                'country_name': data['location']['country'],
                'temp': data['current']['temp_c'],
                'local_time': data['location']['localtime']
            }
            return JsonResponse(weather_data)
        return JsonResponse({'error': 'City not provided'}, status=400)

