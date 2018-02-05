#coding: utf-8
minimo=input("Escriba un mínimo:")
maximo=input("Escriba un máximo:")
suma=0
cont=0
while minimo>maximo:
	minimo=input("Error, introduzca otro numero mínimo:")
	maximo=input("Escriba otro numero máximo:")
while minimo<maximo and suma==0:
	aux=input("Introduzca un numero:")
	if aux<=maximo and aux>=minimo:
		cont=cont+1
		suma=0
	else:
		suma=-1
print "Programa terminado."
print "La cantidad de numeros introducida entre",minimo,"y",maximo,"es:",cont

	
	

