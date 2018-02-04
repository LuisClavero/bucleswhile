#coding: utf-8
limite= float(input("Escriba el valor límite:"))
while limite<=0:
    limite=float(input("El límite debe ser mayor que 0. Inténtelo de nuevo:"))
x=float(input("Escriba un número:"))
suma=0
suma+=x
while suma<limite:
    x= float(input("Escriba otro número:"))
    suma+=x
print "Ha superado el límite. La suma de los números positivos introducidos es",str(suma)+"." 
print "Programa terminado."
