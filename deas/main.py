import requests as req
from pathlib import Path
import json, os, sys
from dea import Dea
from user import User



data_uri = "https://datos.comunidad.madrid/catalogo/dataset/35609dd5-9430-4d2e-8198-3eeb277e5282/resource/c38446ec-ace1-4d22-942f-5cc4979d19ed/download/desfibriladores_externos_fuera_ambito_sanitario.json"
my_data_path = Path('./deas/data')
postalcodes_inside_m30 = ["28029", "28036", "28046", "28039", "28016", "28020", "28002", "28003", "28015", "28010", "28006", "28028", "28008", "28004", "28001", "280013", "28014", "28009", "28007", "28012", "28005", "28045"]
backup_path = Path('./deas/data/users_backup.json')

def get_deas_data():
    
    # response = req.get(data_uri).json()
    # with open(my_data_path / 'deas.json', 'w', encoding= "utf8") as json_file:
    #     json.dump(response['data'], json_file, ensure_ascii = False)
        
    with open(my_data_path / 'deas.json', 'r', encoding="utf8") as file:
        return json.load(file)    

def users_backup(uploaded_list):
    with open(backup_path, 'w', encoding="utf8") as file:
        json.dump(uploaded_list, file, ensure_ascii = False)
    
def downdload_users_backup():
    if backup_path.is_file():
        with open(backup_path, 'r', encoding="utf8") as file:
            return json.load(file)
    else:
        return None

def n_deas(datafile):
    return len(datafile)

def sample_by_postalcodes(postalcodes,datafile):
    for dea in datafile:
        yield dea if dea["direccion_codigo_postal"] in postalcodes else None
        
def samples_by_ownership(datafile):
    for ownership in sorted(set(list(map(lambda deas: deas["tipo_titularidad"], data)))):
        yield list(filter(lambda dea: dea["tipo_titularidad"] == ownership,datafile))
        
def create_user():
    name = input("\nNombre: ")
    password = input("\nPassword: ")
    return User(name, password)

def create_dea(deafile):
    address = deafile["direccion_via_codigo"]+' '+deafile["direccion_via_nombre"]+' '+deafile["direccion_portal_numero"]+'\n'+deafile["direccion_ubicacion"]+'\n'+deafile["direccion_codigo_postal"]
    return Dea(deafile["direccion_coordenada_x"],deafile["direccion_coordenada_y"],deafile["codigo_dea"], address)

def to_access():
    name = input("\nNombre: ")
    password = input("\nPassword: ")
    users = downdload_users_backup()
    if users != None:
        for user in users["data"]:
            if user["name"] == name and user["password"] == password:
                return True
        print("\nEl usuario y la contraseña no coinciden.")
        return False
    
def deas_menu():
    options = ["1 - Buscar DEA por código","2 - Buscar DEA por distancia","3 - Atras"]
    [print(option) for option in options]
    opt = input("\nOpcion: ")
    while not opt in ("123"):
        opt = input("\nOpcion incorrecta. Vuelva a introducir una opcion (1,2 o 3): ")
    return opt

def dea_by_code(datafile):
    code = input("\nCodigo del DEA: ")
    for dea in datafile:
        if dea["codigo_dea"] == code:
            return dea 
    return None

def dea_by_distance(datafile):
    x_user = float(input("\nSu posición x: "))
    y_user = float(input("Su posición y: "))
    dea = None
    distance = 100000
    for deafile in datafile:
        aux_dea = create_dea(deafile)
        aux_distance = aux_dea.get_distance(x_user, y_user)
        if aux_distance < distance: 
            distance = aux_distance
            dea = deafile
    return dea

def menu():
    options = ["1 - Crear usuario","2 - Acceder","3 - Admins","4 - Salir"]
    [print(option) for option in options]
    opt = input("\nOpcion: ")
    while not opt in ("1234"):
        opt = input("\nOpcion incorrecta. Vuelva a introducir una opcion (1,2,3 o 4): ")
    return opt

def main():
    
    data = get_deas_data()  
    users = downdload_users_backup() 
    os.system('cls')
    opt = menu()
    
    while opt != "4": 
        #? NEW USER    
        if opt == "1":
            user = create_user()
            if users != None:
                users["data"].append({"name":user.name,"password":user.password})
            else:
                users = {"data":[{"name":user.name,"password":user.password}]}
        #? TO ACCES 
        if opt == "2":
            cont = 1
            permission = to_access()
            while not permission and not cont == 3:
                print(f"Quedan {3-cont} intentos.")
                cont += 1
                permission = to_access()
            #? PERMITED USER
            if permission:
                os.system("cls")
                opt = deas_menu()
                #? DEA BY CODE
                if opt == "1":
                    deafile = dea_by_code(data)
                    print(create_dea(deafile).address) if deafile != None else print("\nDEA no encontrado")
                #? DEA BY DISTANCE    
                elif opt == "2":
                    nearest_dea = dea_by_distance(data)
                    print(nearest_dea)
                
                
        #?Pruebas con el json de deas
        # print(f"\nNº total de DEAS en la comunidad de Madrid: {n_deas(data)}")            
        # deas_inside_m30 = filter(lambda dea: dea != None, list(sample_by_postalcodes(postalcodes_inside_m30,data)))
        # print(f"\nNº total de DEAS dentro de la M-30: {n_deas(list(deas_inside_m30))}")
        # deas_by_ownership = list(samples_by_ownership(data)) #lista de listas. La primera son los deas privados y la segunda los deas publicos
        # print(f"\n{deas_by_ownership[0][0]['tipo_titularidad']}: {len(deas_by_ownership[0])}\n{deas_by_ownership[1][0]['tipo_titularidad']}: {len(deas_by_ownership[1])}")

        input("\nPulsa ENTER para continuar")  
        os.system('cls')
        opt = menu()
        
    users_backup(users)


main()

sys.exit()
