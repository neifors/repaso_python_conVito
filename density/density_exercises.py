import json, csv
from pathlib import Path

#! ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ CLASES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

'''
* Ejercicio 5: Crear una clase de tipo municipality/municipio
* Debe tener tantas propiedas como claves en el diccionario
'''
class Municipality():
    '''
    * Ejercicio 12: Crea un contador de modo que cada vez que se cree una nueva instancia, 
    el mencionado contador aumente en 1
    '''
    counter = 0
    annual_growth_rate = 0.02
    total_comunity_population = 0
    
    def __init__(self, name, density, surface_km2):
        self.name = name                #str
        self.density = density          #float
        self.surface = surface_km2      #float    
        Municipality.counter += 1
        Municipality.total_comunity_population += self.total_population

    def __repr__(self):
        '''
        * Ejercicio 7: Crear una función que acepte un solo parámetro (municipio) 
        y que devuleva un objeto con las propiedades (nombre, densidad, superfice)
        '''
        return f'Municipality({self.name}, {self.density}, {self.area})'

    def __str__(self):
        '''
        * Ejercicio 8: Modificar el tipo de impresión (print) para que se vea así --> 	 nombre: valor
                                                densidad: float con tres decimales
                                                superficie: float con tres decimales
        '''
        return f'\t\t\tNombre: {self.name}\n\t\t\tDensidad: {self.density:.3f}\n\t\t\tSuperficie: {self.surface:.3f}\n\t\t\tPoblación: {self.total_population:.2f}'

    @property
    def total_population(self):
        '''
        * Ejercicio 10: Considerando que en cada objeto tenemos la superficie y densidad ambas por km2, crear un MÉTODO 
        (una función dentro del objeto) que devuelva la densidad total del municipio dado.
        '''
        return self.surface*self.density
    
    def apply_year_growth_rate(self):
        '''
        * Ejercicio 15: Define un método que aplique el crecimiento anual sobre un objeto
        '''
        print(f'\nLa densidad por Km2 de {self.name}, pasa de ser: {self.density:.2f}')
        self.density += self.density*Municipality.annual_growth_rate
        print(f'a ser: {self.density:.2f}')
    
    def set_annual_growth(self, rate):
        Municipality.annual_growth_rate = rate
    
    @classmethod
    def from_str(cls, cadena):
        '''
        * Ejercicio 13: Crea un **classmethod** llamado from_str que crea una instancia de la siguiente cadena --> "test-3.54-23.86"
        '''
        lista = cadena.split('-')
        try:
            density = float(lista[1])
            surface = float(lista[2])
            return cls(lista[0],density,surface)
        except ValueError as e:
            print(f'Error: {e}')
    
    @classmethod
    def get_counter(cls):
        return cls.counter
    
#! ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ FIN CLASES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#! ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ FUNCIONES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def density_average(dataset):
    '''
    * De ahora en mas al valor de la clave "densidad_por_km2" la llamaremos densidad
    * Ejercicio 1: Obtender la densidad media de los municipios de Madrid
    '''
    total_density = 0
    total_samples = len(dataset)
    for data in dataset:
        total_density += data['densidad_por_km2']
    return f'{(total_density/total_samples):.2f}'

def get_town_by_ine(dataset, ine_code): # "municipio_codigo_ine" // "municipio_nombre"
    '''
    * Ejercicio 2: Obtener municipio por codigo ine // Extra: utilizando función filter
    '''
    for data in dataset:
        if ine_code == data["municipio_codigo_ine"]:
            return data["municipio_nombre"]
    return None

#! (EXPLICACIÓN EN VIDEO WHATSAPP)
# def get_town_by_ine2(dataset, ine_code):  
#     for data in dataset:
#         a = filter(lambda ine_code: ine_code == data["municipio_codigo_ine"],dataset)
#     return (list(a))

def get_biggest_town(dataset): #superficie_km2
    '''
    * Ejercicio 3: Obtener el municipio más grande
    '''
    biggest_surface = 0
    for data in dataset:
        if data["superficie_km2"] > biggest_surface:
            biggest_surface = data["superficie_km2"]
    return f'{biggest_surface:.2f}'

def get_biggest_town2(dataset):
    '''
    * Ejercicio 3: Obtener el municipio más grande
    '''
    surfaces = []
    for data in dataset:
        surfaces.append(data["superficie_km2"])
    return f'{max(surfaces):.2f}'

def top10_biggest_density(dataset):
    '''
    * Ejercicio 4: Obtener los 10 municipios con mayor densidad poblacional
    '''
    densities = []
    for data in dataset:
        densities.append(data['densidad_por_km2'])
    densities.sort()
    return densities[-10:]

