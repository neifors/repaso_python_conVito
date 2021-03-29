from tqdm import tqdm, trange
import time, accumulate

for num in tqdm(range(100)):
    time.sleep(0.01)


# # Declara una barra de progreso con trange() que es equivalente a
# # tqdm(range()) del ejemplo anterior

for num in trange(100):
    time.sleep(0.01)


# Declara una barra de progreso tqdm utilizando una lista,
# correspondiéndose en este caso el número de ciclos con el 
# número de elementos de la lista.

texto = ""
for caracter in tqdm(["a", "b", "c", "d"]):
    texto = texto + caracter


# Declara una barra de progreso tqdm con una lista y
# se establece una descripción para mostrar el elemento
# en curso a la izquierda de la barra.

# barra1 = tqdm(["a", "b", "c", "d"])
# for caracter in barra1:
#     barra1.set_description("Procesando %s" % caracter)
#     time.sleep(0.5)


# # Declara una barra de progreso tqdm para un bucle de
# # 100 ciclos que se actualiza cada 10 ciclos.
# # El carácter utilizado para construir la barra es '#'
# # y lo establece el atributo ascii con el valor True.

# with tqdm(total=100, ascii=True) as barra2:
#     for num in range(10):
#         barra2.update(10)
#         time.sleep(0.5)


# # Declara una barra de progreso tqdm en un bucle para
# # recorrer y acumular con accumulate() los valores de una lista

# from itertools import *
# barra3 = tqdm(accumulate([0, 1, 2, 3, 4, 5]))
# for acumulado in barra3:
#     barra3.set_description("Acumulado %i" % acumulado)
#     time.sleep(0.5)


# # Declara una barra de progreso tqdm en un bucle para
# # recorrer y acumular con accumulate() los valores de una lista.
# # En ese ejemplo el atributo disable se establece con el valor
# # True para no mostrar la barra de progreso

# desactivado = True
# barra4 = tqdm(accumulate(0, 1, 2, 3, 4, 5), disable=desactivado)
# for acumulado in barra4:
#     barra4.set_description("Acumulado %i" % acumulado)
#     if desactivado:
#         print(acumulado, end=' ')
#     time.sleep(0.5)
