#Lista de núumeros pares e impares hasta un líımite dado

Ni = int(input("Introducir el inicio del rango: "))
Nf = int(input("Introducir el final del rango: "))

if (Nf > Ni):
    for x in range(Ni, Nf):
        if((x%2) != 0):
            print("El", x, "es impar")

else:
    print("El rango es ilogico")