#Numero impar, par, o multiplo de otro

N = int(input("Ingrese un numero: "))
M = int(input("Ingrese su posible multiplo: "))

def MUL(N, M):
    if N%M == 0:
        return True
    return False

if N%2 == 0:
    print("El numero", N, "es par")
else:
    print("El numero", N, "es impar")

if MUL(N, M):
    print(N, "es multiplo de", M)
else:
    print(N, "no es multiplo de", M)