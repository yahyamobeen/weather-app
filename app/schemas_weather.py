from pydantic import BaseModel, Field
from typing import Optional

class WeatherRequest(BaseModel):
    city:str=Field(description="Name of city")

class WeatherResponse(BaseModel):
    city:str
    temperature:float

class ErrorResponse(BaseModel):
    detail:str

class WeatherUpdateRequest(BaseModel):
    city:Optional[str]=Field(default=None,description="Updated name of city")
    temperature:Optional[float]=Field(default=None,description="Updated temperature")
    

class WeatherUpdateResponse(BaseModel):
    city:str
    temperature:float

class WeatherDeleteResponse(BaseModel):
    city:str