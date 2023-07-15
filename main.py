import os

import requests
from twilio.rest import Client

MY_LAT = 22.474751
MY_LONG = 88.362289

api_key = os.environ.get("OWM_API_KEY")     #go to Terminal, enter command env
account_sid = "Enter Account SID"
auth_token = "Your Auth Token"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    # "exclude": "current, minutely, daily"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False

weather_slice = weather_data["list"][:6]
for item in weather_slice:
    condition_code = item["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It might rain today. Remember to bring an umbrella.",
        from_='+14027654840',
        to='+919818203823'
    )



# https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
