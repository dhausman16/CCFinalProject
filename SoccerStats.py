#find team stats
import http.client

def get_stats(team_id):
    conn = http.client.HTTPSConnection("v3.football.api-sports.io")

    headers = {
        'x-rapidapi-host': "v3.football.api-sports.io",
        'x-rapidapi-key': "da29c59d2f9733e20278fe624f420a0a"
        }

    conn.request("GET", "/teams/statistics?season=2020&team=" +
     str(team_id) + "&league=39", headers=headers)
    res = conn.getresponse()
    data = res.read()
    data = data.decode("utf-8")
    form = data.split("form\":\"",1)[1]
    form = form.split("\",\"fixtures",1)[0]

    #form is now something like "LDWDLLLW"
    wins, draws, losses = 0,0,0
    for char in form:
        if char == 'W':
            wins += 1
        if char == 'D':
            draws += 1
        if char == 'L':
            losses += 1

    return wins, draws, losses


#separate in case the user types in the team name wrong, then you can ask them
# to type it in again if the output is 0
def get_team_id(teamName):
    team_id = 0
    teamName = teamName.lower()
    teamList = ["manchester united",  "newcastle", "fulham", "wolves", "liverpool",
    "southampton", "arsenal", "burnley", "everton", "leicester city", 'tottenham',
    'west ham', 'chelsea', 'manchester city', 'brighton', 'crystal palace',
    'west brom', 'sheiffield united', "leeds united", 'aston villa']
    teamIdList = [33, 34, 36, 39, 40, 41, 42, 44, 45, 46, 47, 48, 49, 50, 51,
    52, 60, 62, 63, 66]
    for i in range (20):
        if teamName == teamList[i]:
            team_id = teamIdList[i]

    return team_id

def calculate_football_score(wins, draws, losses):
    possible_pts = 3 * (wins + draws + losses)
    pts = (wins*3) + draws
    return round(100 * pts / possible_pts)


# # driver code
# teamName = input ("Enter Favorite Team: ")
# team_id = get_team_id(teamName)
# print(get_stats(team_id))
