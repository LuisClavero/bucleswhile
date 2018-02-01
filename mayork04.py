#coding: utf-8
pos=input("Escriba la cantidad numeros positivos a solicitar:")
cont=0
total=0
while (cont<pos):
	aux=input("Introduce un numero:")
	if aux>0:
		cont+=1
	total=total+1	
print "Has introducido",total,"numeros, de los cuales",pos,"son positivos"
