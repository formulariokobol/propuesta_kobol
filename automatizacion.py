import requests as req
import json
import pandas as pd



if __name__ == '__main__':
    form_id = 'a93vkSiKSw6kbWy5xtuT5e'  # Reemplaza esto con el ID de tu formulario
    url_api = f"https://kf.kobotoolbox.org/api/v2/assets/{form_id}/data.json"
    headers = {'Authorization': f'Token f90946e51dce6fa9445df9ed06d2349fb4081113'}
    response = requests.get(url_api, headers=headers)
    if response.status_code == 200:
        respuesta = response.json()
        base = {"type": "FeatureCollection","name": "kobol_data","features":[]}
        baseFeature = {"type":"Feature"}
        baseProperties = {}
        baseGeometry = {"type":"","coordinates":[]}
        for fe in respuesta["results"]:
            baseProperties = fe.copy()
            baseGeometry["type"] = "MultiPolygon"
            baseGeometry["coordinates"] = [[[[float(x.split(" ")[1]),float(x.split(" ")[0])] for x in fe["Extensi_n_territoria_nar_metros_cuadrados"].split(";")]]]
            baseFeature["properties"] = baseProperties
            baseFeature["geometry"] = baseGeometry
            base["features"].append(baseFeature)
        with open('mi_diccionario3.geojson', 'w') as archivo:
            json.dump(base, archivo)