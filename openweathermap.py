import os
import requests
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_num = os.getenv("TWILIO_PHONE_NUMBER")
my_cell = os.getenv("MY_PERSONAL_NUMBER")
api_key = os.getenv("WEATHER_API_KEY")


def send_sms(message_body):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
     body=message_body,
     from_=twilio_num,
     to=my_cell
    )
    return message.sid

def main():
    city = input("What city do you want to request data from?: ")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    response = requests.get(url)

    try:
        with open("pressure.txt","r") as f:
            old_pressure = float(f.read())
    except FileNotFoundError:
        old_pressure = None

    if response.status_code == 200:
        data = response.json()
        current_pressure = data["main"]["pressure"]
        print(f"The current pressure is: {current_pressure} hPa")
        with open("pressure.txt","w") as f:
            f.write(str(current_pressure))
        if old_pressure is not None:
            delta_p = abs(current_pressure-old_pressure)
            if delta_p >= 5:
                send_sms(f"Alert! Pressure changed by {delta_p} hPa.")

    else:
        print("Error fetching data")

main()