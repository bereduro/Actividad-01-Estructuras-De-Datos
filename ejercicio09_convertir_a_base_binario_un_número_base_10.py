"""
9.	Algoritmo recursivo para convertir a base binario un número en base 10.
    Ej.: N = 12 - > Res = 1100
"""
def decimal_a_binario(n):
    if n < 2:
        return str(n)
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

n = int(input("Ingrese un número decimal para convertir a binario: "))
resultado = decimal_a_binario(n)
print(f"El número {n} en binario es: {resultado}")