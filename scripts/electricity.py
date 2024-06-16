from constants import *
from functions import *

class Electricity:
    def __init__(self, name):
        self.name = name

    def get_preciodelaluz(self):
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