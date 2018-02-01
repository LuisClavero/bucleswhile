#coding: utf-8
x=input("introduce un numero")
cont=0
suma=0
while (cont<x):
    aux=input("introduce otro numero")
    if aux>0:
        cont+=1
        suma=suma+aux
	if suma>=x:
            print "Programa terminado"
