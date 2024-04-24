from django.shortcuts import render
from .forms import GetCityData
import requests

# Create your views here.


def get_weather_data(area):
    # weather api
    url = f"http://api.weatherapi.com/v1/current.json?key=cbc83ec79bba4512901201847232002&q={area}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def Render_Search_Page(req):

    form = GetCityData()
    weather_data = None 
    if req.method == 'POST':
        form = GetCityData(req.POST)
        if form.is_valid():
            area = form.cleaned_data["city_name"]
            weather_data = get_weather_data(area)
    
    return render(req,'Search_Page/Search_Page.html',context={'form':form,'weather_data':weather_data})