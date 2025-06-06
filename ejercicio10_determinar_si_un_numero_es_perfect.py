"""
10.	Algoritmo recursivo para determinar si un número es perfecto.
    Ej.: N = 28  -> res = true
"""
def es_perfecto(n, divisor=1, suma=0):
    if divisor == n:
        return suma == n
    if n % divisor == 0:
        suma += divisor
    return es_perfecto(n, divisor + 1, suma)
n = int(input("Ingrese un número para verificar si es perfecto: "))
if es_perfecto(n):
    print(f"{n} es un número perfecto")
else:
    print(f"{n} no es un número perfecto")
# un número perfecto es aquel que es igual a la suma de sus divisores propios
# ejemplo, 28 es perfecto porque 1 + 2 + 4 + 7 + 14 = 28