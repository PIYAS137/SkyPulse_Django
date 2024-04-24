from django.shortcuts import render
import requests

# Create your views here.


def get_weather_data(lat, lon):
    # weather api
    url = f"http://api.weatherapi.com/v1/current.json?key=cbc83ec79bba4512901201847232002&q={lat},{lon}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None



def Render_AlertPage(req):

    lat = 23.7984941
    lon = 90.3842619

    weather_data = get_weather_data(lat, lon)

    return render(req,'Alert_Page/Alert_Page.html',context={'weather_data':weather_data})