"""Quick test of weather data quality."""
import pandas as pd
from pathlib import Path

# Load weather data
weather_path = Path(__file__).parent.parent / "raw" / "ecuador_weather_2013_2017.csv"
df = pd.read_csv(weather_path, parse_dates=['date'])

print("=" * 60)
print("WEATHER DATA QUALITY CHECK")
print("=" * 60)

print(f"\n📊 Basic Stats:")
print(f"Total rows: {len(df):,}")
print(f"Unique cities: {df['city'].nunique()}")
print(f"Date range: {df['date'].min()} to {df['date'].max()}")
print(f"Days per city (avg): {len(df) / df['city'].nunique():.0f}")

print(f"\n🌡️  Temperature Stats:")
print(f"Min temp: {df['temp_min'].min():.1f}°C")
print(f"Max temp: {df['temp_max'].max():.1f}°C")
print(f"Avg temp: {df['temp_mean'].mean():.1f}°C")

print(f"\n💧 Weather Variables:")
print(f"Humidity range: {df['humidity'].min():.0f}% - {df['humidity'].max():.0f}%")
print(f"Max rainfall: {df['precip'].max():.1f} mm/day")

print(f"\n❓ Missing Data:")
missing = df.isnull().sum()
if missing.sum() == 0:
    print("✅ No missing data!")
else:
    print(missing[missing > 0])

print(f"\n🌍 Cities Coverage:")
city_counts = df.groupby('city').size().sort_values(ascending=False)
for city, count in city_counts.head(10).items():
    print(f"  {city:20s} {count:,} days")

print("\n" + "=" * 60)
print("✅ Weather data looks good!")
print("=" * 60)
