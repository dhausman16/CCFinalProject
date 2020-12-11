#build the playlist and send it to the profile given
import requests
import json

def get_songs(main_description, temp, wind, football_score, user_id, token):
    # SETTINGS
    endpoint_url = "https://api.spotify.com/v1/recommendations?"

    # OUR FILTERS
    limit=30
    market="US"
    # max_instrumentalness = 0.4
    # min_popularity = 95
    if football_score >= 60:
        target_danceability = 0.97
    if football_score > 40:
        target_danceability = 0.60
    else:
        target_danceability = 0.10

    if main_description == "clear": seed_genres = "happy, hip-hop"
    elif main_description == "clouds": seed_genres = "sad"
    elif main_description == "snow": seed_genres = "holidays"
    elif main_description == "rain": seed_genres = "rainy-day"
    else: seed_genres = "pop"

    if temp > 70: seed_genres += ", summer"
    else:seed_genres += ", study"

    if wind > 15: seed_genres += ", rock-n-roll"
    else: seed_genres += ", chill"

    uris = []

    # PERFORM THE QUERY
    query = f'{endpoint_url}limit={limit}&market={market}&seed_genres={seed_genres}&target_danceability={target_danceability}'

    response = requests.get(query,
                   headers={"Content-Type":"application/json",
                            "Authorization":f"Bearer {token}"})
    json_response = response.json()

    for i,j in enumerate(json_response['tracks']):
                uris.append(j['uri'])


    # CREATE A NEW PLAYLIST
    endpoint_url = f"https://api.spotify.com/v1/users/{user_id}/playlists"

    request_body = json.dumps({
              "name": "My Soccer Music",
              "description": "My first programmatic playlist, yooo!",
              "public": False
            })
    response = requests.post(url = endpoint_url, data = request_body, headers={"Content-Type":"application/json",
                            "Authorization":f"Bearer {token}"})

    # print(response.status_code)
    url = response.json()['external_urls']['spotify']
    # FILL THE NEW PLAYLIST WITH THE RECOMMENDATIONS

    playlist_id = response.json()['id']

    endpoint_url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"

    request_body = json.dumps({
              "uris" : uris
            })
    response = requests.post(url = endpoint_url, data = request_body, headers={"Content-Type":"application/json",
                            "Authorization":f"Bearer {token}"})

    return url
