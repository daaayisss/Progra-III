def suma_pares(lista):
    suma = 0
    for numero in lista:
        if numero % 2 == 0:
            suma += numero
    return suma

def main():
    entrada = input("Ingrese una listameros separados por espacio: ")
    lista_numeros = [int(x) for x in entrada.split()]
    suma = suma_pares(lista_numeros)
    print("La suma de los números pares en la lista es:", suma)

if __name__ == "__main__":
    main()
