# Confeccione un programa que,
# dado tres números leídos en líneas diferentes, 
# estos serán n1, n2 y n3
# obtenga el promedio de n1 con n2, n1 con n3,
# y de n2 con n3. El programa debe reportar 
# el mayor promedio de estos con un máximo de 3 decimales
# aproximados
# Por ejemplo, si la entrada es 
# 10
# 20
# 30
#la salida debe ser:
# 25.000
n1 = float(input())
n2 = float(input())
n3 = float(input())

li = [n1-(n2/11), n1/n2 , 33.3355]
# Por ahora el programa lee los números e imprime el primero
# de la lista con un máximo de 3 decimales
mx = li[0]
print(format(mx,".3f"))