#coding: utf-8
numero = int(input("Escriba un número entero mayor que 1: "))
while numero <= 1:
    numero = int(input(str(numero) + " no es mayor que 1. Inténtelo de nuevo: "))
copia = numero

print("Descomposición en factores primos: ", end="")
i = 2
while copia > i:
    while copia % i == 0:
        copia = copia // i
        print(i, end=" ")
    i += 1
print(copia)

print()
print("Programa terminado")
