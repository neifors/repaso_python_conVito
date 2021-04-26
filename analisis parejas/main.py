import requests as req
from pathlib import Path
import json
import statistics as std
from math import sqrt
from functools import reduce


data_path = 'https://datos.comunidad.madrid/catalogo/dataset/eb0c86dc-743d-4220-a53f-da43a8cbc955/resource/d12f9a6d-aa9c-404f-82a8-9dcaaffebc28/download/uniones_hecho_parejas.json'
# My dir to save data (.json)
my_path = Path('./analisis parejas/data')

# response = req.get(data_path).json()
# with open(my_path / 'parejas.json', 'w', encoding= "utf8") as json_file:
#     json.dump(response['data'], json_file, ensure_ascii = False)   

def first_sample(year,datafile):
    for couple in datafile:
        yield couple if couple["inscripcion_año"] <= year else None
        
def second_sample(year,datafile):
    for couple in datafile:
        yield couple if couple["inscripcion_año"] > year else None
        
def sample_by_year(year,datafile):
    for couple in datafile:
        yield couple if couple["inscripcion_año"] == year else None
            
def n_inscriptions(datafile, couple_type = "h"):
    for couple in datafile:
        yield int(couple["num_inscripciones"]) if couple and couple["pareja_tipo"].startswith(couple_type) else 0
            
def n_cancelations(datafile, couple_type = 'h'): 
    for couple in datafile:
        yield int(couple["num_inscripciones_cancelacion"]) if couple and couple["pareja_tipo"].startswith(couple_type) else 0
    
def p_inscriptions(datafile, couple_type):
    return sum(list(n_inscriptions(datafile,couple_type)))/sum(list(n_inscriptions(datafile))) if sum(list(n_inscriptions(datafile))) != 0 else 0

def p_cancelations(datafile, couple_type):
    return sum(list(n_cancelations(datafile,couple_type)))/sum(list(n_cancelations(datafile))) if sum(list(n_cancelations(datafile))) != 0 else 0

def annual_p_inscriptions(datafile, couple_type):
    for year in sorted(set(list(map(lambda couple: couple["inscripcion_año"], datafile)))):
        p_type_inscriptions = p_inscriptions( list(sample_by_year(year, datafile)), couple_type)
        p_total_inscriptions = p_inscriptions(list(sample_by_year(year, datafile)), "h")
        yield p_type_inscriptions/p_total_inscriptions if p_total_inscriptions != 0 else 0
        
def annual_p_cancelations(datafile, couple_type):
    for year in sorted(set(list(map(lambda couple: couple["inscripcion_año"], datafile)))):
        p_type_cancelations = p_cancelations( list(sample_by_year(year, datafile)), couple_type)
        p_total_cancelations = p_cancelations(list(sample_by_year(year, datafile)), "h")
        yield p_type_cancelations/p_total_cancelations if p_total_cancelations != 0 else 0
        
with open(my_path / 'parejas.json', 'r', encoding="utf8") as file:
    data = json.load(file)

    cut_year = "2010"
    
    
    