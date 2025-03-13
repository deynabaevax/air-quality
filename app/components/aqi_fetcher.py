import requests

API_KEY = "7017e593af34b3af4f77a21b690c7d67f27b9a20"
BASE_URL = "https://api.waqi.info/feed/sofia/"

def get_air_quality():
    """Fetch and process real-time AQI data for Sofia."""
    url = f"{BASE_URL}?token={API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        
        if data["status"] == "ok":
            return {
                "aqi": data["data"]["aqi"],
                "city": data["data"]["city"]["name"],
                "pm10": data["data"]["iaqi"].get("pm10", {}).get("v", "N/A"),
                "pm25": data["data"]["iaqi"].get("pm25", {}).get("v", "N/A"),
                "temperature": data["data"]["iaqi"].get("t", {}).get("v", "N/A"),
                "humidity": data["data"]["iaqi"].get("h", {}).get("v", "N/A"),
                "wind": data["data"]["iaqi"].get("w", {}).get("v", "N/A"),
                "forecast_pm10": data["data"]["forecast"]["daily"]["pm10"],
                "forecast_pm25": data["data"]["forecast"]["daily"]["pm25"],
            }
        else:
            return {"error": f"API returned an error: {data['status']}"}
    else:
        return {"error": f"Request failed with status code {response.status_code}"}

if __name__ == "__main__":
    print(get_air_quality())
