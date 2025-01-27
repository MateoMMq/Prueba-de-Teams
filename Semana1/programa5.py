#Numero primo

N = int(input("Ingrese un numero entero: "))

Prim = True
for x in range(2,N):
    if N&x == 0:
        Prim = False

if Prim:
    print(N, "es primo")
else:
    print(N, "no es primo")