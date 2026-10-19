import pandas as pd
import requests

def Menu():
    print("¿Qué desea realizar?")
    input("1. Armar recibos (mes actual)" \
    "2. Modificar datos propiedad" \
    "3. Agregar nueva propiedad" \
    "4. Borrar propiedad")

def ObtenerDatosAPI():
    url = "https://api.argentinadatos.com/v1/finanzas/indices/inflacion"
    response = requests.get(url)
    
    if response.status_code == 200:
        datos_json = response.json()
        # Convertimos el JSON directamente a un DataFrame de Pandas
        df_inflacion = pd.DataFrame(datos_json)
        print(datos_json)
        return df_inflacion
    else:
        print("Error al conectar con la API de inflación")
        return None

ObtenerDatosAPI()