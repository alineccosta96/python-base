'''
Exemplo da função filtre: extrair números de uma string.
Só podemos usar a função filtre quando retorna algo bloenado.
Isdigit, isUpper, Islower
'''

texto = "Aline9846Costa798556"
print(list(filter(str.isdigit, texto))) #sem coverter para a lista não funciona filter object at 0x000001CE2A076320
print("".join(list(filter(str.isdigit, texto))))
# Usando o espaço vazio.join ele retorna um texto

'''
A função map() em Python é uma ferramenta poderosa para aplicar uma função a cada item 
de um iterável (como uma lista, tupla ou conjunto), sem precisar escrever um loop manualmente
'''

numeros = ([1,2,3,4], [5,5,5], [2,2,2])
print(list(map(sum, numeros)))
print(list(map(max, numeros)))

'''
Função all: todos da lista precisams ser True
'''

lista_all = [True, False]
lista_all2 = [2, "b", 0] # zero é considerado False

print(all(lista_all2))

'''
Função any: Pelo menos um True
'''

print(any(lista_all))


'''
Função enumerate: enumera coisas no python. Posso usasr até start para ele coemçar do dois, por exemplo
'''
nomes = ["Aline", "MB", "Alana", "Sofia", "Roseli"]

for index, nome in enumerate(nomes, start=2): 
    print(index, nome)

'''
Função:  é usada para agrupar elementos de múltiplos iteráveis (como listas ou tuplas) 
em pares (ou tuplas) correspondentes. Ela é muito útil quando você quer combinar dados
que estão relacionados entre si.
'''   

colunas = ["nome_a", "sobrenome_a"]
dados = ["Alana", "Costa"]

print(dict(zip(colunas, dados)))
print(dict(zip(colunas, dados))["nome_a"])

dados_2 = [("Aline", "Costa"), ("Marcos", "Bruno")]

for a in dados_2: 
    print(dict(zip(colunas, a)))
