# Databricks notebook source
# MAGIC %md # Básica
# MAGIC Programa que determina si eres mayor de edad o no

# COMMAND ----------

#dbutils.widgets.text("Edad", "")

#dbutils.widgets.remove("Edad")

edad = dbutils.widgets.get("Edad")

# COMMAND ----------

# edad = int(input("Dime tu edad: "))

edad = int(edad)

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# COMMAND ----------

# MAGIC %md #Avanzada
# MAGIC Programa que determina si eres mayor o no de edad y determina tu género

# COMMAND ----------

# Avanzada
diccionario = {'Gaby':'femenino', 'Elena':'femenino', 'Antonio':'masculino', 'Rodrigo':'Masculino'}

#años = 45
#nombre = 'Mateo'
#gen_usuario = 'masculino'

años = 12
nombre = 'Gaby'
gen_usuario = 'femenino'

if edad > 18:
    r = 'mayor edad'
else:
    r = "menor edad"
    
if nombre in diccionario.keys():
    genero = diccionario[nombre]
else:
    genero = "no se puede saber"
    diccionario[nombre] = gen_usuario
    
print(f'Hola {nombre}, eres {r} y tu género {genero}')
