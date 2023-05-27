#Edgar Torres
#Mayo 6 2023
#Ejercicio de estructuras de datos en Python

#Crear una lista
lista=["Lunes","Martes","Miercoles"]  
lista.append("Jueves")
lista.extend(["Viernes", "Sabado"])
lista.remove("Martes")
lista.pop()
print(lista)
numeros=[1,6,10,4,5]
numeros.remove(6)
numeros.pop(0)
print(numeros)
#Crear una tupla
deportes=("Boxeo", "MMA", "TaeKwonDo")
type(deportes)
len(deportes)
print(deportes)
#Inmutable, pero mas rapido y seguro
#Crear un diccionario
#Tienen dos elemento, llave (key) y valor (value)
dicNumeros={1:"Texto",2:25.36,3:True,4:12}
type(dicNumeros)
#Modificar
dicNumeros[1]="Edgar"
#Agregar
dicNumeros[5]="Dany"
#Eliminar
del dicNumeros[3]
print(dicNumeros)

#Crear Conjuntos (sets)
conjunto={2,4,8,3}
type(conjunto)
conjunto.add(7)
conjunto.add(7)
conjunto2={"Lunes","Martes","Miercoles"}
type(conjunto2)
conjunto2.add("Jueves")
print(conjunto)
print(conjunto2)
#Crear un Frozenset
conjFroz=frozenset([5,"Texto",6.8])
conjFroz.add("Prueba") #No agrega
type(conjFroz)
print(conjFroz)
