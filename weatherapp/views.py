from django.shortcuts import render
import requests
import datetime

# Create your views here.
def index(request):
    
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Kampala'
    
    
    appid = 'a4a81793e18ea2d61e1bc98d0064d226'
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q': city, 'appid':appid, 'units': 'metric'}

    
    
    
    
    r = requests.get(url= URL, params=PARAMS)
    res = r.json()
    description = res['weather'][0]['description']
    icon = res['weather'][0]['icon']
    temp = res['main']['temp']

    day = datetime.date.today()



    return render(request, 'weatherapp/index.html', {'description': description, 'icon': icon, 'temp': temp, 'day': day, 'city': city})