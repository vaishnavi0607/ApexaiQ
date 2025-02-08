import json

# Load the data from the weather_data.json file
def load_weather_data():
    with open("weather_data.json", "r") as file:
        return json.load(file)
    
"""Check if 'main', 'description', 'temp', and 'humidity' exist and are not null."""
def test_required_fields_exist():
    weather_response = load_weather_data()
    
    assert "weather" in weather_response and len(weather_response["weather"]) > 0
    assert "main" in weather_response

    # Weather fields
    assert "main" in weather_response["weather"][0]
    assert "description" in weather_response["weather"][0]
    assert weather_response["weather"][0]["main"]
    assert weather_response["weather"][0]["description"]

    # Main fields
    assert "temp" in weather_response["main"]
    assert "humidity" in weather_response["main"]
    assert weather_response["main"]["temp"] is not None
    assert weather_response["main"]["humidity"] is not None

"""Check if the response is for the requested city."""
def test_city_name():
    weather_response = load_weather_data()
    input_city = "Shegaon" 
    assert "name" in weather_response
    assert weather_response["name"].lower() == input_city.lower()
