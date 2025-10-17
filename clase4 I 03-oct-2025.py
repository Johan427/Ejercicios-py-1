#Alumno: Johan Sebastian Beleño Toloza

n1=int(input("digite el 1mer numero"))
n2=int(input("digite el 1mer numero"))
r=n1+n2
r2=n1-n2
r3=n1*n2
r4=n1/n2
print(n1,"+",n2,"=",r)
print(n1,"-",n2,"=",r2)
print(n1,"*",n2,"=",r3)
print(n1,"/",n2,"=",r4)

########################################

#raiz al cuadrado#
import math
ra2=float(input("digite el numero"))
r2=math.sqrt(ra2)
print("La raiz cuadrada de:",ra2,"es",r2)

######################################
#precio de vnta de un articulo (calcular y mostrar) pv=120% utilodad y 15%de impuesto
ppr=float(input("ingrese el precio de compra"))
pv=ppr+(ppr*1.20) # utilidad (120%)
im=pv+(pv*0.15) #precio de venta con impuesto (15%)
print("precio de venta es:",im)

#######################################
#listas
num=[1,2,3,4,5];
#alfanumerico#
datos=["hola",42,"mundo",3.14];

lista=["A","B","C","D","E"] #listas empiezan desde cero (primer elemento) (n-1)

#accediendo al primer elemento
primer_elemento=lista[0]
print(primer_elemento)

#accediendo al segundo elemento
segundo_elemento=lista[1]
print(segundo_elemento)

#accediendo al tercer elemento
tercer_elemento=lista[2]
print(tercer_elemento)

#accediendo al cuarto elemento
cuatro_elemento=lista[3]
print(cuatro_elemento)

#accediendo al quinto elemento
quinto_elemento=lista[4]
print(quinto_elemento)

#len, para obtener los numweros de la lista
num_elementos=len(lista)
print("número de elementos en la lista",num_elementos)

print("-----------------------------")

#calcular el indice
indice=2+1;

#accedemos al elemento usando el indice calculando dinámicamente
elemento=lista[indice]
print("elemento en el indice",indice,"es",elemento)

print("-----------------------------")

#cambiar elementos

#cambiamos el elemento en el indice 2 (3er elemento) por x
lista[2]="x"

#imprimir la lista actualizada
print("lista actualizada (cambiando el incice dos):",lista)

#desenpaquetar elemento
lista2=["a","b","c"]
#desempaquetamos los elementos de la lista en variables individuales
variable1,variable2,variable3=lista2
#imprimimos las variables
print("variable 1:",variable1)
print("variable 2:",variable2)
print("variable 3:",variable3)

print("-----------------------------")
#agregar elementos a una lista
#definimos lista
datos2=["Juan",25,"Ingeniero"]
#desenpaquetamos
nombre,edad,profesion=datos2
#imprimimos la info
print("nombre:",nombre)
print("edad:",edad)
print("profesion:",profesion)
