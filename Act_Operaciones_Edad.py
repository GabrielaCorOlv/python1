# Databricks notebook source
# MAGIC %md #Inciso 1
# MAGIC 1.-El doble de mi edad tiene 24 años, ¿cuántos años tengo?

# COMMAND ----------

# x * 2 == 24

# Despejando
x = 24/2
x

# COMMAND ----------

# MAGIC %md #Inciso 2
# MAGIC 2.- A un tercio de la edad de mi hermana la disminuyo en 15 años. Tengo 6 años. ¿Qué edad tiene?

# COMMAND ----------

#(b * 1/3) - 15 = 6

# Despejando
b = (6+15)*3
b

# COMMAND ----------

# MAGIC %md #Inciso 3
# MAGIC 3.-Determina quién es más grande

# COMMAND ----------

if x > b:
    print("La más grande es x.") #Esta sentencia se ejecuta
else: 
    print("La más grande es b.") #Esta sentencia se ejecuta
