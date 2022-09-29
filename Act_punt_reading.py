# Databricks notebook source
# MAGIC %md # Act: puntaje reading
# MAGIC Crea / Presenta la forma que creas más conveniente para describir cuántos alumnos por escuela tuvieron el mejor puntaje en "reading", y con ello saber que género es el que predomina en este filtro.
# MAGIC Crea / Presenta la forma que creas más conveniente para describir cuántos alumnos por escuela tuvieron el peor puntaje en "reading", y con ello saber que género es el que predomina en este filtro.

# COMMAND ----------

# MAGIC %md ###Librerías y lectura de datos

# COMMAND ----------

import pandas as pd

path = '/dbfs/mnt/dpo/AI_Factory/MonterreyDigitalHub/Modulo 17 - Alumnos por grado/clean_students_complete.csv'
alumnos = pd.read_csv(path)
#display(alumnos)

# COMMAND ----------

alumnos = alumnos.drop(labels=['Unnamed: 0', 'Student ID'], axis=1)
display(alumnos)

# COMMAND ----------



# COMMAND ----------

# MAGIC %md #Act: puntaje reading 2

# COMMAND ----------

#Crea / Presenta la forma que creas más conveniente para describir qué grado por escuela tuvo el mejor puntaje en "reading" y con ello saber que genero es el que predomina en este filtro.

#Seleccionar columnas
df_EscuelaPuntajeReading = df_alumnos[['school_name','grade','reading_score', 'gender']]

df_EscuelaPuntajeReading_max = df_EscuelaPuntajeReading[df_EscuelaPuntajeReading['reading_score'] == df_EscuelaPuntajeReading['reading_score'].max()] #subdf mayor calif

print('Mix Género vs. MAX reading_score por grado:')
print(df_EscuelaPuntajeReading_max[['school_name', 'grade', 'reading_score' ,'gender']].value_counts().sort_values(ascending = True).head(10))


# COMMAND ----------

#Crea / Presenta un algoritmo que genere los datos de "reading_score" y "math_score", en variables categóricas, y guárdalo en dos columnas diferentes (cada columna nueva representa la nueva columna con variables categórica). 

#Crea / Presenta una gráfica que condense la información obtenida ahora categóricamente mostrando que género obtuvo mejor puntaje.
