from django.shortcuts import render
import urllib.request
import json

# Create your views here.

def home(request):
    if request.method == "POST":
        city = request.POST.get('city')
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=imperial&appid=71ccab497e22863ced3e1777a8c92afe').read()  
        list_of_data = json.loads(source)

        data = {
            'temperature': str(list_of_data['main']['temp']) + 'k',
            'pressure': str(list_of_data['main']['pressure']),
            'humidity': str(list_of_data['main']['humidity']),
            'wind_speed': str(list_of_data['wind']['speed']),
            'condition': list_of_data['weather'][0]['description'],
        }
    else:
        city = ''
        data = {}
    
    return render(request, "index.html", {'data':data, 'city':city})
