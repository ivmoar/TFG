################################# APIs DATA #################################
#Aemet
AEMET_KEY = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJpdmFudGVuaXM2QGhvdG1haWwuY29tIiwianRpIjoiODkwMWVlMWEtNWMyOC00NTEzLWE5YWQtZjNhNzFiODY0MDhlIiwiaXNzIjoiQUVNRVQiLCJpYXQiOjE2OTUyNTA5ODAsInVzZXJJZCI6Ijg5MDFlZTFhLTVjMjgtNDUxMy1hOWFkLWYzYTcxYjg2NDA4ZSIsInJvbGUiOiIifQ.b5rIzkNjXpVvDeswx0jnftViYFiJfIFKdim30oXwukY"
AEMET_VALENCIA_CODE = "46250"
AEMET_URL_OBTAIN_URL = "https://opendata.aemet.es/opendata/api/prediccion/especifica/municipio/horaria/46250" #This URL gives us a new URL wich we have to use to obtain the data
AEMET_URL_DATA = "https://opendata.aemet.es/opendata/sh/b331c3c9"
AemetJs = {
    "Current": {
        "wind": None,
        "temp": None
    },
    "Wind": [],
    "Temperature": []
}

#OpenWeather
OPENWEATHER_KEY = "9f74a5005ea5ccfd86c211a8bb40cf70"
OPENWEATHER_VALENCIA_ID = "2509954"
OPENWEATHER_VALENCIA_NAME = "Valencia"
OPENWEATHER_VALENCIA_COD = "200"
OPENWEATHER_VALENCIA_LON = "-0.378"
OPENWEATHER_VALENCIA_LAT = "39.47"
OPENWEATHER_EXCLUDE = "minutely,daily,alerts"
OPENWEATHER_URL_2_5 = "https://api.openweathermap.org/data/2.5/forecast?lat=39.47&lon=-0.38&appid=9f74a5005ea5ccfd86c211a8bb40cf70"
OPENWEATHER_URL_3_0 = "https://api.openweathermap.org/data/3.0/onecall?"
OpenWeatherJs = {
    "Current": {
        "wind": None,
        "temp": None,
        "uvi": None
    }, 
    "Wind": [],
    "Temperature": [],
    "UV": []
}

#Tomorrow.io
TOMORROWOI_KEY = "1U50XpASQrdgYPG4iEGVel1XkhhR6M7Z"
TOMORROWOI_URL_DAY = "https://api.tomorrow.io/v4/weather/forecast?"
TOMORROWOI_URL_CURRENT = "https://api.tomorrow.io/v4/weather/realtime?"
TOMORROWOI_LOCATION = "valencia"
TOMORROWOI_TIMESTEPS = "1h"
TomorrowJson = {
    "Temperature": [],
    "UV": [],
    "Wind": {
        "Speed": [],
        "Dir": [],
    }
}

#WeatherStack
WEATHERSTACK_KEY = "da18d0c4be2e3d33b0cac5fcdd5778d5"
WEATHERSTACK_URL = "http://api.weatherstack.com/current"
WEATHERSTACK_VALENCIA_QUERY = "Valencia, Spain"
WEATHERSTACK_UNITS = "m"
WeatherstackJson = {
    "Wind": {"wind_speed": None, "wind_degree": None, "wind_dir": None},
    "UVindex": None,
    "Temperature": None
}

#Current
CurrentJson = {
    "Wind": None,
    "UVindex": None,
    "Temperature": None
}

#All
AllJson = {
    "Wind": [],
    "Temperature": [],
    "UV": []
}
###################################################################
###################### - preciodelaluz API - ######################
#Api Key: No necesaria
#Zone: PCB (Península, Canarias & Balears) - CYM (Ceuta & Melilla)
#URL-Obtiene la serie de precios completa: https://api.preciodelaluz.org/v1/prices/all?

ZONE_PENINSULA_CANARIAS_BALEARS = "PCB"
ZONE_CEUTA_MELILLA = "CYM"
PRECIODELALUZ_ALL_URL = "https://api.preciodelaluz.org/v1/prices/all?"
PRECIODELALUZ_AVG_URL = "https://api.preciodelaluz.org/v1/prices/avg?"
PRECIODELALUZ_MAX_URL = "https://api.preciodelaluz.org/v1/prices/max?"
PRECIODELALUZ_MIN_URL = "https://api.preciodelaluz.org/v1/prices/min?"
PRECIODELALUZ_NOW_URL = "https://api.preciodelaluz.org/v1/prices/now?"

ElectricityJSON = {
    "Current": {
        "Time": None,
        "Price": None
    },
    "AVG": None,
    "Max": {
        "Time": None,
        "Price": None
    },
    "Min": {
        "Time": None,
        "Price": None
    },
    "Next": None
}

#####################################################
###################### - UDP - ######################
UDP_URL = "http://158.42.16.178"
UDP_PORT = 15500