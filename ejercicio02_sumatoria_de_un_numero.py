"""
2.	Algoritmo recursivo para calcular la sumatoria de un número.
    Ej.: n= 5, suma = 1+2+3+4+5 = 15
"""
def sumatoria(n):
    if n <= 1:
        return n
    else:
        return n + sumatoria(n - 1)
n = int(input("Ingrese un número para calcular su sumatoria: "))
print(f"La sumatoria de {n} es {sumatoria(n)}")
