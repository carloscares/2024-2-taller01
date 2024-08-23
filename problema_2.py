#Cree un programa en python que 
#dado dos enteros positivos, n1 y n2, genere una
#lista que comienza en n1, incrementa sus valores
#en el doble de n1 y tiene elementos mientras
#sean menores que n2
#Ejemplo de entrada:
#3
#30
#salida
#[3, 9, 15, 21, 27]
n1 = input()
n2 = input()
print([int(n1), int(n2)+int(n2), int(n1*3)])