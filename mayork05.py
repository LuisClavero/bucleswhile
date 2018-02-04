#coding: utf-8
num1=int(input("Introduce un numero:"))
num2=0
while num1>0:
	num2+=num1
	num1=int(input("Introduce otro numero:"))	
print "La suma de los numeros positivos es:",str(num2)+"."
print "Programa terminado"
