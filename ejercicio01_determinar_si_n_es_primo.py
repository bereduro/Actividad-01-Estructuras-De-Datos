"""
 1.	Algoritmo recursivo para determinar si n es primo.
    Ej.: 7 es primo, 8 no es primo
"""
def es_primo(n, divisor=2):
    if n < 2:
        return False
    if divisor * divisor > n:
        return True
    if n % divisor == 0:
        return False
    return es_primo(n, divisor + 1)
n = int(input("Ingrese un número para verificar si es primo: "))
if es_primo(n):
    print(f"{n} es un número primo")
else:
    print(f"{n} no es un número primo")