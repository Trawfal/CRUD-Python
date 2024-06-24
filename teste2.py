minha_lista = ['Kevin', 22, 'Matheus', 21, 'Diego', 20]

#Metodo append - adiciona um elemento ao final da lista
minha_lista.append(6)
print(minha_lista)

#Metodo index - retorna o indice do elemento especificado
indice = minha_lista.index(22)
print(indice)

#Metodo insert - insire um elemento em um indice especifico
minha_lista.insert(1, 'indefinido')
print(minha_lista)

#Metodo pop - remove um index especificio
remover = minha_lista.pop(1)
print(remover)
print(minha_lista)

print(minha_lista.sort)