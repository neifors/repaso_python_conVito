import requests as req
import csv, json, os, sys
from pathlib import Path

'''
* Ejercicio 4: Crear una pequeña aplicación con las siguientes características:
    
    Debe permitirnos buscar países por nombre y por continentes 
    Cada uno de los países buscados debe quedar escrito en un archivo tipo csv que solo admitira los siguientes valores: 
            name, 
            capital, 
            region, 
            population, 
            area, 
            idioma (el primero), 
            flag 
    A su vez estos valores acturán como encabezados 
    
    Cuando se busquen países por continente, estos deben ser escritos en un archivo json con nombre dinámico 
    EJ. dinámico --> Si se busca "africa", el archivo deberá llamarse --> africa.json
'''

def add_to_csvFile(path,lines):
    with open(path,'a', newline='') as f:
        csv_file =csv.writer(f)
        if len(lines)==2:
            for line in lines:
                csv_file.writerow(line)
        else:
            csv_file.writerow(lines)
            
def country_finder():
    name = input("\n¿Qué país desea buscar?: ")
    my_path = Path('./data/searched_countries.csv')
    
    try: 
        response = req.get(f'https://restcountries.eu/rest/v2/name/{name}').json()
        print(f'''
              Name: {response[0]['name']},
              Capital: {response[0]['capital']},
              Region: {response[0]['region']},
              Population: {response[0]['population']},
              Area: {response[0]['area']},
              Language: {response[0]['languages'][0]['name']},
              Flag url: {response[0]['flag']}''')
        data_to_save = [response[0]['name'],response[0]['capital'],response[0]['region'],response[0]['population'],response[0]['area'],response[0]['languages'][0]['name'],response[0]['flag']]
    except KeyError:
        print(f"No hay resultados para la búsqueda que estás realizando.")

        return False
    
    if my_path.is_file():
        add_to_csvFile(my_path,data_to_save)
        return True
    else:
        head_line = ['name', 'capital', 'region', 'population', 'area', 'language', 'flag']
        add_to_csvFile(my_path,[head_line,data_to_save])
        return True
        
def continent_countries_extraction():
    region = input("\n¿Qué continente desea buscar?: ")
    my_path = Path(f'./data/{region}.json')

    response = req.get(f'https://restcountries.eu/rest/v2/region/{region}').json()
    if response != {"status": 404, "message": "Not Found"}:
        with open(my_path, 'w') as json_file:
            json.dump([element for element in response], json_file)
            return True
    else:
        print( 'ERROR 404: Continent Not Found')
        return False
    
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