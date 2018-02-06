#coding: utf-8
num=input("Escriba un numero par:")
num_int=1
while num%2!=0:
	print "El numero introducido no es par."
	num=input("Introduzca un numero par:")

q=raw_input("Quiere escribir otro numero par? S/N:")

while  (num%2==0) and ((q=="S") or (q=="s")):
	num=input("Introduzca un numero par:")
	while num%2!=0:
		print "El numero introducido no es par."
		num=input("Introduzca un numero par:")
	num_int=num_int+1
	q=raw_input("Quiere escribir otro numero par? S/N:")

print "Has introducido "+str(num_int)+" pares."
print "Programa terminado."
