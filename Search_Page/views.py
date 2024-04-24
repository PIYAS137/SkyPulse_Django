from django.shortcuts import render
from .forms import GetCityData
import requests

# Create your views here.


def weather_condition_image(text,day):
    condition_text = text.lower()
    print(text,day)
    
    # IF DAY
    if day == 1:
        if "sunny" in condition_text:
            return "https://i.ibb.co/Pw7Zds0/pngwing-com-1.png"
        elif "partly cloudy" in condition_text:
            return "https://i.ibb.co/4sVRxqR/pngwing-com-2.png"
        elif "cloudy" in condition_text:
            return "https://i.ibb.co/j3SRfXy/pngwing-com-4.png"
        elif "overcast" in condition_text:
            return "https://i.ibb.co/j3SRfXy/pngwing-com-4.png"
        elif "rain" in condition_text:
            return "https://i.ibb.co/GM4FDGW/pngwing-com-6.png"
        elif "drizzle" in condition_text:
            return "https://i.ibb.co/GM4FDGW/pngwing-com-6.png"
        elif "fog" in condition_text:
            return "https://i.ibb.co/4sVRxqR/pngwing-com-2.png"
    
    # IF NIGHT
    else :
        if "clear" in condition_text:
            print("CLEAR===========>")
            return "https://i.ibb.co/9TrFLZM/pngwing-com.png"
        elif "partly cloudy" in condition_text:
            return "https://i.ibb.co/1JwP8yS/pngwing-com-3.png"
        elif "cloudy" in condition_text:
            return "https://i.ibb.co/j3SRfXy/pngwing-com-4.png"
        elif "overcast" in condition_text:
            return "https://i.ibb.co/j3SRfXy/pngwing-com-4.png"
        elif "rain" in condition_text:
            return "https://i.ibb.co/F6rzxLZ/pngwing-com-5.png"
        elif "drizzle" in condition_text:
            return "https://i.ibb.co/F6rzxLZ/pngwing-com-5.png"
        elif "fog" in condition_text:
            return "https://i.ibb.co/1JwP8yS/pngwing-com-3.png"



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
    weather_image = None
    weather_condition_text = None
    weather_condition_is_day = None
    if req.method == 'POST':
        form = GetCityData(req.POST)
        if form.is_valid():
            area = form.cleaned_data["city_name"]
            weather_data = get_weather_data(area)
            weather_condition_text = weather_data["current"]["condition"]["text"]
            weather_condition_is_day = weather_data["current"]["is_day"]
            weather_image = weather_condition_image(weather_condition_text,weather_condition_is_day)
    
    return render(req,'Search_Page/Search_Page.html',context={'form':form,'text':weather_condition_text,'weather_image':weather_image,'weather_data':weather_data})