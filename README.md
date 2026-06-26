# Weather App

A Python-based backend utility designed to help track barometric pressure changes that may trigger migraines. The script fetches weather data for multiple cities and sends an SMS alert via Twilio if a significant pressure shift is detected.

## Features

- **Multi-City Support**: Tracks barometric pressure for a configurable list of cities.
- **Persistent Storage**: Saves the last known pressure for each city locally to calculate changes over time.
- **SMS Alerts**: Integration with Twilio API to send real-time notifications to your phone.
- **Logging**: Detailed logging of successful data fetches and errors for easy debugging.
- **Security**: Uses environment variables to keep API keys and credentials secure.

## Prerequisites

- Python 3.x
- An [OpenWeatherMap](https://openweathermap.org/api) API Key.
- A [Twilio](https://www.twilio.com/) account and phone number.

## Setup

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd <repo-name>
2. **Install dependencies**:
   ```pip install -r requirements.txt

3. ** Configure Environmental Variables**:
   ```Create a .env file in the root directory and add your credentials:
   WEATHER_API_KEY=your_openweathermap_key
   TWILIO_ACCOUNT_SID=your_twilio_sid
   TWILIO_AUTH_TOKEN=your_twilio_auth_token
   TWILIO_PHONE_NUMBER=your_twilio_number
   MY_PERSONAL_NUMBER=your_actual_phone_number

4. **Run the script**:
   ```python main.py