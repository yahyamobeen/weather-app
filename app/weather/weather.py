from fastapi import APIRouter 
from app.schemas_weather import WeatherResponse, WeatherRequest
from fastapi import HTTPException
from os import environ
from dotenv import load_dotenv
import requests
load_dotenv()
WEATHER_API_KEY = environ.get("Weather_API_KEY")

router = APIRouter(prefix="/weather", tags=["weather"])

@router.post("/", response_model=WeatherResponse)
def get_weather(request: WeatherRequest):
    if not WEATHER_API_KEY:
        raise HTTPException(status_code=500, detail="API key not found")
    
    city = request.city
    url = "https://api.weatherapi.com/v1/current.json"
    params = {"key": WEATHER_API_KEY, "q": city}
    
    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="City not found")
    
    data = response.json()
    temperature = data["current"]["temp_c"]

    return WeatherResponse(city=city, temperature=temperature)