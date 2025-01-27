#Interés compuesto dado un capital, tasa y tiempo

def CAL(Monto,Tasa,Tiempo):
    Interes = Monto*(Tiempo*(Tasa/100))

    print("El interes es de: $", format(Interes))

Monto = float(input("Ingrese la cantidad del prestamo: "))
Tasa = int(input("Ingrese la tasa de interes: %"))
Tiempo = int(input("Ingrese el tiempo (meses): "))
CAL(Monto, Tasa, Tiempo)