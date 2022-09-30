# Databricks notebook source
# MAGIC %md # Act: puntaje reading
# MAGIC Crea / Presenta la forma que creas más conveniente para describir cuántos alumnos por escuela tuvieron el mejor puntaje en "reading", y con ello saber que género es el que predomina en este filtro.
# MAGIC Crea / Presenta la forma que creas más conveniente para describir cuántos alumnos por escuela tuvieron el peor puntaje en "reading", y con ello saber que género es el que predomina en este filtro.

# COMMAND ----------

# MAGIC %md ###Librerías y lectura de datos

# COMMAND ----------

import pandas as pd
import numpy as np

path = '/dbfs/mnt/dpo/AI_Factory/MonterreyDigitalHub/Modulo 17 - Alumnos por grado/clean_students_complete.csv'
alumnos = pd.read_csv(path)
#display(alumnos)

# COMMAND ----------

# Elimino los id y math score ya que solo se analizará reading
alumnos1 = alumnos.drop(labels=['Unnamed: 0', 'Student ID', 'math_score'], axis=1)
display(alumnos1)

# COMMAND ----------

# Saber como se comparará
alumnos1['school_name'].unique()

# COMMAND ----------

keys = alumnos1["gender"].value_counts().keys()
pie = alumnos1["gender"].value_counts().plot.pie(figsize=(5,5), labels= keys, autopct="%0.2f %%")

# COMMAND ----------

# Obtener sueldo min con info
Max = alumnos1.loc[alumnos1["reading_score"] == alumnos1["reading_score"].max()]
Max = Max.head(10)
Max

# COMMAND ----------

keys = Max["gender"].value_counts().keys()
pie = Max["gender"].value_counts().plot.pie(figsize=(5,5), labels= keys, autopct="%0.2f %%")

# COMMAND ----------

# Obtener sueldo min con info
Min = alumnos1.loc[alumnos1["reading_score"] == alumnos1["reading_score"].min()]
Min = Min.head(10)
Min

# COMMAND ----------

keys = Min["gender"].value_counts().keys()
pie = Min["gender"].value_counts().plot.pie(figsize=(5,5), labels= keys, autopct="%0.2f %%")

# COMMAND ----------

# MAGIC %md #Act: puntaje reading 2
# MAGIC Crea / Presenta la forma que creas más conveniente para describir qué grado por escuela tuvo el mejor puntaje en "reading" y con ello saber que genero es el que predomina en este filtro.

# COMMAND ----------

#Seleccionar columnas
alumnosmax = alumnos1[alumnos1['reading_score'] == alumnos1['reading_score'].max()] #subdf mayor calif
value = pd.DataFrame(alumnosmax[['school_name', 'grade', 'reading_score' ,'gender']].value_counts().sort_values(ascending = True).head(10))

print('Info school, grade, reading, gender')
print(alumnosmax[['school_name', 'grade', 'reading_score' ,'gender']].value_counts().sort_values(ascending = True).head(10))

# COMMAND ----------


