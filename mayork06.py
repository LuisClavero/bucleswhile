#coding: utf-8
cont=0
suma=0
x=float(input("introduce un numero:"))
while (x<=0):
	x=float(input("Error, introduce otro:"))

else:		
	aux=float(input("introduce otro numero:"))
	if aux>0:
		suma=suma+aux
		if suma>=x:
			print "Programa terminado, la suma es igual o ha superado",x
