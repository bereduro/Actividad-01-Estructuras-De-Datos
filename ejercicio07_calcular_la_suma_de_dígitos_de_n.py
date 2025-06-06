"""
7.	Algoritmo recursivo para calcular la suma de dígitos de n.
    Ej.: 1234 -> 1 + 2 + 3 + 4 = 10
"""
def suma_digitos(n):
    if n < 10:
        return n
    else:
        return n % 10 + suma_digitos(n // 10)
n = int(input("Ingrese un número para calcular la suma de sus dígitos: "))
resultado = suma_digitos(n)
print(f"La suma de los dígitos de {n} es: {resultado}")