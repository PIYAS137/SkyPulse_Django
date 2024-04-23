from django.shortcuts import render
import requests


def get_weather_data(lat, lon):
    # weather api
    url = f"http://api.weatherapi.com/v1/current.json?key=cbc83ec79bba4512901201847232002&q={lat},{lon}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def get_hourly_data(lat,lon):
    # weather api 
    url = f"http://api.weatherapi.com/v1/forecast.json?key=cbc83ec79bba4512901201847232002&q={lat},{lon}&dt=today&hours=5"
    response = requests.get(url)
    print(response)
    if response.status_code == 200 : 
        return response.json()
    else:
        return None


def get_next_days_data(lat,lon):
    url = f"http://api.weatherapi.com/v1/forecast.json?key=cbc83ec79bba4512901201847232002&q={lat},{lon}&days=7"
    response = requests.get(url)
    print(response)
    if response.status_code == 200 : 
        return response.json()
    else:
        return None


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




def Render_HomePage(req):
    # Get latitude and longitude from the query params
    # lat = req.GET.get('lat') or 23.7984941
    # lon = req.GET.get('lon') or 90.3842619

    # print(lat)
    # print(lon)

    # if lat and lon:
    #     weather_data = get_weather_data(lat, lon)
    #     if weather_data is not None:
    #         print(weather_data)
    #         # Pass the weather data to the template
    #         return render(req, 'Home_Page/Home_Page.html', context={'weather_data': weather_data})
    #     else:
    #         # If the request was not successful, handle the error
    #         return render(req, 'Home_Page/Home_Page.html', context={'error_message': 'Failed to retrieve weather data'})
    # else:
    #     # If latitude and longitude are not provided, handle the error
    #     return render(req, 'Home_Page/Home_Page.html', context={'error_message': 'Latitude and longitude not provided'})


    lat = 23.7984941
    lon = 90.3842619

    weather_data = get_weather_data(lat, lon)
    weather_condition_text = weather_data["current"]["condition"]["text"]
    weather_condition_is_day = weather_data["current"]["is_day"]



    weather_image = weather_condition_image(weather_condition_text,weather_condition_is_day)
    print("=====>>>>",weather_image)
    weather_data['current']['max_temp_c'] = weather_data['current']['feelslike_c'] + 5
    weather_data['current']['min_temp_c'] = weather_data['current']['feelslike_c'] - 9
    hourly_data = get_hourly_data(lat,lon)
    next_days_data = get_next_days_data(lat,lon)

    final_hour_res = hourly_data['forecast']['forecastday'][0]['hour'][:6]

    # print("====== HR =======>>>>>",hourly_data)
    if weather_data : 
        return render(req, 'Home_Page/Home_Page.html', context={'weather_data': weather_data,'final_hour_res':final_hour_res,'next_days_data':next_days_data,'weather_image':weather_image})
            # If the request was not successful, handle the error
    else:
        return render(req, 'Home_Page/Home_Page.html', context={'error_message': 'Failed to retrieve weather data'})