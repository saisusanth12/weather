from django.shortcuts import render
import json
import urllib.request


# Create your views here.
def index(request):
    
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=00fa11cadfb4a9da6370fcc3ec7301cf').read()
        
        json_data = json.loads(res)
        
        data = {
            "coordinate": 'coordinates : ' + str(json_data['coord']['lon']) + ' ' +
            str(json_data['coord']['lat']),
            "temp": str(json_data['main']['temp']) + ' K',
            "pressure": 'pressure : ' + str(json_data['main']['pressure']) + ' hPa',
            "humidity": 'humidity : ' + str(json_data['main']['humidity']) + ' %'
        }
    else:
        city= ''
        data = {}
    
    return render(request, 'index.html', {'city': city, 'data': data})
