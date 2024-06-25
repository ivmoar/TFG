from flask import Flask, render_template, request
import sys
import os

# Obtener la ruta del directorio 'scripts'
scripts_path = os.path.join(os.path.dirname(__file__), 'scripts')

# Añadir 'scripts' al sys.path
if scripts_path not in sys.path:
    sys.path.append(scripts_path)

from scripts import weather, electricity, functions

app = Flask(__name__)

# Página de inicio del servidor
@app.route("/")
def home():
    return render_template('index.html')

# Llamada a la ejecución de la predicción
@app.route('/execute', methods=['POST'])
def execute():
    param1 = request.form['weather-source']
    param2 = request.form['w-option']
    param3 = request.form['electricity-source']
    param4 = request.form['e-option']

    weather_object = weather.Weather("W")
    electricity_object = electricity.Electricity("E")

    weather_data = None
    current_W_data = None

    # Weather
    if param1 == "Aemet":
        weather_data = weather_object.get_aemet()
        w_temperature_24 = weather_data["Temperature"]
        w_wind_24 = weather_data["Wind"]
        w_uv_24 = "No hay valores"
    elif param1 == "Open Weather":
        weather_data = weather_object.get_openweather()
        w_temperature_24 = weather_data["Temperature"]
        w_wind_24 = weather_data["Wind"]
        w_uv_24 = "No hay valores"
    elif param1 == "Tomorrow.io":
        weather_data = weather_object.get_tomorrowoi()
        w_temperature_24 = weather_data["Temperature"]
        w_wind_24 = weather_data["Wind"]["Speed"]
        w_uv_24= weather_data["UV"]
    elif param1 == "Weather Stack":
        weather_data = weather_object.get_weatherstack()
        w_temperature_24 = str(weather_data["Temperature"]) + "(Solo se ofrece el valor actual)"
        w_wind_24 = str(weather_data["Wind"]["wind_speed"]) + "(Solo se ofrece el valor actual)"
        w_uv_24 = str(weather_data["UVindex"]) + "(Solo se ofrece el valor actual)"
    elif param1 == "All":
        weather_data = weather_object.get_all()
        w_temperature_24 = weather_data["Temperature"]
        w_wind_24 = weather_data["Wind"]
        w_uv_24= weather_data["UV"]

    if param2 == "yes":
        current_W_data = weather_object.get_current()
        w_temperature_current = current_W_data["Temperature"]
        w_wind_current = current_W_data["Wind"]
        w_uv_current = current_W_data["UVindex"]
        weather_data = {**weather_data, **current_W_data}
    else:
        w_temperature_current = "No selected"
        w_wind_current = "No selected"
        w_uv_current = "No selected"
    
    # Electricity
    electricity_data = electricity_object.get_preciodelaluz()

    if param4 == "yes":
        electricity_current = electricity_data["Current"]["Time"] + " - " + str(electricity_data["Current"]["Price"])
    else:
        electricity_current = "No selected"

    combined_data = {**electricity_data, **weather_data}

    udp_response = functions.udp_client(combined_data)

    return render_template('data.html', w_temperature_current=w_temperature_current, w_wind_current=w_wind_current, w_uv_current=w_uv_current, electricity_current=electricity_current, w_temperature_24=w_temperature_24, w_wind_24=w_wind_24, w_uv_24=w_uv_24, e_avg=electricity_data["AVG"], e_max=electricity_data["Max"]["Price"], e_min=electricity_data["Min"]["Price"], e_nexts=electricity_data["Next"], udp_response=udp_response)

if __name__ == "__main__":
    app.run(port=8080)