# Databricks notebook source
# MAGIC %md #Arrange, arrey, apend, sort

# COMMAND ----------

!pip install numpy
import numpy as np

# COMMAND ----------

# Crear arreglo del 3 hasta los años que tengo
year =np.arange(3, 22)
year

# COMMAND ----------

# arreglo 
ar = np.array([1,2,3,4,0,1,2,3,4])
ar

# COMMAND ----------

# Juntar ambos arreglos
jun = np.append(year,ar)
jun

# COMMAND ----------

# Ordenar de menos a más
ar_sort = np.sort(jun)
ar_sort

# COMMAND ----------

# MAGIC %md #Arreglos llenos y vacíos

# COMMAND ----------

# Crear matriz 3x3 con valores de 0 a 8
np.arange(0,9).reshape(3,3)

# COMMAND ----------

# Crear matriz identidad de 6x6
np.identity(6)
