#calculadora

def suma(a, b):
    return a + b 

def resta(a, b):
    return a - b

def mul(a, b):
    return a * b

def divicion(a, b):
    if b != 0:
        return a/b
    else:
        return "Error, Valores invalidos. No se puede dividir entre 0"
    

N1 = float(input("ingrese el primer numero: "))
N2 = float(input("ingrese el segundo numero: "))


print("Suma: ", suma(N1,N2))
print("Resta: ", resta(N1,N2))
print("Multiplicación: ", mul(N1,N2))
print("Divición: ", divicion(N1,N2))