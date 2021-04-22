from functools import reduce
from math import sqrt


y = [3,7,30]

print(list(map(lambda a: a+10, y)))
print(list(filter(lambda x: x%2 == 0,y)))
print(reduce(lambda a,b: a+b, y))

#? EJEMPLO

values = [1,2,3]
def pow(a):
    return a**2

print(list(map(pow,values)))

##* map va a coger cada uno de los elementos del iterable y lo pasa por la función por defecto.
## Convertimos a list para obtener un iterable de los resultados

new_values = [2,4,6,8]

results = list(map(pow,new_values))
print(results)

#? Calcular raiz cuadrada de los elementos de un iterable

#! With MAP

numbers = [4,81,144]
print(list(map(sqrt,numbers)))

#! With lambda

f = lambda elem: sqrt(elem)
print([f(elem) for elem in numbers])

## x = [2,4,24]
## y = [3,7,30]
## print(sum(map(lambda a, b: a * b, x, y)))

sample = [{"num_inscripciones": "3"},{"num_inscripciones": "4"},{"num_inscripciones": "1"}]

print([sum(int(num["num_inscripciones"]) for num in sample)] )

# def add(a,b):
#     return int(a["num_inscripciones"])+int(b["num_inscripciones"])

print(list(filter(lambda element: int(element['num_inscripciones']) if element['num_inscripciones']>"2" else None, sample)))