import requests
import numpy as np
from constants import *

#AEMET
def AemetRequest(URL):
    querystring = {"api_key": AEMET_KEY}
    headers = {'cache-control': "no-cache"}
    response = requests.request("GET", URL, headers=headers, params=querystring)
    return response.json()

#OPENWEATHER
def OpenWeatherRequest(URL):
    params = {
        "lat": OPENWEATHER_VALENCIA_LAT,
        "lon": OPENWEATHER_VALENCIA_LON,
        "exclude": OPENWEATHER_EXCLUDE,
        "appid": OPENWEATHER_KEY
    }
    response = requests.request("GET", URL, params=params)
    return response.json()

def CalcOW(lista,index):
    res = []
    index = len(lista) - 1
    for i in range(0, index):
        res.extend(interpolationOW(lista[i], lista[i+1]))
    return res

def interpolationOW(num1, num2):
    aux = np.linspace(num1, num2, 4)
    lista = [round(elemento, 2) for elemento in aux]
    return lista[1:]

def kelvin_celsius(kelvin):
    return kelvin - 273.15

#TOMORROWOI
def TomorrowRequest(URL):
    params = {
        'location': TOMORROWOI_LOCATION,
        'timesteps': TOMORROWOI_TIMESTEPS,
        'apikey': TOMORROWOI_KEY,
    }
    headers = {"accept": "application/json"}
    response = requests.request("GET", URL, headers=headers, params=params)
    return response.json()

#WEATHERSTACK
def WeatherstackRequest(URL):
    params = {
        'access_key': WEATHERSTACK_KEY,
        'query': WEATHERSTACK_VALENCIA_QUERY,
        'units': WEATHERSTACK_UNITS
    }
    headers = {'cache-control': "no-cache"}
    response = requests.request("GET", URL, headers=headers, params=params)
    return response.json()

#PRECIODELALUZ
def PreciodelaluzRequest(URL):
    params = {
        'zone': ZONE_PENINSULA_CANARIAS_BALEARS
    }
    headers = {'cache-control': "no-cache"}
    response = requests.request("GET", URL, headers=headers, params=params)
    return response.json()

def pdllFunction():
    AVGData = PreciodelaluzRequest('https://api.preciodelaluz.org/v1/prices/avg?')
    ElectricityJSON["AVG"] = AVGData["price"]

    MaxData = PreciodelaluzRequest('https://api.preciodelaluz.org/v1/prices/max?')
    ElectricityJSON["Max"]["Time"] = MaxData["hour"]
    ElectricityJSON["Max"]["Price"] = MaxData["price"]

    MinData = PreciodelaluzRequest('https://api.preciodelaluz.org/v1/prices/min?')
    ElectricityJSON["Min"]["Time"] = MinData["hour"]
    ElectricityJSON["Min"]["Price"] = MinData["price"]

    CurrentData = PreciodelaluzRequest('https://api.preciodelaluz.org/v1/prices/now?')
    ElectricityJSON["Current"]["Time"] = CurrentData["hour"]
    ElectricityJSON["Current"]["Price"] = CurrentData["price"]

    indice = CurrentData["hour"][-2:]
    aux_indice = int(indice) + 1
    cadena = indice + '-' + str(aux_indice)

    AllDayData = PreciodelaluzRequest('https://api.preciodelaluz.org/v1/prices/all?')
    AllDayData = {clave: valor for clave, valor in AllDayData.items() if clave >= cadena}

    lista_json = [{"Time": valor["hour"], "Price": valor["price"]} for valor in AllDayData.values()]
    ElectricityJSON["Next"] = lista_json

    return ElectricityJSON