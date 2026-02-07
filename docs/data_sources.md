# Data Sources

## Calibration Dataset: Corporación Favorita

**Source**: Kaggle Competition "Favorita Grocery Sales Forecasting"  
**URL**: https://www.kaggle.com/competitions/favorita-grocery-sales-forecasting  
**Licensing**: Subject to Kaggle competition terms. Used for research and portfolio demonstration only.  
**Downloaded**: February 7, 2026

**Contents**:
- ~125 million transaction records
- 54 stores across Ecuador
- Date range: 2013-01-01 to 2017-08-15
- Product categories include BEVERAGES, BEER, and 30+ other families

**Files Used**:
- `train.csv`: Daily unit sales by store × item × date (4.77 GB)
- `items.csv`: Product metadata (family, class, perishable) - 4,100 items
- `stores.csv`: Store metadata (city, state, type, cluster) - 54 stores
- `oil.csv`: Daily oil price (Ecuador economy indicator)

**Store Distribution:**
- Quito: 17 stores
- Guayaquil: 8 stores  
- Cuenca: 4 stores
- Other cities: 25 stores across Ecuador

**Beverage Coverage:**
- BEVERAGES family: Juices, bottled water, soft drinks
- BEER family: Alcoholic beverages

**Note**: This dataset is from Ecuador (tropical/equatorial climate) and serves as a proxy for global beverage demand patterns. Enterprise deployment requires calibration on local market data.

---

## Weather Data: Open-Meteo

**Source**: Open-Meteo Historical & Forecast APIs  
**URL**: https://open-meteo.com  
**Licensing**: CC BY 4.0 with attribution. Free for non-commercial use.  
**Required Attribution**: "Weather data by Open-Meteo.com"

**Variables Used**:
- `temperature_2m_max`: Daily maximum temperature (°C)
- `temperature_2m_min`: Daily minimum temperature (°C)
- `temperature_2m_mean`: Daily mean temperature (°C)
- `relative_humidity_2m_mean`: Average relative humidity (%)
- `precipitation_sum`: Total daily precipitation (mm)

---

## Usage Policy

This project uses publicly available data for **educational and research purposes only**.

**For Enterprise Deployment**:
- Verify compliance with Kaggle dataset terms of use
- Obtain commercial weather API license
- Calibrate elasticity on local market data
