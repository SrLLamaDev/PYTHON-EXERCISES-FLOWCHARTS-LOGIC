#condicional
'''
Solicita cinco valores enteros e imprime 
a existencia de si hay duplicados o no.
'''
# Solicitar al usuario cinco valores enteros
numeros = list(map(int, input("Ingrese cinco números: ").split()))

# Verificar si hay duplicados
if len(numeros) != len(set(numeros)):
    print("Duplicados")
else:
    print("Todos unicos")
