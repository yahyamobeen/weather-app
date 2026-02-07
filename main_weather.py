from fastapi import FastAPI
from app.weather.weather import router as weather_router
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app= FastAPI()
app.include_router(weather_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (for development)
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

app.mount("/static", StaticFiles(directory="frontend", html=True), name="frontend")