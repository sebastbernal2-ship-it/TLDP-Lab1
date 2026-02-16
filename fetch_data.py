import requests
import json
from pathlib import Path

API_KEY = "YOUR_API_KEY_HERE"  # put your PurpleAir READ key here


def get_gainesville_sensor_index():
    url = "https://api.purpleair.com/v1/sensors"
    headers = {"X-API-Key": API_KEY}
    params = {
        "fields": "sensor_index,name,latitude,longitude,pm2.5_atm"
    }

    r = requests.get(url, headers=headers, params=params)
    r.raise_for_status()
    data = r.json()

    fields = data["fields"]
    sensors = data["data"]

    lat_idx = fields.index("latitude")
    lon_idx = fields.index("longitude")
    idx_idx = fields.index("sensor_index")
    name_idx = fields.index("name")

    # rough Gainesville bounding box
    for row in sensors:
        lat = row[lat_idx]
        lon = row[lon_idx]

        # skip sensors with missing coords
        if lat is None or lon is None:
            continue

        if 29.5 <= lat <= 29.8 and -82.5 <= lon <= -82.2: # Set your area coords
            sensor_index = row[idx_idx]
            print("Using sensor:", row[name_idx], "index:", sensor_index)
            return sensor_index

    raise ValueError("No Gainesville-area sensor found.")


def fetch_data():
    sensor_index = get_gainesville_sensor_index()

    url = f"https://api.purpleair.com/v1/sensors/{sensor_index}"
    headers = {"X-API-Key": API_KEY}
    params = {
        "fields": "pm2.5_atm,temperature,humidity,pressure"
    }

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    data = response.json()

    print(data)  # prints some data to terminal

    Path("data").mkdir(exist_ok=True)
    with open("data/purpleair_sensor.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


if __name__ == "__main__":
    fetch_data()
