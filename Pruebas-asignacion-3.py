from GC import *

gc = GregorianCalendar()

fecha1 = (2015,1,29)
fecha2 = (2016,2,12)
fecha3 = (2017,3,1)
fecha4 = (2018,4,15)
fecha5 = (2019,5,31)
fecha6 = (2020,6,12)
fechas = [fecha1,fecha2,fecha3,fecha4,fecha5,fecha6]

print("Pruebas de GC pt 2")
print("No se incluyen las validaciones, ya que en la asignación pasada se comprobaron correctamente")
print("Se realizarán las pruebas con los siguientes datos:")
for i in fechas:
    print(i)

print("\n Prueba de R7: fecha futura")

for i in range(5,10):
    for j in fechas:
        print(i,"dias en el futuro de",j,"->",gc.fecha_futura(j,i))

print("\n Prueba de R8: cantidad de dias entre fechas")
for i in range(0,len(fechas),2):
    print("Dias entre",fechas[i],"y",fechas[i+1],"->",gc.dias_entre(fechas[i],fechas[i+1]))

print("\n Prueba de R9: Dia de la semana")
for i in fechas:
    print("Dia de la semana de",i,"-> ",gc.dia_semana(i))

print("\n Prueba de R10: Fecha futura hábil")
for i in range(5,10):
    for j in fechas:
        print(i,"dias habiles en el futuro de",j,"->",gc.fecha_futura(j,i))

print("\n Prueba de R11: Días habiles entre dos fechas")
for i in range(0,len(fechas),2):
    print("Dias habiles entre",fechas[i],"y",fechas[i+1],"->",gc.dias_habiles_entre(fechas[i],fechas[i+1]))
