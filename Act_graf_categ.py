# Databricks notebook source
# MAGIC %md # Actividad: Gráfica por Categoria
# MAGIC Crea / Presenta un algoritmo que genere los datos de "reading_score" y "math_score", en variables categóricas, y guárdalo en dos columnas diferentes (cada columna nueva representa la nueva columna con variables categórica).

# COMMAND ----------

import pandas as pd
import numpy as np

path = '/dbfs/mnt/dpo/AI_Factory/MonterreyDigitalHub/Modulo 17 - Alumnos por grado/clean_students_complete.csv'
alumnos = pd.read_csv(path)
display(alumnos)

# COMMAND ----------

# Elimino los id y math score ya que solo se analizará reading
alumnos1 = alumnos.drop(labels=['Unnamed: 0', 'Student ID'], axis=1)
display(alumnos1)

# COMMAND ----------


