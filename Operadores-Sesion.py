# Databricks notebook source
# MAGIC %md
# MAGIC Práctica

# COMMAND ----------

i=4 #Entero

# COMMAND ----------

i**4 #Entero ; Mantiene el tipo de variable

# COMMAND ----------

i*=10 #Multiplica el valor almacenado en i por el escrito a la derecha del igual

# COMMAND ----------

i

# COMMAND ----------

i /=10 #Puede alterar el tipo de variable
i

# COMMAND ----------

i -= 1 #Mantiene el tipo de variable
i

# COMMAND ----------

i += 10 #Mantiene el tipo de variable
i

# COMMAND ----------

i //= 3
i

# COMMAND ----------

i%=3
i

# COMMAND ----------

contador=1

# COMMAND ----------

contador = contador + 1

# COMMAND ----------

contador

# COMMAND ----------

contador +=1
contador

# COMMAND ----------

# MAGIC %md
# MAGIC # Parte 2

# COMMAND ----------

1==2 #Evalúa una igualdad

# COMMAND ----------

1<2 #>, <, <=, >=

# COMMAND ----------

1!=2 #Evalúar una diferencia

# COMMAND ----------

cadena1, cadena2 = "Hola", "Adiós"
lista1, lista2 = [3,"Bienvenido",23], [True,"Gracias por su visita"]

# COMMAND ----------

c_cadenas= cadena1==cadena2

# COMMAND ----------

c_cadenas

# COMMAND ----------

c_listas= lista1==lista2
c_listas

# COMMAND ----------

a,b,c="Hola","Mundo"," "

# COMMAND ----------

a+c+b

# COMMAND ----------

a*3+c+b

# COMMAND ----------

d="Murciélago"
#  0123456789

# COMMAND ----------

d

# COMMAND ----------

ult_letras=d[6:10] 

# COMMAND ----------

ult_letras!=d

# COMMAND ----------

ult_letras==d

# COMMAND ----------

edad=24/2
print("Mi edad es", edad)

# COMMAND ----------

#1/3(x)-15=a
a=6
x=(a+15)/(1/3)
print("La edad de mi hermana es",x)

# COMMAND ----------

a>x

# COMMAND ----------

x>a

# COMMAND ----------

import numpy as np

# COMMAND ----------

a=np.array([1,2,3,4,5,6,7])
a

# COMMAND ----------

mascara = a>3
mascara

# COMMAND ----------

a

# COMMAND ----------


