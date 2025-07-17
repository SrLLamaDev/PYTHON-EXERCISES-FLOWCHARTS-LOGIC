#condicional

#ingrese cinco
numeros = list(map(int, input("Ingrese cinco números: ").split()))

# Verificar que el usuario ingresó exactamente 5 números
if len(numeros) != 5:
    print("Error: Debe ingresar exactamente cinco números.")
else:
    # Encontrar el mínimo y el máximo
    minimo = min(numeros)
    maximo = max(numeros)

    # Imprimir los resultados
    print(f"Mínimo = {minimo}, Máximo = {maximo}")
