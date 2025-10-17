# ALUMNO Johan Sebastian Beleño Toloza

"""NOTA: es mejor ejecutar los ejecicios individualmente 
ya que algunos tienen variables con el mismo nombre y pueden ocacionar errores al ejecutar todos a la ves"""
import math

#1
print("Hola Mundo");

#2
name = input("Ingrese su nombre");
print(name);

#3

n1 = int( input("Ingrese el primer número para sumar"))
n2= int(input("Ingrese el segundo número para sumar"))
int=resultado= n1+ n2
print("La suma de: ",n1, "+ ", n2, "es: ",resultado)

#4
int=h=7;
int=b=5;
int=resultado=h*b/2;
print("base",b,"altuta",h)
print("El àrea del triángulo es: ",resultado);

#5
temp = int( input("Ingrese los grados celsius para convertir a fahrenheit: "));
int=resultado=(temp*(9/5)+32);
print("Los ",temp," celcius en fahrenheit es: ",resultado);

#6
num=int(input("Ingrese un número para saber si es par o impar"))
if num %2==0:
    print(num," es par")
else:
     print(num," es impar" )
        
#7
print("Ingrese datos para hallar el mayor de 3 números")
n1 = int( input("Ingrese el primer número"))
n2= int(input("Ingrese el segundo número"))
n3= int(input("Ingrese el tercer número"))
print("El número mayor es: ", max(n1,n2,n3))


#8
num = int( input("Ingrese un número para calcular su cuadrado: "))
cua=pow(num, 2)
print("El cuadrado de ",num," es: ",cua)

#9
num = int(input("Ingrese un número para hallar su tabla de multiplicar "))
for n in range(1, 11):
    r=(num*n);
    print(num, "*", n, "=", r)
    
#10
pal=(input("Ingrese una palabra para invertirla: "))
inver=pal[::-1]
print(inver)

#11
ana=int(input("Ingrese su año de nacimiento: "))
est=int(input("Ingrese el año actual: "))
int=edad=est-ana
if edad < 18:
    print("Su edad es de: ",edad, ", usted es menor de edad" )
else:
   print("Su edad es de: ",edad, ", usted es mayor de edad")
   
   #12
   
num=int(input("Ingrese un número para obtener su factorial: "))

if num<0:
    print("no se puede obtener con números negativos")
else:
    fac=1
    for f in range(1,num+1):
        fac*=f
print("El factorial de", num, " es: ", fac)

#13
print("Ingrese datos para hallar el promedio de 5 números")
n1 = int( input("Ingrese el primer número"))
n2= int(input("Ingrese el segundo número"))
n3= int(input("Ingrese el tercer número"))
n4= int(input("Ingrese el cuarto número"))
n5= int(input("Ingrese el  quinto número"))
prom=n1+n2+n3+n4+n5/5
print("El promedio es de: " ,prom)

#14
num= int( input("Ingrese un número para obtener los pares hasta ese: "))
for n in range (2,num+1,2):
    print(n)
    
 #15  
le= (input("Ingrese una letra para saber si es vocal o consonante "))
if le in ['a','e','i','o','u']:
    print(le, " Es una vocal" )
else:
    print(le, " es consonante" ) 
    
#17
num= int(input("Ingrese un número para ver si es o no primo "))
if num<2:
    print(num, " No es Numero primo")

    if num%i==0:
        print(num, " No es Numero primo")
else:
    for i in range(2,num):
        print(num, " Si es Numero primo")
        
  #18      
for n in range(1,101):
    if n%5==0:
        print(n) 
        
    #19 
pal= (input("Ingrese una palaBra para saber cuántas vocales tiene "))
count=0
for let in pal:
  if let in ['a','e','i','o','u']:
    count=count+1
print(pal," tiene ",count, " vocales")

#20
print("Calculadora +,-,*,/")
n1 = int( input("Ingrese el primer número"))
n2= int(input("Ingrese el segundo número"))

s=n1+n2
r=n1-n2
m=n1 * n2
d=n1/n2
if d==0:
    print("Indeterminado 0/0")
op=(input("Seleccione una opción: \n 1. suma\n 2. resta \n 3. multiplicación \n 4. divición \n 5. mostrar todas las operaciones" ))

if op==1:
    print(s)
if op==2:
    print(r)
if op==3:
    print(m)
if op==4:
    print(d)
if op==5:
 print("suma: ", s)
 print("resta: ",r)
 print("multiplación: ",m)
 print("division:", d)
 

#ejercicios 21 a 23, 25 y 30#
nums=[15,40,40,54,12,27,48,66,7,54]
print("lista: 15,40,40,54,12,27,48,66,7,54")
print("número mayor: ",max(nums))
orden=sorted(nums)
print("orden de menor a mayor: ",orden)
dup=list(set(nums))
print("sin duplicados: ",dup )
s= sum(nums)
print("La suma de la lista es: ",s)
sma=dup[-2]
print("segundo número mayor: ",sma)



# ejercicio 24#
nam=["juan","maria"  ,"ana", "stef", "steve", "ramon"]
print("orden original:",nam)
orden=sorted(nam)
print("Lista ordenada: ",orden )

#ejercicio 26#
l1=[1,2,3,4]
l2=[11,12,13,14]
l3=l1+l2
print ("lista 1:",l1 )
print ("lista 2: ",l2 )
print ("listas unidas :",l3 )

#27#
fr= (input("Ingresa una frase: "))
pal = fr.split()
cant = len(pal)

print("la frase:", fr,"\ntiene", cant, "palabras")

 
#28

pal = (input("Ingresa una palabra: "))
pal =pal.lower()

if pal == pal[::-1]:
    print(pal, "es un palíndromo")
else:
    print(pal, "NO ES un palíndromo")
  
#29
print("cuadrados de 1 a 10:")
for n in range(1, 11):
    cuad = pow(n,2)
    print(cuad)

    
