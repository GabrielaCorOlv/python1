# Databricks notebook source
# MAGIC %md #Actividad salarios

# COMMAND ----------

import pandas as pd

path = '/dbfs/mnt/dpo/AI_Factory/MonterreyDigitalHub/Modulo 17 - Alumnos por grado/clean_students_complete.csv'
df_alumnos = pd.read_csv(path)
display(df_alumnos)
