'''
A Tupla não pode ser alterada. Portanto, não consigo substituir nada dentro dela, por exmpleo, 
trocar o nome Aline por Maria.
Com isso, elas sãos mais enxutas e mais rápidas.
Avaliar se usaremos tuplas ou listas
'''

dados = "Aline", 18, True, 4654.98 #pode fazer assim ou colocar () Ex: dados = ("Aline", 18, True)
print(type(dados))

#dados[4] = "Maria" Gera erro: TypeError: 'tuple' object does not support item assignment


#Quantas vezes Aline está dentro da tupla
print(dados.count("Aline"))

#mostra a posição 1 da tupla
# o -1 mostra a ultima posição --> pega a tupla ao contrario
print(dados[1], dados[-1])
print()

#Funciona como uma lista e pega todos os dados
for info in dados:
    print(info)

# Empacotamento (atribuição)
pontos = (1,2,3)

# Desempacotamento (atribuição multipla)
# É quando tiramos tudo da tupla e deixamos separados
x,y,z = pontos #aqui sabemos o total da tupla e colocamos a msm qtdade de variaveis
print(x,y,z)


# Atribuir sem parenteses
coord = 140, 200, 9

# atribuir com parenteses
coord = (140, 200, 9)

# desempacotar
x, y, z = coord

# ignorar elementos (será atribuito apenas o x já que *_ ignora o que vem depois)
x, *_ = coord

# pegar apenas o primeiro e o último elemento
x, *_, y = coord

# Verificar o tamanho
len(coord)
3

# Acessar via subscrição pelo indice
coord[0]
140

# fatiar
coord[1:]
(200, 9)

compra = ("Bruno", "caneta")
print(f"O cliente {compra[0]} comprou {compra[1]}")