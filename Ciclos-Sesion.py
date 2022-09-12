# Databricks notebook source
# MAGIC %md
# MAGIC # IF

# COMMAND ----------

a=5

# COMMAND ----------

if a==3:
    a=a*3
    print(a)

# COMMAND ----------

a=3

# COMMAND ----------

if a==3:
    a=a*3
    print(a)

# COMMAND ----------

a=1

# COMMAND ----------

if a==3:
    a=a*3
    print(a)
elif a>10:
    a%=2
    print(a)
else:
    print(a)

# COMMAND ----------

animal=["leon", "perro", "gato", "tigre", "toro", "murciélago"]

# COMMAND ----------

print("El primer animale es {0}, su longitud es {1}".format(animal[0],len(animal[0])))
#                                                           variable{0},variable{1}

# COMMAND ----------

edad1=10

# COMMAND ----------

if edad1>=18:
    print("Eres mayor de edad")
elif edad1<18:
    print("Eres menor de edad")

# COMMAND ----------

edad= int(input("Por favor, escriba su edad en números enteros"))
if edad>=18:
    print("Eres mayor de edad")
elif edad<18:
    print("Eres menor de edad")

# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------

a=float(input('Por favor, ingrese el primer número a comparar: '))
b=float(input('Por favor, ingrese el segundo número a comparar: '))
if a==b:
    print('Ambos números son iguales')
elif a>b:
    print('El primer número que es igual a {0} es mayor al segundo que es igual a {1}'.format(a,b))
elif a<b:
    print('El segundo número es mayor', b)

# COMMAND ----------

# MAGIC %md
# MAGIC # For

# COMMAND ----------

numeros=[1,2,3,4,5,6,7]

# COMMAND ----------

# numeros[0]
# numeros[1]

# COMMAND ----------

for i in numeros:
    print(i)

# COMMAND ----------

diccionario={"A":2,"B":3,"C":4}
for k in diccionario:
    print(k)

# COMMAND ----------

for v in diccionario.values():
    print(v)

# COMMAND ----------

# k es del diccionario como k y el v como valor
for k,v in diccionario.items():
    print("El key es: ",k,"\nEl valor es: ",v)

# COMMAND ----------

for e in range(0,20,2): #(Inicio,Fin-1,Paso o diferencia)
    print(e)

# COMMAND ----------

r=list(range(0,20,7))

# COMMAND ----------

r

# COMMAND ----------

numeros

# COMMAND ----------

for n in numeros:
    if n==5:
        break
    print(n)

# COMMAND ----------

for n in numeros:
    if n==5:
        continue
    print(n)

# COMMAND ----------

dict={"Miguel":18,"Edwin":23,"Erick":28,"Pedro":16,"Pau":25,"Liliana":20,"Marco":25,"Claudia":21,"Roland":25,"Gerardo":9,"Jonathan":15}

# COMMAND ----------

i=0
j=0
v=0
for i,j in dict.items():
    if j==v:
        v=j
    elif j<=v:
        pass
    elif j>=v:
        v=j
print('El valor máximo es ',d)

# COMMAND ----------

# MAGIC %md
# MAGIC # While

# COMMAND ----------

numero=int(input("Escribe un número positivo: "))
while numero<0:
    print("El número escrito no es positivo, intente de nuevo")
    numero=int(input("Escribe un número positivo: "))
print("Número positivo, gracias!")

# COMMAND ----------

numero_0=1
numero_1=0 #Resultado de suma
while numero_0 <=10:
    numero_1= numero_0 + numero_1
    numero_0= numero_0 + 1
print("La suma es " + str(numero_1))

# COMMAND ----------

numero_0

# COMMAND ----------

numero_1

# COMMAND ----------

total=0
conteo=0
print("Ingrese la nota del estudiante (-1 para salir):")
grado = float(input())
while grado !=-1:
    total= total+grado
    conteo = conteo + 1
    grado=float(input("Ingrese la nota del estudiante (-1 para salir):"))
promedio=total/conteo
print("El pomedio de las notas del estudiante es:" + str(promedio))

# COMMAND ----------


