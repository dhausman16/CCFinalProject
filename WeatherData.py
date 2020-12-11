import json
import requests

def get_weather_data(cityName, countryName):
    weather_data = requests.get("http://api.openweathermap.org/data/2.5/weather?q="
    + str(cityName) + "," + str(countryName) + "&appid=a3fa997fe96687a6375343ae5979c3bb")
    weather_data = str(weather_data.json())

    #get the important weather data
    main_description = weather_data.split("main\': \'",1)[1]
    main_description = main_description.split("\', \'descripti",1)[0]
    main_description = main_description.lower()
    temp = weather_data.split("temp\': ",1)[1]
    temp = float(temp.split(", \'feels_li",1)[0])
    temp = ((temp - 273.15) * (9/5)) + 32 #convert to Farenheit
    temp = round(temp, 2)
    wind = weather_data.split("speed\': ",1)[1]
    wind = float(wind.split(", \'deg",1)[0])
    wind = round(wind, 2)
    return main_description, temp, wind

# def calculate_weather_score(main_description, temp, wind):
#     #assume temp range 120 to -20 or so
#     temp_score = abs(temp - 72) / 4 #divide by 4 to minimize the effect
#     wind_score = wind / 2 #same as above
#     main_description_score = 0 #certain thing means a certain number
#     #cloudy is like 5
#     #sunny is 0
#     #snowy is 10
#     #rain is 20
#     return 50 - main_description_score - temp_score - wind_score


# # driver code
# cityName = input ("Enter your city: ")
# countryName = input("Enter your country (use abbreviations for countries that are more than one name): ")
# #cityName, countryName = "nashville", "us"
# print(get_weather_data(cityName, countryName))
