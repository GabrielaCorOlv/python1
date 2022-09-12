# Databricks notebook source
# Librerías
!pip install numpy
import numpy as np

# COMMAND ----------

# MAGIC %md #Inciso A
# MAGIC 1.- Crear una matriz 3x3 con valores de 0 a 8

# COMMAND ----------

# Crear matriz 3x3 con valores de 0 a 8
np.arange(0,9).reshape(3,3)

# COMMAND ----------

# MAGIC %md #Inciso B
# MAGIC 2.- Crear una matriz identidad de 6x6

# COMMAND ----------

# Crear matriz identidad de 6x6
np.identity(6)
