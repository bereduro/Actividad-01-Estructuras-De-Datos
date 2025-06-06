"""
8.	Algoritmo recursivo para calcular la cantidad de bit unos que
    tiene un número al convertir de base 10 a base 2.
        Ej.: N = 5 -> B = 101 -> Res = 2.
"""
def contar_unos(n):
    if n == 0:
        return 0
    else:
        return (n % 2) + contar_unos(n // 2)
numero = int(input("Ingrese un número: "))
print(f"Cantidad de bits '1' en la representación binaria de {numero}: {contar_unos(numero)}")