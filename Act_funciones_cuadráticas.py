# Databricks notebook source
# Librerías 
from math import sqrt
import cmath

# COMMAND ----------

# MAGIC %md #Básico 
# MAGIC Crea una función en la cual recibas como argumentos los parámetros reales de una función cuadrática, y te regrese x1 y x2.

# COMMAND ----------

def chicharronera(a,b,c):
    if((b**2)-4*a*c) < 0:
        print("La solución va a ser compleja, ve al inciso avanzado.")
    else: 
        x1 = (-b+sqrt(b**2-(4*a*c)))/(2*a)
        x2 = (-b-sqrt(b**2-(4*a*c)))/(2*a)
        print("El valor de x1 es: + {0} \nEl valor de x2 es: {1}".format(x1,x2))
    
#chicharronera(17,40,24)
chicharronera(1,3,-3)

# COMMAND ----------

# MAGIC %md #Avanzado
# MAGIC Crea una función en la cual recibas como argumentos los parámetros reales e imaginarios de una función cuadrática, y te regrese x1 y x2.
# MAGIC En caso de obtener valores imaginarios, imprime valores de la constante real x la constante imaginaria (2xi).

# COMMAND ----------

def chichcompleja(a,b,c):
    if((b**2)-4*a*c) < 0:
        print("La solución será compleja")
        x1c = (-b+cmath.sqrt(b**2-(4*a*c)))/(2*a)
        x2c = (-b-cmath.sqrt(b**2-(4*a*c)))/(2*a)
        print("Los valores comlejos de x1 es: + {0} \nY e x2 x2 es: {1}".format(x1c,x2c))
    else: 
        x1 = (-b+sqrt(b**2-(4*a*c)))/(2*a)
        x2 = (-b-sqrt(b**2-(4*a*c)))/(2*a)
        print("El valor de x1 es: + {0} \nEl valor de x2 es: {1}".format(x1,x2))
    
chichcompleja(17,40,24)
#chichcompleja(1,3,-3)
