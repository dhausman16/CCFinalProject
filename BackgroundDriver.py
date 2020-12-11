from WeatherData import *
from SoccerStats import *
from GetSongs import *

#Driver for the web API
def inBackground(inputVariableList):

    #gather info
    teamName = inputVariableList[0]
    token = inputVariableList[1]
    user_id = inputVariableList[2]
    cityName = inputVariableList[3]
    countryName = inputVariableList[4]
    #fill in

    #if team_id = 0, repeat until user inputs correct team name
    team_id = get_team_id(teamName)
    while team_id == 0:
        print ("incorrect team name. Try again.")
        teamName = input ("Enter Favorite Team: ")
        team_id = get_team_id(teamName)

    #get the weather data and display it for the user
    main_description, temp, wind = get_weather_data(cityName, countryName)
    weather_data = [main_description, temp, wind]

    #get the soccer stats and display for the user
    wins, draws, losses = get_stats(team_id)
    soccer_record = [wins, draws, losses]

    #calculate_football_score
    football_score = calculate_football_score(wins, draws, losses)

    #get the songs
    playlist_url = get_songs(main_description, temp, wind, football_score, user_id, token)
    temp = playlist_url.split("com/playlist/",1)[1]
    return weather_data, soccer_record, [temp]
