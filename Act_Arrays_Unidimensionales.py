# Databricks notebook source
# Librerías
!pip install numpy
import numpy as np

# COMMAND ----------

# MAGIC %md #Inciso A
# MAGIC 1.- Crea un vector con valores dentro del rango 3 a el número que representa tu edad.

# COMMAND ----------

# Crear arreglo del 3 hasta los años que tengo
year =np.arange(3, 22)
year

# COMMAND ----------

# MAGIC %md #Inciso B
# MAGIC 2.- Crea un arreglo con los siguientes elementos: [0, 1, 2, 3, 4, 0, 1, 2, 3, 4]

# COMMAND ----------

# arreglo 
ar = np.array([1,2,3,4,0,1,2,3,4])
ar

# COMMAND ----------

# MAGIC %md #Inciso C
# MAGIC 3.- Ordena de forma ascendiente dicho arreglo.

# COMMAND ----------

# Ordenar de menos a más
ar_sort = np.sort(ar)
ar_sort
