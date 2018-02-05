#coding: utf-8
limite= float(input("Escriba el valor límite:"))
suma=0
while limite<=0:
    limite=float(input("El límite debe ser mayor que 0. Inténtelo de nuevo:"))
while suma<limite:
    aux= float(input("Escriba otro número:"))
    suma=suma+aux
print "Ha superado el límite. La suma es:",suma
print "Programa terminado."
