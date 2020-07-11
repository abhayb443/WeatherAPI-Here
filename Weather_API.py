import httplib2
import json


def getWeather(inputString):

    # Use Here Maps to convert a location into Latitute/Longitute coordinates
    # FORMAT: https://geocode.search.hereapi.com/v1/geocode?q=5+Rue+Daunou%2C+75000+Paris%2C+France

    locationString = inputString.replace(" ", "+")
    apiKey = 'Add Your HERE Maps API Key Here'

    url = ('https://weather.ls.hereapi.com/weather/1.0/report.json?product=observation&name=%s&apiKey=%s'
           %(locationString, apiKey))

    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    temperature = result.get('observations').get('location')[0].get('observation')[0].get('temperature')
    visibility = result.get('observations').get('location')[0].get('observation')[0].get('visibility')
    humidity = result.get('observations').get('location')[0].get('observation')[0].get('humidity')
    skyDescription = result.get('observations').get('location')[0].get('observation')[0].get('skyDescription')

    return (temperature, visibility, humidity, skyDescription)

if __name__ == "__main__":
    getWeather('Chicago')
