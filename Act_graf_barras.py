# Databricks notebook source
# MAGIC %md #Actividad avanzada
# MAGIC Crea una gáfica de barras que represente a los 10 países con más medallas en orden de menor a mayor y que muestre sus valores.

# COMMAND ----------

# MAGIC %md ##Leer CSV desde Azure

# COMMAND ----------

import pandas as pd

# COMMAND ----------

#Leer de azure usando pandas
path = '/dbfs/mnt/dpo/AI_Factory/MonterreyDigitalHub/Modulo 12 - Actividad Competidores Olimpicos/athlete_events.csv'
data = pd.read_csv(path)
display(data)

# COMMAND ----------

# MAGIC %md ##Creación de filtro

# COMMAND ----------

# Comienzo por eliminar los valores vacíos de medallas
indexes = data[data['Medal'].isnull()].index #Elimino nulos de 'medal'
data = data.drop(index = indexes, inplace= False, axis = 0) #Respetar index 

# COMMAND ----------

# Paises con más medallas
top10 = data['NOC'].value_counts().head(10)
display(top10)

# COMMAND ----------

# MAGIC %md ##Gráfica de barras

# COMMAND ----------

# Países junto con las medallas top 10
pais10 = data[['NOC','Medal']] # ejes
pais10['NOC'].value_counts().head(10).sort_values(ascending = True).plot(kind = 'bar', figsize = (15,10))

# COMMAND ----------

# MAGIC %md ###Explicación clase

# COMMAND ----------

top10_medallas = data[["NOC","Year"]]
top10_medallas["NOC"].value_counts().head(10).plot(kind="bar", figsize=(15,10))
