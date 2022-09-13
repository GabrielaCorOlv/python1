# Databricks notebook source
# Esto sería con databricks, llega a ser más complicado por falta de interactividad

#dbutils.widgets.text("Cantidad", "")

#dbutils.widgets.remove("Cantidad")

#cantidad = dbutils.widgets.get("Cantidad")

# COMMAND ----------

# Link Colab
# https://colab.research.google.com/drive/15qm7OB9FX8jEHuzbIkead8hvnS_IWnV3?usp=sharing

# COMMAND ----------

import math

# COMMAND ----------

# MAGIC %md #Básica
# MAGIC Crear un programa que permita al usuario ingresar los montos de las compras de un cliente (se desconoce la cantidad de datos que se cargarán, que pueden cambiar en cada ejecución), cortando el ingreso de datos cuando el usuario ingresa el monto 0.
# MAGIC Si ingresa una cantidad negativa, no debe procesarse y se le debe solicitar que ingrese una nueva cantidad. Al finalizar, informar el total a pagar teniendo en cuenta que, si las ventas superan el total de $1000, se debe aplicar un 10% de descuento.

# COMMAND ----------

#Databricks
'''
suma = 0 
cantidad = int(cantidad)

while (cantidad !=0):
    if(cantidad < 0):
        print("La cantidad es negativa, por lo tanto no es una entrada válida")
    else:
        suma += cantidad
    cantidad = cantidad

if(suma > 1000):
    print("Suma total: " + str(suma))
    print("Con el 10% de descuento te queda en: " + str(suma*0.9))
else:
    print("Suma total: " + str(suma))
'''

# COMMAND ----------

# Colaboratory
suma = 0
cantidad = int(input("Ingresa la cantidad que desea: "))

while (cantidad != 0):
  if (cantidad <0):
    print("La cantidad no es válida por ser negativa.")
  else:
    suma += cantidad
  cantidad= int(input("Ingresa la cantidad que desea:"))

if (suma > 1000):
  print("Suma total: " + str(suma))
  print("Con el 10% de descuento te queda en: " + str(suma*0.9))
else:
  print("Suma total: "+ str(suma))

# COMMAND ----------

# MAGIC %md #Avanzada
# MAGIC Crear un programa que permita al usuario ingresar el tiempo dentro en un estacionamiento , cortando el ingreso de datos cuando el usuario ingresa 0 minutos.
# MAGIC Si ingresa una cantidad negativa, no debe procesarse y se le debe solicitar que ingrese una nueva cantidad.
# MAGIC Ingresar una tarifa fija durante la primera hora (60 minutos) de $25 y $15 por cada hora adicional. Al finalizar, informar el total a pagar teniendo en cuenta que, si el monto supera las 8 horas se aplica una tarifa fija de $200 extra. 

# COMMAND ----------

# Colaboratory
suma = 0 
costo = 0 
tiempo = int(input("Ingrese el tiempo de visita: "))

while (tiempo != 0):
  if(tiempo < 0): 
    print("Ingrese un tiempo válido, los negarivos no se pueden. ")
  else: 
    suma += tiempo
  tiempo = int(input("Ingrese el tiempo de visita: "))

if (suma > 60):
  suma -= 60
  temp = math.ceil(suma/60) * 15 #ceil() devuelve el entero mayor o igual más próximo a un número dado
  if(temp + 25 > 145):
    temp += 200
    print("El costo final es: " + str(temp + 25))
  else:
    print("El costo final es: "+ str(temp + 25))
elif(suma==0):
  print("Puede salir sin costo alguno.")
else: 
  print("El monto total a pagara es: " + str(25))
