import requests
import pandas as pd

def fetch_data():
    API_KEY = '3b1549c29e5fb2e6923fc7f0e27daee1'  # Replace with your OpenWeatherMap API key
    CITY = 'Islamabad'
    URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"  # Add units=metric for Celsius

    response = requests.get(URL)

    # Check the status of the response
    if response.status_code != 200:
        raise Exception(f"API call failed with status code {response.status_code}: {response.text}")

    data = response.json()

    # Check if 'list' is in the data
    if 'list' not in data:
        raise Exception(f"Error in API response: {data.get('message', 'Unknown error')}")

    # Extract relevant fields
    weather_data = []
    for item in data['list']:
        weather_data.append({
            "Temperature": item['main']['temp'],  # Temperature in Celsius
            "Humidity": item['main']['humidity'],  # Percentage
            "Wind Speed": item['wind']['speed'],   # Speed in m/s
            "Weather Condition": item['weather'][0]['description'],  # Condition (e.g., clear sky)
            "Date": item['dt_txt']  # Date and time
        })

    # Save to CSV
    raw_data_path = 'raw_data.csv'
    df = pd.DataFrame(weather_data)
    df.to_csv(raw_data_path, index=False)
    print(f"Weather data saved to {raw_data_path}")

if __name__ == "__main__":
    fetch_data()
