"""
3.	Algoritmo recursivo para determinar si un número n esta ordenado con respecto a sus dígitos.
    Ej.: n = 1258, res = true
"""
def esta_ordenado(n):
    n = abs(n)
    if n < 10:
        return True
    ultimo = n % 10
    penultimo = (n // 10) % 10
    if penultimo > ultimo:
        return False
    return esta_ordenado(n // 10)
n = int(input("Ingrese un número: "))
if esta_ordenado(n):
    print(f"{n} está ordenado con respecto a sus dígitos.")
else:
    print(f"{n} NO está ordenado con respecto a sus dígitos.")