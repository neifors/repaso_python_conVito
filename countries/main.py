import requests as req
import csv, json, os, sys
from pathlib import Path
import time, threading
from concurrent.futures import ThreadPoolExecutor
from country import Country

def add_to_csvFile(path,lines):
    with open(path,'a', newline='') as f:
        csv_file =csv.writer(f)
        if len(lines)==2:
            for line in lines:
                csv_file.writerow(line)
        else:
            csv_file.writerow(lines)
            
def get_data_from_ulr(area, to_search):
    if area == 'region':
        response = req.get(f'https://restcountries.eu/rest/v2/region/{to_search}').json()
        return response
    elif area == 'country':
        response = req.get(f'https://restcountries.eu/rest/v2/name/{to_search}').json()
        return response
            
def line_already_exists(path, name):
    with open(path,'r') as file:
        lectura = csv.reader(file)
        for line in lectura:
            if line[0] == name:
                return False
    return True
    
def country_finder():
    name = input("\n¿Qué país desea buscar?: ")
    my_path = Path('./data/searched_countries.csv')
    
    ##? MENSAJE ASÍNCRONO
    with ThreadPoolExecutor() as executor:
        future = executor.submit(get_data_from_ulr, area='country', to_search=name)
        print('\n\nObteniendo datos resultado.....')
    
    ##? IMPRIMIR DATOS DEL PAIS SELECCIONADO Y GUARDARLOS EN searched_countries.csv    
    if future.result() != {"status": 404, "message": "Not Found"}:
        print(f"Name: {future.result()[0]['name']}\nCapital: {future.result()[0]['capital']}\nRegion: {future.result()[0]['region']}\nPopulation: {future.result()[0]['population']}\nArea: {future.result()[0]['area']}\nLanguage: {future.result()[0]['languages'][0]['name']}\nFlag url: {future.result()[0]['flag']}")
        data_to_save = [future.result()[0]['name'],future.result()[0]['capital'],future.result()[0]['region'],future.result()[0]['population'],future.result()[0]['area'],future.result()[0]['languages'][0]['name'],future.result()[0]['flag']]
        if my_path.is_file():
            if line_already_exists(my_path, future.result()[0]['name']):
                add_to_csvFile(my_path,data_to_save)
        else:
            head_line = ['name', 'capital', 'region', 'population', 'area', 'language', 'flag']
            add_to_csvFile(my_path,[head_line,data_to_save])
        
        ##? GUARDAR BANDERA EN FORMATO SVG
        save_flag = input("¿Quieres guardar la bandera de este pais en formato svg? (y/n): ")
        while not save_flag in "yYnN":
            save_flag = input("\n\nRESPUESTA INCORRECTA\n¿Quieres guardar la bandera de este pais en formato svg? (y/n): ")
        if save_flag in "yY":
            response = req.get(future.result()[0]['flag'])
            save_flag_svg('./data/images',response.content, name)
        
    else:
        print(f"\nNo hay resultados para la búsqueda que estás realizando.")
          
def region_countries_extraction():
    region = input("\n¿Qué continente desea buscar?: ")
    my_path = Path(f'./data/{region}.json')

    with ThreadPoolExecutor() as executor:
        future = executor.submit(get_data_from_ulr, area='region', to_search=region)
        print('\n\nObteniendo datos resultado.....')
    
    if future.result() != {"status": 404, "message": "Not Found"}:
        with open(my_path, 'w') as json_file:
            json.dump([element for element in future.result()], json_file)
    else:
        print(f"\nNo hay resultados para la búsqueda que estás realizando.")
        
def save_flag_svg(path, img_content, name):
    with open(path+f"/{name}.svg", "wb") as img:
        img.write(img_content)

def get_total_population():
    region = input('\nContinente del que desea saber la población total: ')
    try:
        with open(f'./data/{region}.json', 'r') as f:
            json_file = json.load(f)
            acum = 0
            for element in json_file:
                acum += element['population']
        return {'region':f'{region}','population':acum}
    except FileNotFoundError:
        print('\nERROR: No existe el fichero del continente del que desea obtener la población total.\nRealiza primero la búsqueda del continente y consulta la población de nuevo.\nQuizás si existe, pero simplemente escribiste mal el continente.')
        return None

def backup_history_flags(flags_container):
    for url in flags_container[1:-1]:
        url_split = url.split('/')
        file_name = url_split[-1].split('.')
        name = file_name[0]
        response = req.get(url)    
        save_flag_svg('./data/flags_history_backup', response.content, name)

def search_history():
    flags_container = []
    countries = []
    ##? IMPRIME LOS PAISES (Y SU POBLACION) QUE SE ENCUENTRAN EN EL HISTORIAL DE BÚSQUEDA
    with open('./data/searched_countries.csv', 'r') as file:
        lectura = csv.reader(file)
        next(file, None)
        for row in lectura:
            print(f"name:{row[0]}**\n**poblacion: {row[3]}")
            
            countries.append(create_obj_country(row[0],row[1],float(row[3]))) # creamos objetos Country con cada uno de los paises que 
                                                                              # se encuentran en el historial
            flags_container.append(row[-1]) # guardamos la url de todas las banderas para que si luego decidimos guardarlas
                                            # que no tengamos que recorrer otra vez todo el historial.
    print(f"\nLa suma total de la poblacion de todos los paises mostrados anteriormente es: {Country.population_sum}")
    ##? GUARDAR BANDERAS DE LOS PAISES QUE APARECEN EN EL HISTORIAL DE BÚSQUEDA        
    save_flags_svg = input("¿Desea guardar todas las banderas correspondientes a los países del historial de búsqueda? (y/n): ") 
    while not save_flags_svg in "yYnN":
        save_flags_svg = input("\n\nRESPUESTA INCORRECTA\n¿Desea guardar todas las banderas correspondientes a los países del historial de búsqueda? (y/n): ")
    if save_flags_svg in 'yY':
        backup_history_flags(flags_container)

def create_obj_country(name,capital,population):
    return Country(name,capital,population)    

def menu():
    os.system('cls')
    opt=input('\nMENÚ PRINCIPAL\n1. Pais\n2. Continente\n3. Población\n4. Historial de búsqueda\n5. Salir\n\nOPCIÓN: ')
    while not opt in '12345':
        opt=input('\nOPCION INCORRECTA\n1. Pais\n2. Continente\n3. Población\n4. Historial de búsqueda\n5. Salir\n\nOPCIÓN: ')

    if opt == '1':
        country_finder()
    elif opt == '2':
        region_countries_extraction()
    elif opt == '3':
        region_total_population = get_total_population()
        if region_total_population != None:
            print(f"{region_total_population['region']}: {region_total_population['population']}")
    elif opt == '4':
        search_history()
    else:
        print('Hasta pronto...')
        sys.exit()

def main():
    
    while True:
        menu()
        input('\nPulse enter para continuar')
     
main()