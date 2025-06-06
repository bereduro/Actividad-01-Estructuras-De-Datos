"""
11.	Algoritmo recursivo para determinar si dos números son amigos.
    Ej.: 220 y 284 son números amigos
"""
def suma_divisores(n, i=1):
    if i == n:
        return 0
    if n % i == 0:
        return i + suma_divisores(n, i + 1)
    else:
        return suma_divisores(n, i + 1)
def son_amigos(a, b):
    return suma_divisores(a) == b and suma_divisores(b) == a
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
if son_amigos(a, b):
    print(f"{a} y {b} son números amigos.")
else:
    print(f"{a} y {b} no son números amigos.")