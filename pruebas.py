from GC import *

gc = GregorianCalendar()

fecha1 = (2016,2,29)
fecha2 = (2018,8,12)
fecha3 = (2019,21,50)
fecha4 = (1,1,1)
fecha5 = ("a","b",True)
fecha6 = [2020,1,1]
fechas = [fecha1,fecha2,fecha3,fecha4,fecha5,fecha6]



print("Pruebas de GC")
print("Se realizarán las pruebas con los siguientes datos:")
for i in fechas:
    print(i)

print("De los cuales, solo los dos primeros son correctos")

print("\n Prueba de R0: fecha es tupla")
for i in fechas:
    print(i,"-> ",gc.fecha_es_tupla(i))

print("\n Prueba de R1: Bisiesto")
for i in fechas:
    print(i[0],"-> ",gc.bisiesto(i[0]))

print("\n Prueba de R2: Fecha es válida")
for i in fechas:
    print(i,"-> ",gc.fecha_es_valida(i))

print("\n Prueba de R3: Día siguiente")
for i in fechas:
    print(i,"-> ",gc.dia_siguiente(i))

print("\n Prueba de R4: Dias desde primero enero")
for i in fechas:
    print(i,"-> ",gc.dias_desde_primero_enero(i))

print("\n Prueba de R5: Día primero enero")
for i in fechas:
    print(i[0],"-> ",gc.dia(gc.dia_primero_enero(i[0])))

print("\n Prueba de R6: Imprimir 3x4 con 2018")
gc.imprimir_3x4(2018)
