"""Client for Open-Meteo weather API."""
import requests
from typing import Dict, List
import pandas as pd
from datetime import datetime, timedelta

class WeatherClient:
    """Fetch historical and forecast weather data from Open-Meteo."""
    
    BASE_URL_HISTORICAL = "https://archive-api.open-meteo.com/v1/archive"
    BASE_URL_FORECAST = "https://api.open-meteo.com/v1/forecast"
    
    def get_historical_weather(
        self,
        latitude: float,
        longitude: float,
        start_date: str,  # Format: "2013-01-01"
        end_date: str     # Format: "2017-12-31"
    ) -> pd.DataFrame:
        """
        Fetch historical weather data.
        
        Args:
            latitude: Location latitude
            longitude: Location longitude
            start_date: Start date (YYYY-MM-DD)
            end_date: End date (YYYY-MM-DD)
            
        Returns:
            DataFrame with daily weather data
        """
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "start_date": start_date,
            "end_date": end_date,
            "daily": ",".join([
                "temperature_2m_max",
                "temperature_2m_min",
                "temperature_2m_mean",
                "relative_humidity_2m_mean",
                "precipitation_sum"
            ]),
            "timezone": "auto"
        }
        
        print(f"  Fetching weather for ({latitude:.4f}, {longitude:.4f})...", end=" ")
        
        try:
            response = requests.get(self.BASE_URL_HISTORICAL, params=params, timeout=30)
            response.raise_for_status()
            
            data = response.json()
            
            # Convert to DataFrame
            df = pd.DataFrame({
                "date": pd.to_datetime(data["daily"]["time"]),
                "temp_max": data["daily"]["temperature_2m_max"],
                "temp_min": data["daily"]["temperature_2m_min"],
                "temp_mean": data["daily"]["temperature_2m_mean"],
                "humidity": data["daily"]["relative_humidity_2m_mean"],
                "precip": data["daily"]["precipitation_sum"],
            })
            
            df["latitude"] = latitude
            df["longitude"] = longitude
            
            return df
            
        except requests.exceptions.RequestException as e:
            print(f"ERROR: {e}")
            raise
    
    def get_forecast(
        self,
        latitude: float,
        longitude: float,
        days: int = 7
    ) -> pd.DataFrame:
        """
        Fetch weather forecast.
        
        Args:
            latitude: Location latitude
            longitude: Location longitude
            days: Number of forecast days (1-16)
            
        Returns:
            DataFrame with forecast data
        """
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "daily": ",".join([
                "temperature_2m_max",
                "temperature_2m_min",
                "temperature_2m_mean"
            ]),
            "forecast_days": days,
            "timezone": "auto"
        }
        
        response = requests.get(self.BASE_URL_FORECAST, params=params, timeout=30)
        response.raise_for_status()
        
        data = response.json()
        
        df = pd.DataFrame({
            "date": pd.to_datetime(data["daily"]["time"]),
            "temp_max": data["daily"]["temperature_2m_max"],
            "temp_min": data["daily"]["temperature_2m_min"],
            "temp_mean": data["daily"]["temperature_2m_mean"],
        })
        
        return df


# Test code
if __name__ == "__main__":
    print("Testing WeatherClient...\n")
    print("=" * 60)
    
    client = WeatherClient()
    
    # Test 1: Fetch 7 days of historical data for Quito
    print("Test 1: Fetch 7 days of historical data for Quito, Ecuador")
    print("-" * 60)
    
    df = client.get_historical_weather(
        latitude=-0.1807,
        longitude=-78.4678,
        start_date="2017-01-01",
        end_date="2017-01-07"
    )
    
    print(f"SUCCESS! Downloaded {len(df)} days")
    print("\nFirst 5 rows:")
    print(df.head())
    
    # Test 2: Fetch current forecast
    print("\n" + "=" * 60)
    print("Test 2: Fetch 3-day forecast for Quito")
    print("-" * 60)
    
    forecast = client.get_forecast(
        latitude=-0.1807,
        longitude=-78.4678,
        days=3
    )
    
    print(f"SUCCESS! Retrieved {len(forecast)} days of forecast")
    print("\nForecast:")
    print(forecast)
    
    print("\n" + "=" * 60)
    print("✅ All tests passed!")
    print("=" * 60)
