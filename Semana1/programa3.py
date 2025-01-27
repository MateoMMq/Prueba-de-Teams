#Numero factorial

N = int(input("Ingrese un numero del cualquiera su factorial: "))
Fac = 1

for i in range(1,1+N):
    Fac*=i
    print("El numero factorial de :",N, "es: ",Fac)