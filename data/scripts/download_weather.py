"""Download historical weather for all Ecuador cities."""
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

import pandas as pd
from pipeline.weather_client import WeatherClient
from data.scripts.ecuador_cities import ECUADOR_CITIES
import time

def download_all_weather():
    """Download weather for all cities 2013-2017."""
    
    client = WeatherClient()
    all_weather = []
    
    print("=" * 70)
    print(f"Downloading weather for {len(ECUADOR_CITIES)} Ecuador cities")
    print("Date range: 2013-01-01 to 2017-12-31")
    print("This will take 10-20 minutes (API calls are rate-limited)")
    print("=" * 70)
    print()
    
    success_count = 0
    failed_cities = []
    
    for i, (city_name, coords) in enumerate(ECUADOR_CITIES.items(), 1):
        print(f"[{i:2d}/{len(ECUADOR_CITIES)}] {city_name:20s}", end=" ")
        
        try:
            df = client.get_historical_weather(
                latitude=coords["lat"],
                longitude=coords["lon"],
                start_date="2013-01-01",
                end_date="2017-12-31"
            )
            
            df["city"] = city_name
            df["state"] = coords["state"]
            all_weather.append(df)
            
            print(f"✅ {len(df):,} days")
            success_count += 1
            
            # Be nice to the API - add small delay
            time.sleep(1)
            
        except Exception as e:
            print(f"❌ Error: {str(e)[:50]}")
            failed_cities.append(city_name)
            continue
    
    print()
    print("=" * 70)
    
    if not all_weather:
        print("❌ No data downloaded. Check internet connection and try again.")
        return
    
    # Combine all
    print("Combining data...")
    weather_df = pd.concat(all_weather, ignore_index=True)
    
    # Save
    output_path = project_root / "data" / "raw" / "ecuador_weather_2013_2017.csv"
    weather_df.to_csv(output_path, index=False)
    
    print("=" * 70)
    print("✅ SUCCESS!")
    print("=" * 70)
    print(f"Saved to: {output_path}")
    print(f"Total rows: {len(weather_df):,}")
    print(f"Cities downloaded: {success_count}/{len(ECUADOR_CITIES)}")
    print(f"Unique cities: {weather_df['city'].nunique()}")
    print(f"Date range: {weather_df['date'].min()} to {weather_df['date'].max()}")
    print(f"File size: {output_path.stat().st_size / (1024*1024):.1f} MB")
    
    if failed_cities:
        print(f"\n⚠️  Failed cities: {', '.join(failed_cities)}")
        print("You can retry these later or continue without them.")
    
    print("=" * 70)

if __name__ == "__main__":
    download_all_weather()
