'''Tudo que você faz com a tupla você pode fazer com a lista:
fatiar, acessar po index, desacoplar e etc'''

users = []
users.append("Aline")
print(users)
users.append("João")
users.append("Maria")
print(users)

# O append coloca sempre na última posição.
#Caso queria adicionar numa posição especifica adicionar o insert Ex: Adcionar Fabio em primeiro
users.insert(0, "Fabio")
print(users)
users.insert(2, "Klara")
print(users)

#Para remover
users.remove("João")
print(users)

#Juntar listas
outra_lista = ["Rose", "Alana"]
new= users + outra_lista #Aqui ele cria um objeto novo. Ele não altera a lista users e nem outra_lista
print(new)

users.extend(outra_lista) #Aqui sim eu transformo a lista "users"
print(users)
print(users.count("Alana")) #mostra quantas vezes Alana está dentro da lista
users.append("Alana") #insere novamente
print(users)
users.remove("Alana") #Ele tira somente a primeira que encontrar. Precisafazer isso até tirar todas
print(users)