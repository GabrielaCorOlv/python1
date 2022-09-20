# Databricks notebook source
# MAGIC %md #Leer CSV desde Azure

# COMMAND ----------

import pandas as pd

# COMMAND ----------

#Leer de azure usando pyspark
path = 'dbfs:/mnt/dpo/AI_Factory/MonterreyDigitalHub/Modulo 12 - Actividad Competidores Olimpicos/athlete_events.csv'
data = (spark.read.option("header", True).option("inferSchema", True,).option("encoding", "utf-8").csv(path))
display(data)

# COMMAND ----------

# MAGIC %md #Convertir a df de pandas

# COMMAND ----------

#Convertir a df de pandas
data_pandas = data.toPandas()
display(data_pandas)

# COMMAND ----------

# MAGIC %md #Avanzado
# MAGIC 
# MAGIC 1. Crear un programa en Visual Studio que me permita saber cuál es el competidor más veterano que ha recibido medalla para los NOC´s MEX, COL y ARG (oro, plata o bronce) 
# MAGIC 2. Crear un programa en Visual Studio que me permita saber cuál es el competidor más joven que ha recibido medalla de oro para los NOC´s USA y CAN
# MAGIC 3. Encuentra al competidor más ganador de la historia en medallas totales, medallas de oro, medallas de plata y medallas de broce para los NOC´s USA, CHN y RUS. Crea un csv con toda su información.

# COMMAND ----------

# 1. Crear un programa que permita saber cuál es el competidor más veterano que ha recibido medalla para los NOC´s MEX, COL y ARG (oro, plata o bronce)

df_pd = data_pandas

#Eliminar datos faltantes
indexes = df_pd[df_pd['Age'].isnull()].index #Elimino datos nulos específicamente de la variable 'age'
df_pd = df_pd.drop(index = indexes, inplace= False, axis = 0) #Los index se respetan

indexes = df_pd[df_pd['Medal'].isnull()].index #Elimino nulos de 'medal'
df_pd = df_pd.drop(index = indexes, inplace= False, axis = 0) #Respetar index 

cveterano = df_pd

#Filtrar (NOC´s -> mex, col, arg)
cveterano = cveterano[cveterano['NOC'].isin(['MEX', 'COL', 'ARG'])]
cveteranoMEX = cveterano[cveterano['NOC'] == 'MEX'] #Mexico
cveteranoARG = cveterano[cveterano['NOC'] == 'ARG'] #Argentina
cveteranoCOL = cveterano[cveterano['NOC'] == 'COL'] #Colombia

# Para obtener el más veterano de todos
#nombre_veterano = competidor_veterano[competidor_veterano['Age'] == max(competidor_veterano['Age'])]['Name'].item()

# Veterano Mex
cveteranoMEX = cveteranoMEX[cveteranoMEX['Age'] == max(cveteranoMEX['Age'])]['Name']
cveteranoMEX = cveteranoMEX.head(1).item() #Obtener el top 1
print("El más veterano en MEX es: ", cveteranoMEX)

# Veterano Arg
cveteranoARG = cveteranoARG[cveteranoARG['Age'] == max(cveteranoARG['Age'])]['Name']
cveteranoARG = cveteranoARG.head(1).item() #Obtener el top 1
print("El más veterano en ARG es: ", cveteranoARG)

# Veterano Col
cveteranoCOL = cveteranoCOL[cveteranoCOL['Age'] == max(cveteranoCOL['Age'])]['Name']
cveteranoCOL = cveteranoCOL.head(1).item() #Obtener el top 1
print("El más veterano en COL es: ", cveteranoCOL)

# COMMAND ----------

# 2. Crear un programa que me permita saber cuál es el competidor más joven que ha recibido medalla de oro para los NOC´s USA y CAN

# Se realiza limpieza por la medalla de oro
cjoven = df_pd
cjoven = cjoven[cjoven['Medal'] == 'Gold']

# Del filtro anterior ahora se busca solo para usa y can
cjovenUSA = cjoven[cjoven['NOC'] == 'USA']
cjovenCAN = cjoven[cjoven['NOC']== 'CAN']

# Se obtienen los nombres de los más jovenes para cada país
cjovenUSA = cjovenUSA[cjovenUSA['Age'] == min(cjoven['Age'])]['Name']
cjovenUSA = cjovenUSA.head(1).item()
print("El más joven USA con oro es: ", cjovenUSA)

cjovenCAN = cjovenCAN[cjovenCAN['Age'] == min(cjovenCAN['Age'])]['Name']
cjovenCAN = cjovenCAN.head(1).item()
print("El más joven CAN con oro es: ", cjovenCAN)

# COMMAND ----------

# 3. Encuentra al competidor más ganador de la historia en medallas totales, medallas de oro, medallas de plata y medallas de broce para los NOC´s USA, CHN y RUS. 
# Crea un csv con toda su información. Esto nono se puede por el espacio de AZURE en KOF, pero sería con (OrdAge.to_age("path.csv", header = True, index = True))

# Limpieza de medalla de ganadores totales de usa, chin y rus
medallasmax = df_pd
medallasmax = medallasmax[medallasmax['NOC'].isin(['USA', 'CHN', 'RUS'])][['NOC','Name', 'Medal']]

# Se hace por cada país
medallasmaxUSA = medallasmax[medallasmax['NOC'].isin(['USA'])][['NOC','Name', 'Medal']]
medallasmaxCHN = medallasmax[medallasmax['NOC'].isin(['CHN'])][['NOC','Name', 'Medal']]
medallasmaxRUS = medallasmax[medallasmax['NOC'].isin(['RUS'])][['NOC','Name', 'Medal']]

# Agrupar por NOC y Name

medallasmaxUSA = medallasmaxUSA.groupby(["NOC",'Name']).Medal.count().sort_values(ascending=False).head(3)
print("Los competidores que en más ocaciones es: ", medallasmaxUSA)

medallasmaxCHN = medallasmaxCHN.groupby(["NOC",'Name']).Medal.count().sort_values(ascending=False).head(3)
print("Los competidores que en más ocaciones es: ", medallasmaxCHN)
      
medallasmaxRUS = medallasmaxRUS.groupby(["NOC",'Name']).Medal.count().sort_values(ascending=False).head(3)
print("Los competidores que en más ocaciones es: ", medallasmaxRUS)
