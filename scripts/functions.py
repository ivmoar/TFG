import requests
import numpy as np
from constants import *
import socket
import json

# Petición https - AEMET
def AemetRequest(URL):
    querystring = {"api_key": AEMET_KEY}
    headers = {'cache-control': "no-cache"}
    response = requests.request("GET", URL, headers=headers, params=querystring)
    return response.json()

# Petición https - OpenWeather
def OpenWeatherRequest(URL):
    params = {
        "lat": OPENWEATHER_VALENCIA_LAT,
        "lon": OPENWEATHER_VALENCIA_LON,
        "exclude": OPENWEATHER_EXCLUDE,
        "appid": OPENWEATHER_KEY
    }
    response = requests.request("GET", URL, params=params)
    return response.json()

def kelvin_celsius(kelvin):
    return kelvin - 273.15

# Petición https - Tomorrow.io
def TomorrowRequest(URL):
    params = {
        'location': TOMORROWOI_LOCATION,
        'timesteps': TOMORROWOI_TIMESTEPS,
        'apikey': TOMORROWOI_KEY,
    }
    headers = {"accept": "application/json"}
    response = requests.request("GET", URL, headers=headers, params=params)
    return response.json()

# Petición https - WeatherStack
def WeatherstackRequest(URL):
    params = {
        'access_key': WEATHERSTACK_KEY,
        'query': WEATHERSTACK_VALENCIA_QUERY,
        'units': WEATHERSTACK_UNITS
    }
    headers = {'cache-control': "no-cache"}
    response = requests.request("GET", URL, headers=headers, params=params)
    return response.json()

# Petición https - preciodelaluz
def PreciodelaluzRequest(URL):
    params = {
        'zone': ZONE_PENINSULA_CANARIAS_BALEARS
    }
    headers = {'cache-control': "no-cache"}
    response = requests.request("GET", URL, headers=headers, params=params)
    return response.json()

# UDP
def udp_client(data):
    server_address = (UDP_URL, UDP_PORT)  # Dirección y puerto del servidor UDP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        message = json.dumps(data)
        client_socket.sendto(message.encode(), server_address)
        response, _ = client_socket.recvfrom(4096)
        return response.decode()
    finally:
        client_socket.close()





# Other
"""
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
"""