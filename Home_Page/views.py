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
    print(weather_data)
    hourly_data = get_hourly_data(lat,lon)
    next_days_data = get_next_days_data(lat,lon)

    final_hour_res = hourly_data['forecast']['forecastday'][0]['hour'][:6]

    # print("====== HR =======>>>>>",hourly_data)
    if weather_data : 
        return render(req, 'Home_Page/Home_Page.html', context={'weather_data': weather_data,'final_hour_res':final_hour_res,'next_days_data':next_days_data})
            # If the request was not successful, handle the error
    else:
        return render(req, 'Home_Page/Home_Page.html', context={'error_message': 'Failed to retrieve weather data'})