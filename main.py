import requests
from twilio.rest import Client
import os
apikey = os.environ.get("WEATHER_API_KEY")
accountSid = os.environ.get("TWILIO_S_ID")
authToken = os.environ.get("TWILIO_AUTH_TOKEN")

MY_LAT = 47.327209 # Your latitude
MY_LONG = 5.044040 # Your longitude
SENDER_NUMBER = "Twilio Phone Number Here"
RECEIVER_NUMBER = "Your Phone Number Here"


parameters = {
    "appid":apikey,
    "lat": MY_LAT,
    "lon": MY_LONG,
    "exclude":"daily,current,minutely"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall",params=parameters)
# response.raise_for_status()
weatherData = response.json()
print(weatherData)
hourlyWeather = weatherData["hourly"][:12]
willRain = False
for hour in hourlyWeather:
    if hour["weather"][0]["id"] < 700:
        willRain = True
if willRain:
    client = Client(accountSid,authToken)
    message = client.messages \
        .create(
        body="Looks like it is going to rain today! Bring your Umbrella!",
        from_=SENDER_NUMBER,
        to=RECEIVER_NUMBER
    )
