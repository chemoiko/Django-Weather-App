from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    appid = 'a4a81793e18ea2d61e1bc98d0064d226'
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q': 'kampala', 'appid':appid, 'units': 'metric'}

    
    
    
    
    r = requests.get(url= URL, params=PARAMS)
    res = r.json()
    description = res['weather'][0]['description']
    icon = res['weather'][0]['description']
    temp = res['main'][0]['temp']



    return render(request, 'weatherapp/index.html', {'description': description}, {'icon': icon}, {'temp': temp})