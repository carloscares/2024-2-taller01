# Cree un programa que dado una lectura de una lista
# genere una lista con las longitudes de cada elemento
# dividido por 3 con un máximo de 2 decimales (obs,
# esto forzará que la representación sea como string
# al interior de la lista).

# Ejemplo de entrada
# uno dos tres cuatro noventa
# salida
# ['1.00', '1.00', '1.33', '2.00', '2.33']

lista = input().split()
print([str(len(lista)) for x in lista])