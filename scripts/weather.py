from datetime import datetime
from constants import *
from functions import *
import json

class Weather:
    def __init__(self, name):
        self.name = name

    def get_aemet(self):
        AemetRequest(AEMET_URL_OBTAIN_URL)
        data = AemetRequest(AEMET_URL_DATA)

        # Variables
        hora_actual = datetime.now().time()
        indice = None

        #Datos Temperatura
        TempList = data[0]["prediccion"]["dia"][0]["temperatura"]

        for i, elemento in enumerate(TempList):
            if elemento["periodo"] == str(hora_actual.hour):
                indice = i
                break

        if indice is not None:
            indice = len(TempList) - indice
            TempList = TempList[-indice:]
            TempList.extend(data[0]["prediccion"]["dia"][1]["temperatura"]) #TempList.extend(data[0]["prediccion"]["dia"][2]["temperatura"]) para conseguir los datos del siguiente día

            currentT = TempList.pop(0)

            AemetJs["Current"]["temp"] = int(currentT["value"])
            AemetJs["Temperature"] = [int(elemento["value"]) for elemento in TempList]

        #Datos viento
        WindList = data[0]["prediccion"]["dia"][0]["vientoAndRachaMax"]

        for i, elemento in enumerate(WindList):
            if elemento["periodo"] == str(hora_actual.hour):
                indice = i
                break

        if indice is not None:
            indice = len(WindList) - indice
            WindList = WindList[-indice:]
            WindList.extend(data[0]["prediccion"]["dia"][1]["vientoAndRachaMax"]) #WindList.extend(data[0]["prediccion"]["dia"][2]["vientoAndRachaMax"]) para conseguir los datos del siguiente día
            WindList = WindList[::2]

            currentW = WindList.pop(0)

            AemetJs["Current"]["wind"] = int(currentW["velocidad"][0])
            AemetJs["Wind"] = [int(elemento["velocidad"][0]) for elemento in WindList]

        return AemetJs

    def get_openweather(self):
        OpenWeatherData = OpenWeatherRequest(OPENWEATHER_URL_3_0)

        """
        wind = [element["wind"]["speed"] for element in OpenWeatherData["list"][:17]]
        temp = [element["main"]["temp"] for element in OpenWeatherData["list"][:17]]

        OpenWeatherJs["Wind"] = CalcOW(wind, 17)

        temp = CalcOW(temp, 17)

        OpenWeatherJs["Temperature"] = [round(kelvin_celsius(temperatura),2) for temperatura in temp]
        """

        OpenWeatherJs["Current"]["temp"] = round(kelvin_celsius(OpenWeatherData["current"]["temp"]),2)
        OpenWeatherJs["Current"]["wind"] = OpenWeatherData["current"]["wind_speed"]
        OpenWeatherJs["Current"]["uvi"] = OpenWeatherData["current"]["uvi"]

        OpenWeatherData = OpenWeatherData["hourly"][:24]
        
        for data in OpenWeatherData:
            OpenWeatherJs["Temperature"].append(round(kelvin_celsius(data['temp']),2))
            OpenWeatherJs["Wind"].append(data['wind_speed'])
            OpenWeatherJs["UV"].append(data['uvi'])

        return OpenWeatherJs

    def get_tomorrowoi(self):
        TomorrowData = TomorrowRequest('https://api.tomorrow.io/v4/weather/forecast?')
        TomorrowData = TomorrowData["timelines"]["hourly"][:49]

        for data in TomorrowData:
            TomorrowJson["Temperature"].append(data['values']['temperature'])
            TomorrowJson["UV"].append(data['values']['uvIndex'])
            TomorrowJson["Wind"]["Speed"].append(data['values']['windSpeed'])
            TomorrowJson["Wind"]["Dir"].append(data['values']['windDirection'])

        return TomorrowJson

    def get_weatherstack(self):
        WeatherstackData = WeatherstackRequest(WEATHERSTACK_URL)
        WeatherstackJson["Wind"]["wind_speed"] = WeatherstackData["current"]["wind_speed"]
        WeatherstackJson["Wind"]["wind_degree"] = WeatherstackData["current"]["wind_degree"]
        WeatherstackJson["Wind"]["wind_dir"] = WeatherstackData["current"]["wind_dir"]
        WeatherstackJson["UVindex"] = WeatherstackData["current"]["uv_index"]
        WeatherstackJson["Temperature"] = WeatherstackData["current"]["temperature"]

        return WeatherstackJson
    
    def get_current(self):
        aemet = self.get_aemet()
        weatherstack = self.get_weatherstack()
        tomorrowio = self.get_tomorrowoi()
        openweather = self.get_openweather()

        current_temp = (aemet["Current"]["temp"] + weatherstack["Temperature"] + tomorrowio["Temperature"][0] + openweather["Current"]["temp"]) / 4
        current_wind = (aemet["Current"]["wind"] + weatherstack["Wind"]["wind_speed"] + tomorrowio["Wind"]["Speed"][0] + openweather["Current"]["wind"]) / 4

        CurrentJson["Wind"] = round(current_wind, 2)
        CurrentJson["Temperature"] = round(current_temp, 2)
        CurrentJson["UVindex"] = round((weatherstack["UVindex"] + openweather["Current"]["uvi"]) / 2, 2)

        return CurrentJson
    
    def get_all(self):
        aemet = self.get_aemet()
        tomorrowio = self.get_tomorrowoi()
        openweather = self.get_openweather()
        
        #Obtención de la temperatura promedio para las próximas 24 horas
        list1 = openweather["Temperature"]
        list2 = aemet["Temperature"][:24]
        list3 = tomorrowio["Temperature"][1:25]

        for i in range(24):
            aux = round(((list1[i] + list2[i] + list3[i]) / 3), 2)
            AllJson["Temperature"].append(aux)

        #Obtener de la velocidad del viento promedio para las próximas 24 horas
        list1 = openweather["Wind"]
        list2 = aemet["Wind"][:24]
        list3 = tomorrowio["Wind"]["Speed"][1:25]

        for i in range(24):
            aux = round(((list1[i] + list2[i] + list3[i]) / 3), 2)
            AllJson["Wind"].append(aux)

        #Obtener de la radiación promedio para las próximas 24 horas
        list1 = openweather["UV"]
        list2 = tomorrowio["UV"][1:25]

        for i in range(24):
            aux = round(((list1[i] + list2[i]) / 2), 2)
            AllJson["UV"].append(aux)

        return AllJson
    
result = Weather("W")
data = result.get_weatherstack()
#print(data["hourly"][:24][0]['temp'])
print(data)