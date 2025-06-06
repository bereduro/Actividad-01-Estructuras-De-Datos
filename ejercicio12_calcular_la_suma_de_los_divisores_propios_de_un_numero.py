"""
12.	Algoritmo recursivo para calcular la suma de los divisores propios de un número.
    Ej.: N = 12 -> div = 1 + 2 + 3 + 4 + 6  => sdp = 16
    (Los divisores propios son aquellos que dividen exactamente al número y son menores que él)
"""
def suma_divisores_propios(n, divisor=1):
    if divisor >= n:
        return 0
    if n % divisor == 0:
        return divisor + suma_divisores_propios(n, divisor + 1)
    else:
        return suma_divisores_propios(n, divisor + 1)
num = int(input("Ingrese un número: "))
resultado = suma_divisores_propios(num)
print(f"La suma de los divisores propios de {num} es: {resultado}")