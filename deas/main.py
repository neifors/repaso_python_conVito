import requests as req
from pathlib import Path
import json


data_uri = "https://datos.comunidad.madrid/catalogo/dataset/35609dd5-9430-4d2e-8198-3eeb277e5282/resource/c38446ec-ace1-4d22-942f-5cc4979d19ed/download/desfibriladores_externos_fuera_ambito_sanitario.json"
my_path = Path('./deas/data')

# response = req.get(data_uri).json()
# with open(my_path / 'deas.json', 'w', encoding= "utf8") as json_file:
#     json.dump(response['data'], json_file, ensure_ascii = False)

def n_deas(datafile):
    return len(datafile)

def sample_by_postalcodes(postalcodes,datafile):
    for dea in datafile:
        yield dea if dea["direccion_codigo_postal"] in postalcodes else None
        
def samples_by_ownership(datafile):
    for ownership in sorted(set(list(map(lambda deas: deas["tipo_titularidad"], data)))):
        yield list(filter(lambda dea: dea["tipo_titularidad"] == ownership,datafile))
    
with open(my_path / 'deas.json', 'r', encoding="utf8") as file:
    data = json.load(file)

    print(f"\nNº total de DEAS en la comunidad de Madrid: {n_deas(data)}")
        
    postalcodes_inside_m30 = ["28029", "28036", "28046", "28039", "28016", "28020", "28002", "28003", "28015", "28010", "28006", "28028", "28008", "28004", "28001", "280013", "28014", "28009", "28007", "28012", "28005", "28045"]
    deas_inside_m30 = filter(lambda dea: dea != None, list(sample_by_postalcodes(postalcodes_inside_m30,data)))
    
    print(f"\nNº total de DEAS dentro de la M-30: {n_deas(list(deas_inside_m30))}")
    
    deas_by_ownership = list(samples_by_ownership(data)) #lista de listas. La primera son los deas privados y la segunda los deas publicos
    
    print(f"\n{deas_by_ownership[0][0]['tipo_titularidad']}: {len(deas_by_ownership[0])}\n{deas_by_ownership[1][0]['tipo_titularidad']}: {len(deas_by_ownership[1])}")