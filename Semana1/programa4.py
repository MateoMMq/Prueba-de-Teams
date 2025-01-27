#Secuencia Fibonacci

N = int(input("Ingrese el numero con el que decee empezar la secuencia: "))

def SF(n):
    if n <= 0:
        return(0)
    elif n == 1:
        return(1)
    else:
        return SF(n-1) + SF(n-2)

print("El resutado de la secuencia para", N, "es igual a:", SF(N))