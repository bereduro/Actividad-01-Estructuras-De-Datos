"""
5.	Algoritmo recursivo para calcular la suma de los factores primos de N.
    Ej.: N=12, res=2+2+3=7
"""
def suma_factores_primos(n, divisor=2):
    if n == 1:
        return 0
    if n % divisor == 0:
        return divisor + suma_factores_primos(n // divisor, divisor)
    else:
        return suma_factores_primos(n, divisor + 1)
N = int(input("Ingrese un número para calcular la suma de sus factores primos: "))
res = suma_factores_primos(N)
print(f"La suma de los factores primos de {N} es: {res}")