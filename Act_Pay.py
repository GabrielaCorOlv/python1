# Databricks notebook source
# MAGIC %md #Actividad avanzada
# MAGIC Crear y guardar una gráfica de pay del año más reciente existente en la base de datos.

# COMMAND ----------

# MAGIC %md ##Leer CSV desde Azure

# COMMAND ----------

import pandas as pd

# COMMAND ----------

#Leer de azure usando pyspark
path = '/dbfs/mnt/dpo/AI_Factory/MonterreyDigitalHub/Modulo 12 - Actividad Competidores Olimpicos/athlete_events.csv'
data = pd.read_csv(path)
display(data)

# COMMAND ----------

# MAGIC %md ##Creación de filtro

# COMMAND ----------

# Comienzo por eliminar los valores vacíos de medallas
indexes = data[data['Medal'].isnull()].index #Elimino nulos de 'medal'
data = data.drop(index = indexes, inplace= False, axis = 0) #Respetar index 
data

# COMMAND ----------

maxAños = data[data['Year'] == data['Year'].max()]
display(maxAños)

# COMMAND ----------

# MAGIC %md ##Gráfica Pay

# COMMAND ----------

pay = maxAños['NOC'].value_counts().head(15).plot(kind = 'pie')
