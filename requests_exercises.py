import requests as req
import csv, json, os, sys
from pathlib import Path
import time, threading
from concurrent.futures import ThreadPoolExecutor

def add_to_csvFile(path,lines):
    with open(path,'a', newline='') as f:
        csv_file =csv.writer(f)
        if len(lines)==2:
            for line in lines:
                csv_file.writerow(line)
        else:
            csv_file.writerow(lines)
            
def get_data_from_ulr(area, to_search):
    if area == 'continent':
        response = req.get(f'https://restcountries.eu/rest/v2/region/{to_search}').json()
        return response
    elif area == 'country':
        response = req.get(f'https://restcountries.eu/rest/v2/name/{to_search}').json()
        return response
            
def country_finder():
    name = input("\n¿Qué país desea buscar?: ")
    my_path = Path('./data/searched_countries.csv')
    
    with ThreadPoolExecutor() as executor:
        future = executor.submit(get_data_from_ulr, area='country', to_search=name)
        print('\n\nObteniendo datos resultado.....')
        
    if future.result() != {"status": 404, "message": "Not Found"}:
        print(f"Name: {future.result()[0]['name']}\nCapital: {future.result()[0]['capital']}\nRegion: {future.result()[0]['region']}\nPopulation: {future.result()[0]['population']}\nArea: {future.result()[0]['area']}\nLanguage: {future.result()[0]['languages'][0]['name']}\nFlag url: {future.result()[0]['flag']}")
        data_to_save = [future.result()[0]['name'],future.result()[0]['capital'],future.result()[0]['region'],future.result()[0]['population'],future.result()[0]['area'],future.result()[0]['languages'][0]['name'],future.result()[0]['flag']]
        if my_path.is_file():
            add_to_csvFile(my_path,data_to_save)
        else:
            head_line = ['name', 'capital', 'region', 'population', 'area', 'language', 'flag']
            add_to_csvFile(my_path,[head_line,data_to_save])
    else:
        print(f"\nNo hay resultados para la búsqueda que estás realizando.")
  
def continent_countries_extraction():
    region = input("\n¿Qué continente desea buscar?: ")
    my_path = Path(f'./data/{region}.json')

    with ThreadPoolExecutor() as executor:
        future = executor.submit(get_data_from_ulr, area='continent', to_search=region)
        print('\n\nObteniendo datos resultado.....')
    
    if future.result() != {"status": 404, "message": "Not Found"}:
        with open(my_path, 'w') as json_file:
            json.dump([element for element in future.result()], json_file)
    else:
        print(f"\nNo hay resultados para la búsqueda que estás realizando.")
        
def get_total_population():
    continent = input('\nContinente del que desea saber la población total: ')
    try:
        with open(f'./data/{continent}.json', 'r') as f:
            json_file = json.load(f)
            acum = 0
            for element in json_file:
                acum += element['population']
        return {'continent':f'{continent}','population':acum}
    except FileNotFoundError:
        print('\nERROR: No existe el fichero del continente del que desea obtener la población total.\nRealiza primero la búsqueda del continente y consulta la población de nuevo.\nQuizás si existe, pero simplemente escribiste mal el continente.')
        return None

def menu():
    os.system('cls')
    opt=input('\nMENÚ PRINCIPAL\n1. Pais\n2. Continente\n3. Población\n4. Salir\n\nOPCIÓN: ')
    while not opt in ('1','2','3','4'):
        opt=input('\nOPCION INCORRECTA\n1. Pais\n2. Continente\n3. Población\n3. Salir\n\nOPCIÓN: ')
    return opt

def main():
   
    while True:
        opt = menu()
        if opt == '1':
            country_finder()
        elif opt == '2':
            continent_countries_extraction()
        elif opt == '3':
            continent_total_population = get_total_population()
            if continent_total_population != None:
                print(f"{continent_total_population['continent']}: {continent_total_population['population']}")
        else:
            print('Hasta pronto...')
            break
        input('\nPulse enter para continuar')
         
main()

sys.exit()