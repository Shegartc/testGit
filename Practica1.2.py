#Edgar Torres
#6/Mayo/2023
#Calculadora de IMC

#Entradas
Peso = float(input("Peso(Kg): "))
Altura = float(input("Estatura(m): "))

#Proceso
IMC=round(Peso/(Altura**2),2)

#Salida
print("Tu IMC es: ",IMC)

#Estructura condicional
if IMC >= 30:
    print("Obesidad")
elif IMC >= 25:
    print("Sobrepeso")
elif IMC >=18.5:
    print("Normal")
else:
    print("Peso Bajo")
    