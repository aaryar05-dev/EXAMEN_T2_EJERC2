def suma_entre(lista, i, pi, pf, sumar):

    if i == len(lista):
        return 0

    if lista[i] == pf:
        return 0

    if sumar == True:
        return lista[i] + suma_entre(lista, i + 1, pi, pf, sumar)

    if lista[i] == pi:
        return suma_entre(lista, i + 1, pi, pf, True)

    return suma_entre(lista, i + 1, pi, pf, sumar)


lista = []

n = int(input("Ingrese cantidad de números: "))

for i in range(n):
    numero = int(input("Ingrese número: "))
    lista.append(numero)

pi = int(input("Ingrese PI: "))
pf = int(input("Ingrese PF: "))

resultado = suma_entre(lista, 0, pi, pf, False)

print("Resultado =", resultado)