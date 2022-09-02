# Databricks notebook source
# MAGIC %md ##Actividad 1- tuplas

# COMMAND ----------

# Inciso 1
tupla = (["gaby",2001], True, 1, 6, 8)
tupla

# COMMAND ----------

# Inciso 2
lista = list(tupla)
lista

# COMMAND ----------

# Inciso 3
diccionario = {}
for i in range(5):
  diccionario[i+1] = lista[i]

diccionario
