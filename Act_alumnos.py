# Databricks notebook source
# MAGIC %md #Alumnos por grado

# COMMAND ----------

import pandas as pd

path = '/dbfs/mnt/dpo/AI_Factory/MonterreyDigitalHub/Modulo 17 - Alumnos por grado/clean_students_complete.csv'
alumnos = pd.read_csv(path)
display(alumnos)

# COMMAND ----------

alumnos = alumnos.drop(labels=['Unnamed: 0', 'Student ID'], axis=1)
display(alumnos)

# COMMAND ----------

# MAGIC %md ##Act avanzada
# MAGIC 
# MAGIC Crea/Presenta  la forma que creas más conveniente para describir cuántos alumnos hay por grados, segmentanto por género, asignatura y grado.

# COMMAND ----------

import matplotlib.pyplot as plt
import numpy as np

# COMMAND ----------

alumnos.describe()

# COMMAND ----------

#genero = alumnos["gender"].unique
# pie = alumnos["gender"].value_counts().plot.pie(figsize=(10,10), labels= genero, autopct="%0.1f")
alumnos['gender'].value_counts().sort_values(ascending = True).plot(kind="pie")

# COMMAND ----------

keys = alumnos["gender"].value_counts().keys()
pie = alumnos["gender"].value_counts().plot.pie(figsize=(10,10), labels= keys, autopct="%0.2f %%")

# COMMAND ----------

#Observar grades
alumnos["grade"].value_counts().sort_values(ascending=True)

# COMMAND ----------

#Diferente visualizacón
values = pd.DataFrame(alumnos["grade"].value_counts().sort_values(ascending=True))
#display(values)

# COMMAND ----------

temp = alumnos['gender'].value_counts()
temp

# COMMAND ----------

#Dataframe por hacer en gráfica, no es necesario este paso pero permite uqe la visualización de datos previos sea posible
value = alumnos[["grade", "gender", "reading_score"]]
value

# COMMAND ----------

import seaborn as sns
import matplotlib.pyplot as plt
 
sns.barplot(x = 'grade', y = 'reading_score', hue = 'gender', data = value)
 
plt.show()
