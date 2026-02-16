# TLDP Lab 1 – PurpleAir API Script

## API Used
I used the **PurpleAir API** to retrieve air quality sensor data.

## Data Retrieved
The script:
- Calls the PurpleAir '/v1/sensors' endpoint to find a sensor located near inputted coordinates (Ex: Gainesville, FL) using latitude and longitude.
- Uses that sensor’s 'sensor_index' to request detailed data from '/v1/sensors/:sensor_index'.
- Retrieves and saves these fields for that sensor:
  - pm2.5_atm (fine particulate matter concentration in the air)
  - temperature
  - humidity
  - pressure

The full JSON response is saved to 'data/purpleair_sensor.json'.

## How to Run the Code

# 1. Open the project folder in your code editor (for example, VS Code).

# 2. Create and activate a virtual environment (if not already done):
python -m venv venv
.\venv\Scripts\activate      # For Windows

# 3. Install dependencies:
pip install requests

# 4. Add your PurpleAir API key:
In fetch_data.py, replace YOUR_API_KEY_HERE with your PurpleAir READ API key.

# 5. Place Area Coordinatess:
In fetch_data.py, replace current baseline coordinates (Gainesville) with target location to identify the area's sensors.

# 6. Run the script:
python fetch_data.py

# 7. Check the output:
- The script prints the chosen sensor (near Gainesville) and its latest data in the terminal.
- A file named purpleair_sensor.json is created inside the data/ folder containing the JSON response from the API.
