#EdgarTorres
#6 de Mayo del 2023
#Primer programa de calculo de propinas
print("Bienvenido a la calculadora de propinas")
#Entradas
cuenta = float(input("Monto a pagar: "))
porcentaje = int(input("% Propina: "))
comensales= int(input ("# de personas: "))
#Procesos
porcentajeDecimal = porcentaje/100
propina = cuenta * porcentajeDecimal
totalCuenta = cuenta + propina
pagoPersona = totalCuenta/comensales
pagoTotal = round(pagoPersona,2) #Funcion predefinida para redondear
#Salida
print("Pago por persona: $",pagoTotal," Pesos MXN")




