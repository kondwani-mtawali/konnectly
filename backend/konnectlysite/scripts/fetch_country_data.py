import os
import django
import requests

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "konnectlysite.settings")
django.setup()

from konnectlysite.models import Country

# Parse Name, Region, Currency
META_DATA_URL = "https://api.worldbank.org/v2/country?format=json&per_page=300"

# Indicators Dictionary
INDICATOR_CODES = {
    "gross_national_income": "NY.GNP.PCAP.CD",
    "exchange_rate_to_usd": "PA.NUS.FCRF",
    "population": "SP.POP.TOTL",
    "labor_force_participation": "SL.TLF.CACT.ZS",
    "population_growth_rate": "SP.POP.GROW",
    "gdp": "NY.GDP.MKTP.CD",
    "gdp_growth_rate": "NY.GDP.MKTP.KD.ZG",
    "trade_access_score": "TG.VAL.TOTL.GD.ZS",
    "tariff_rate": "TM.TAX.MRCH.SM.AR.ZS",
    "value_of_exports": "TX.VAL.MRCH.WL.CD",
    "value_of_imports": "TM.VAL.MRCH.CD.WT",
    "trade_rating": "IQ.CPA.TRAD.XQ",
    "fdi_percentage": "BX.KLT.DINV.WD.GD.ZS",
    "political_stability_percentile": "PV.PER.RNK",
}

# Country Codes Dictionary
COUNTRY_CODES = {
    "Algeria": "DZA",
    "Angola": "AGO",
    "Benin": "BEN",
    "Botswana": "BWA",
    "Burkina Faso": "BFA",
    "Burundi": "BDI",
    "Cabo Verde": "CPV",
    "Cameroon": "CMR",
    "Central African Republic": "CAF",
    "Chad": "TCD",
    "Comoros": "COM",
    "Congo (Congo-Brazzaville)": "COG",
    "Congo (Congo-Kinshasa)": "COD",
    "Djibouti": "DJI",
    "Egypt": "EGY",
    "Equatorial Guinea": "GNQ",
    "Eritrea": "ERI",
    "Eswatini": "SWZ",
    "Ethiopia": "ETH",
    "Gabon": "GAB",
    "Gambia": "GMB",
    "Ghana": "GHA",
    "Guinea": "GIN",
    "Guinea-Bissau": "GNB",
    "Ivory Coast": "CIV",
    "Kenya": "KEN",
    "Lesotho": "LSO",
    "Liberia": "LBR",
    "Libya": "LBY",
    "Madagascar": "MDG",
    "Malawi": "MWI",
    "Mali": "MLI",
    "Mauritania": "MRT",
    "Mauritius": "MUS",
    "Morocco": "MAR",
    "Mozambique": "MOZ",
    "Namibia": "NAM",
    "Niger": "NER",
    "Nigeria": "NGA",
    "Rwanda": "RWA",
    "Sao Tome and Principe": "STP",
    "Senegal": "SEN",
    "Seychelles": "SYC",
    "Sierra Leone": "SLE",
    "Somalia": "SOM",
    "South Africa": "ZAF",
    "South Sudan": "SSD",
    "Sudan": "SDN",
    "Tanzania": "TZA",
    "Togo": "TGO",
    "Tunisia": "TUN",
    "Uganda": "UGA",
    "Zambia": "ZMB",
    "Zimbabwe": "ZWE",
}

BASE_URL = "https://api.worldbank.org/v2/country/{COUNTRY_CODE}/indicator/{INDICATOR_CODE}?format=json&per_page=1"

# -------------------------------
# Fetching Indicators per country
# -------------------------------
def fetch_indicator(country_code, indicator_code): 
    url = BASE_URL.format(COUNTRY_CODE=country_code, INDICATOR_CODE=indicator_code)
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch {indicator_code} for {country_code}")
        return None
   
    # Try/Except handles unexpected cases of unavailable data in API
    try: 
        """
        World Bank API Structure:
        data[0] - metadata
        data[1] - list of values
        data[1][0] - most recent year's data
        data[1][0]['value'] - numeric value of most recent year
        """
        data = response.json() # Converts API response from JSON to python object
        value = data[1][0]['value']
        return value
    
    # If data is unavailable or malformed, store nothing in DB instead of throwing error
    except (IndexError, TypeError):
        return None

# -------------------------------
# Looping through indicators and countries
# -------------------------------
for country_name, country_code in COUNTRY_CODES.items():
    print(f"Processing {country_name}...")

    country_data = {} # Temp storage for indicator values before populating DB

    for field_name, indicator_code in INDICATOR_CODES.items():
        country_data[field_name] = fetch_indicator(country_code, indicator_code)

    # Create object or update current in Database
    country_obj, created = Country.objects.update_or_create(
        name=country_name,
        defaults=country_data
    )
    status = "CREATED" if created else "UPDATED"
    print(f"{country_name} updated: {created}")