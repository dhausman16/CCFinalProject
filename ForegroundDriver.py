from flask import Flask, redirect, url_for, render_template, request
from BackgroundDriver import *
app = Flask(__name__)

stuff = []

@app.route ("/", methods = ["POST", "GET"])
def getTeamName():
    if request.method == "POST":
        teamName = request.form["teamName"]
        stuff.append(teamName)
        return redirect(url_for("getSpotifyToken"))
    else:
        return render_template("TeamName.html")

@app.route("/spotifytoken", methods = ["POST", "GET"])
def getSpotifyToken():
    if request.method == "POST":
        spotToken = request.form["spotifyToken"]
        stuff.append(spotToken)
        return redirect(url_for("getSpotifyUserName"))
    else:
        return render_template("SpotifyToken.html")


@app.route("/spotifyusername", methods = ["POST", "GET"])
def getSpotifyUserName():
    if request.method == "POST":
        token = request.form["spotifyUserName"]
        stuff.append(token)
        return redirect(url_for("getCityName"))
    else:
        return render_template("SpotifyUserName.html")

@app.route("/cityname",methods = ["POST", "GET"])
def getCityName():
    if request.method == "POST":
        token = request.form["cityName"]
        stuff.append(token)
        return redirect(url_for("getCountryName"))
    else:
        return render_template("CityName.html")

@app.route("/countryname",methods = ["POST", "GET"])
def getCountryName():
    if request.method == "POST":
        token = request.form["countryName"]
        stuff.append(token)
        output = inBackground(stuff)
        return redirect(url_for("finalOutput", results = output))
    else:
        return render_template("CountryName.html")

@app.route("/<results>")
def finalOutput(results):
    weather, record, url = results.split(", [",2)
    record = record[:-1]
    record = record.replace(", ", "-")
    url = url[1:]
    url = url[:-3]
    url = "https://open.spotify.com/playlist/" + url
    weather = weather[3:]
    weather = weather.replace("\'", "")
    weather = weather [:-1]
    coverage, temperature, wind = weather.split(", ",2)
    return render_template("Results.html", coverage = coverage, temperature = temperature, wind = wind, soccer_record = record, spotify_url = url, place = stuff[3] + ", " + stuff[4])

if __name__ == "__main__":
    app.run(debug = True)
