# Databricks notebook source
# MAGIC %md #Actividad salarios

# COMMAND ----------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
path='/dbfs/mnt/dpo/AI_Factory/MonterreyDigitalHub/Modulo 14 - Salarios/2022_qna16_remuneraciones.csv'
df = pd.read_csv(path)
df.head()

# COMMAND ----------

# MAGIC %md ## Actividad Básica
# MAGIC 
# MAGIC Obtener la diferencia entre el salario más alto y el más bajo.

# COMMAND ----------

# Borrar nombres nulos 
indexes = df[df['NOMBRE'].isnull()].index #Elimino nulos de 'medal'
df = df.drop(index = indexes, inplace= False, axis = 0) #Respetar index 

# COMMAND ----------

# Crear columna con nombre completo
NombreC = df['NOMBRE']+" "+ df["APELLIDO_1"]+ " "+ df["APELLIDO_2"]
NombreC = pd.DataFrame(NombreC)

# COMMAND ----------

# Juntar DataFrames
comp = pd.concat([NombreC, df], axis=1)
# Renombrar 1 columna
comp.rename(columns = {0:'NombreC'}, inplace = True)
comp.display()

# COMMAND ----------

# Borrar nombresC nulos 
indexes = comp[comp['NombreC'].isnull()].index #Elimino nulos de 'medal'
comp = comp.drop(index = indexes, inplace= False, axis = 0) #Respetar index 

# COMMAND ----------

# Obtener sueldo max con info
SueldoNetoMax = comp.loc[df["SUELDO_TABULAR_NETO"] == comp["SUELDO_TABULAR_NETO"].max()]

# Obtener sueldo min con info
SueldoNetoMin = comp.loc[df["SUELDO_TABULAR_NETO"] == comp["SUELDO_TABULAR_NETO"].min()]
SueldoNetoMin = SueldoNetoMin.head(1)

# COMMAND ----------

# Sueldo min a 
min = SueldoNetoMin['SUELDO_TABULAR_NETO'].to_string(index=False)
min = float(min)

# COMMAND ----------

# Sueldo max en float
max = SueldoNetoMax['SUELDO_TABULAR_NETO'].to_string(index=False)
max = float(max)

# COMMAND ----------

print("El sueldo tabular neto más alto en el gobierno de la CDMX es de:", SueldoNetoMax['NombreC'].to_string(index=False))
print("Tiene el puesto de:", SueldoNetoMax['N_PUESTO'].to_string(index=False))
print("Con salario tabular neto de:", SueldoNetoMax['SUELDO_TABULAR_NETO'].to_string(index=False), "\n", "\n")

print("El sueldo tabular neto más bajo en el gobierno de la CDMX es de:", SueldoNetoMin['NombreC'].to_string(index=False))
print("Tiene el puesto de:", SueldoNetoMin['N_PUESTO'].to_string(index=False))
print("Con salario tabular neto de:", SueldoNetoMin['SUELDO_TABULAR_NETO'].to_string(index=False), "\n", "\n")

print("La diferencia entr4e sueldos es de:", max - min, "pesos.")

# COMMAND ----------

# MAGIC %md ##Actividad Avanzada
# MAGIC 
# MAGIC Obtener los estadísticos descriptivos de los salarios. (media, mediana, desviación estándar, etc..

# COMMAND ----------

df.describe()
