# Databricks notebook source
# Librerías

#Create Widget
#dbutils.widgets.text("PrimerNum", "")
#dbutils.widgets.text("SegundoNum", "")

#dbutils.widgets.remove("PrimerNum")

num1 = dbutils.widgets.get("PrimerNum")
num2 = dbutils.widgets.get("SegundoNum")

#print(factores)
#print(csv)

# COMMAND ----------

# MAGIC %md #Ejercicio Básica
# MAGIC Crear una calculadora con al menos 4 operaciones básicas

# COMMAND ----------

class calc:
    def __init__(self,num1,num2):
        self.num1= float(num1)
        self.num2= float(num2)
    
    def suma(self):
        suma=self.num1+self.num2
        print('La sumatoria es igual a: ', suma)
        
    def resta(self):
        resta=self.num1-self.num2
        print('La diferencia es igual a: ',resta)
        
#num1=input('Ingrese el primer número: ')
#num2=input('Ingrese el segundo número: ')

calc=calc(num1,num2)
calc.suma()
calc.resta()

# COMMAND ----------

# MAGIC %md #Ejercicio Avanzado
# MAGIC Crear una calculadora con al menos 4 operaciones básicas + raíz cuadrada y elevar a una potencia.

# COMMAND ----------

class calculadora2:
    def __init__(self,num1,num2):
        self.num1= float(num1)
        self.num2= float(num2)
    
    def suma(self):
        suma=self.num1+self.num2
        print('La sumatoria es igual a: ', suma)
        
    def resta(self):
        resta=self.num1-self.num2
        print('La diferencia es igual a: ',resta)
        
    def multi(self):
        multi= self.num1 * self.num2
        print('La multiplicación es igual a: ',multi)
        
    def div(self):
        div= self.num1 / self.num2
        print('La división es igual a: ',div)

calculadora2=calculadora2(num1,num2)
calculadora2.suma()
calculadora2.resta()
calculadora2.multi()
calculadora2.div()
