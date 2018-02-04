#coding: utf-8
x=float(input("introduce un numero:"))
suma=0
cont=0
while (x<=0):
	x=float(input("Error, introduce otro:"))
while (x>cont):		
	aux=float(input("introduce otro numero:"))
	if aux>0:
		cont+=x
		suma=suma+aux
	else:
		cont+=0
	if suma>=x:
		print "La suma de los numeros introducidos supera",x,"y es",suma
print "Programa terminado"
