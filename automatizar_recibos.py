import pandas as pd
import requests
import json 

def Menu():
    print("¿Qué desea realizar?")
    input("1. Armar recibos (mes actual)" \
    "2. Modificar datos propiedad" \
    "3. Agregar nueva propiedad" \
    "4. Borrar propiedad")

def TraerDatosJSON():
    with open("lista_clientes.json", "r", encoding="utf-8") as arch:
        datos = json.load(arch)
    df_json = pd.json_normalize(datos["contratos"])
    return df_json

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

def CalcularAumentoIPC(df_filtrado,monto_inicial, fecha_inicio, meses_a_actualizar):
    print("")

def ModificarDatosPropiedad(datos): # Agregar chequeo para la propiedad
    modificar = input("Ingrese la dirección de la propiedad que desea modificar (también se acepta el ID): ")
    

df_json = TraerDatosJSON()
match Menu():
    case 1:
        ArmarRecibos()
    case 2:
        ModificarDatosPropiedad(df_json)
    case 3:
        AgregarNuevaPropiedad()
    case 4: 
        BorrarPropiedad()


df_datosAPI = ObtenerDatosAPI()
monto = CalcularAumentoIPC(df_datosAPI)
print(monto)

# Ver si es posible pasar los datos directamente desde un Excel