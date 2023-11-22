from django.shortcuts import render
import json
import urllib.request

# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        api_key = 'f6ad6dee5af5e362dc626f7ccfcedef3'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
        res = urllib.request.urlopen(url).read()
        json_data = json.loads(res)
        data = {
            'country_code': str(json_data['sys']['country']),
            'coordinate': str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
            'temp': str(json_data['main']['temp'])+'k',
            'pressure': str(json_data['main']['pressure']),
            'humidiy': str(json_data['main']['humidity'])
        }
        
    else:
        city = ''
        data = {}
    return render(request,'index.html',{'city':city,'data':data})