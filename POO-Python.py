# Databricks notebook source
# MAGIC %md
# MAGIC # Organizar el código y llamar funciones/transformaciones n cantidad de veces (re-utilizar)

# COMMAND ----------

class Persona: #Def clase #__name__
    '''Clase que repesenta a una persona''' #__doc__
    nombre = 'Isaac'
    apellido = "Hernandez"
    genero = "M"
    cedula = "N/A"

# COMMAND ----------

Emp1=Persona #Asignación

# COMMAND ----------

Emp1.nombre #Buscar valor

# COMMAND ----------

Emp2=Persona

# COMMAND ----------

Emp2.nombre

# COMMAND ----------

dir(Emp1)

# COMMAND ----------

print("El objeto de la clase "+Emp1.__name__+", "+Emp1.__doc__)

# COMMAND ----------

class Persona: #Def clase
    '''Clase que repesenta a una persona'''
    nombre = 'Isaac'
    apellido = "Hernandez"
    genero ="M"
    cedula = "N/A"
    def hablar(self,mensaje):
        '''Impresión de un mensaje''' #Mensaje de saludo
        return mensaje

# COMMAND ----------

Emp2=Persona

# COMMAND ----------

Persona().hablar("Mensaje personalizado 1") #Se manda a la persona, el mensaje 

# COMMAND ----------

# Persona().saludo("Pertenezco a la clase {0}".format(Emp2.__name__))

# COMMAND ----------

dir(Emp2)

# COMMAND ----------

type(Persona().hablar)

# COMMAND ----------

Persona().hablar.__doc__

# COMMAND ----------

Emp2.hablar

# COMMAND ----------

Emp2.nombre

# COMMAND ----------

class Persona: #Def clase
    '''Clase que repesenta a una persona'''
    
    def __init__(self, nombre, apellido, genero, cedula): #Definir función init
        self.nombre = nombre
        self.apellido = apellido
        self.genero = genero
        self.cedula = cedula
# self es para decirte como vas a guardar cada cosa
        
    def hablar(self,mensaje):
        '''Impresión de un mensaje'''
        return mensaje

# COMMAND ----------

class Superv(Persona):
    '''Clase que representa a un supervisor'''
    
    def __init__(self, nombre, apellido, genero, cedula, puesto):
        '''Constructor para un supervisor'''
        
        Persona.__init__(self, nombre, apellido, genero, cedula)
        self.puesto=puesto #Atributo nuevo que lo diferencía de la clase Persona
        self.tareas=["10","11","12","13"] #Nuevo atributo diferenciador por medio de Monkey Patching
        
    def __str__(self):
        '''Devuelve la cadena descriptiva'''
        
        return "%s: %s %s, puesto: '%s', sus tareas son %s" %( #% regresa el último valor
            #   0  1   2     3      VE__init            4
        self.__doc__,self.nombre, self.apellido, self.puesto, self.consulta_tareas())
        #      0           1             2             3            4
        #Clase que representa a un supervisor: Mauricio Gomez, puesto: 'B', sus tareas son 10, 11, 12, 13
    
    def consulta_tareas(self):
        '''Mostrar las tareas de un supervisor'''
        return ", ".join(self.tareas)

# COMMAND ----------

Emp2=Persona("nombre","apellido","genero","cedula")

# COMMAND ----------

dir(Emp2)

# COMMAND ----------

Super1=Superv("nombre","apellido","genero","cedula", "puesto")

# COMMAND ----------

dir(Super1)

# COMMAND ----------

Super2=Superv("Isaac","Hernandez","M","123", "A")

# COMMAND ----------

Super3=Superv("Mauricio","Gomez","M","456", "B")

# COMMAND ----------

# es como un estilo de print, donde el índice 0 se toma y se le da el format
print("Cedula de S1: {0}".format(Super1.cedula))

# COMMAND ----------

# MAGIC %md #Notas
# MAGIC * Hay dos tipos de entrada, herencia simple (ejemplo que vimos, hereda todo lo que viene de padre) y herencia múltiple (hereda todo de ambos)
# MAGIC * Orden primero de librerías y luego las clases padre, hijos y luego el main
# MAGIC * Self ayuda a llamar funciones previamente definidas

# COMMAND ----------

print("\n" + str(Super3))

# COMMAND ----------

print("Las tareas son: {0}".format(Super2.consulta_tareas()))

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
        
num1=input('Ingrese el primer número: ')
num2=input('Ingrese el segundo número: ')

calc=calc(num1,num2)
calc.suma()
calc.resta()