def get_sorted_density_lists(dataset):
    '''* Ejercicio Bonus: Crea una función que reciba como parametro el dataset y devuelva tres listas con la siguiente condición:
	* la lista 1 tendrá todos los valores de densidad que empiecen por 1
	* la lista 2 tendrá todos los valores de densidad que empiecen por 2
	ej:
	lista_1 = ["134324", "1354211", "1349.34"]
    * qué porcentaje supone cada una de las listas
    '''
    list_1, list_2, list_3 = [],[],[]
    total_datas = len(dataset)
    for data in dataset:
        first_digit = str(data['densidad_por_km2'])[0]
        if first_digit == '1':
            list_1.append(data['densidad_por_km2'])
        elif first_digit == '2':
            list_2.append(data['densidad_por_km2'])
        elif first_digit == '3':
            list_3.append(data['densidad_por_km2'])
    percentage_1 = str(f'{(len(list_1)*100/total_datas):.2f}')+'%'
    percentage_2 = str(f'{(len(list_2)*100/total_datas):.2f}')+'%'
    percentage_3 = str(f'{(len(list_3)*100/total_datas):.2f}')+'%'
    return [{'percentage':percentage_1,'list':list_1},{'percentage':percentage_2,'list':list_2},{'percentage':percentage_3,'list':list_3}]

def load_json(dataset):
    '''
    * Ejercicio 9: Crear una función que acepte como parámetro toda la lista de diccionarios 
    y devuelva una lista de objetos
    '''
    obj_list = []
    for data in dataset:
        obj_list.append(Municipality(data["municipio_nombre"],data['densidad_por_km2'],data["superficie_km2"]))
    return obj_list

def download_csv(municipalities_list):
    f = open('./data/backup.csv','w')
    for municipality in municipalities_list:
        f.write(f'{municipality.name},{municipality.density},{municipality.surface},{municipality.total_population}\n')
    f.close()
        
def download_csv2(municipalities_list):
    with open('./data/backup.csv','w',newline='') as f:
        file_to_write = csv.writer(f)
        for municipality in municipalities_list:
            file_to_write.writerow([municipality.name,municipality.density,municipality.surface,municipality.total_population])

def main():
    
    #! Usando os.path
    # import os.path

    # pwd = os.path.dirname(os.path.realpath(__file__))
    # o = open(f'{pwd}/lab\data/data.json')

    #! Usando Path (pathlib)
    current_file_path = Path.cwd()
    o = open(current_file_path/"data/data.json")

    dataset = json.load(o)
    dataset = dataset["data"]

    print(f'\nLa densidad media de la comunidad de Madrid: {density_average(dataset)}')
    
    print(f'\nEl municipio con ine = 280468 se llama: {get_town_by_ine(dataset,"280468")}')
    print(f'El municipio con ine = 280493 se llama: {get_town_by_ine(dataset,"280493")}')
    
    print(f'\nEl municipio mas grande de la comunidad de Madrid (funcion1): {get_biggest_town(dataset)}')   #| 2 funciones diferentes
    print(f'El municipio mas grande de la comunidad de Madrid (funcion2): {get_biggest_town2(dataset)}')  #| para hacer lo mismo
    
    
    print(f'\nLas 10 mayores densidades de poblaciones de la comunidad de Madrid: {top10_biggest_density(dataset)}')
    
    densities_dict = get_sorted_density_lists(dataset)
    cont = 1
    for portion in densities_dict:
        print(f'\nDensities by {cont}: {portion["percentage"]}\n{portion["list"]}')
        cont += 1

    municipalities_list_madrid = load_json(dataset) # LISTA de instancias Municipality de toda la comunidad de Madrid
    
    '''
    * Ejercicio 11: Ya que tenemos una lista con todos los objetos, con su método "get_total_density()" 
    obtener la densidad total de la comunidad de Madrid
    '''
    madrid_total_density = 0
    for municipality in municipalities_list_madrid:
        madrid_total_density += municipality.total_population
    print(f'\nPoblación total de la comunidad de Madrid: {madrid_total_density}')
    
    cadena = "test-3.54-23.86"
    obj_from_string = Municipality.from_str(cadena)
    print(f'\nNuevo instancia de Municipality creada a partir de una cadena: \n{obj_from_string}')
    
    obj_from_string.apply_year_growth_rate()
    print(Municipality.total_comunity_population)
    o.close()
    
    '''
    * Ejercicio 20: Crear un backup de todos nuestros objetos en un fichero tipo CSV
    '''
    download_csv(municipalities_list_madrid)

#! ~~~~~~~~~~~~~~~~~~~~~~~~~~~ FIN FUNCIONES ~~~~~~~~~~~~~~~~~~~~~~~~~~~

main()

