"""
4.	Algoritmo recursivo para calcular la suma de los divisores de N.
    Ej.: N = 6 , res = 1+2+3+6 = 12
"""
def suma_divisores(n, divisor=1):
    if divisor > n:
        return 0
    if n % divisor == 0:
        return divisor + suma_divisores(n, divisor + 1)
    else:
        return suma_divisores(n, divisor + 1)
N = int(input("Introduce un número entero positivo N: "))
res = suma_divisores(N)
print(f"La suma de los divisores de {N} es {res}")