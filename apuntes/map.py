from math import sqrt


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
