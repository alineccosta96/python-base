cliente = {
    "nome": "Aline", 
    "idade":29, 
    "codigo_pais": 55
}
extra = {
    "pais": "Brasil"
}
# Dicionários são estruturas de dados que armazenam pares de chave-valor.
print(cliente)

'''Métodos comuns de dicionários:
cliente.keys(): 
    retorna todas as chaves do dicionário (por exemplo: `"nome"`, `"idade"`, `"codigo_pais"`).
cliente.values(): 
    retorna todos os valores do dicionário (por exemplo: `"Aline"`, `29`, `55`).
cliente.items(): 
    retorna uma lista de tuplas com os pares (chave, valor), 
    por exemplo: `("nome", "Aline")`, `("idade", 29)`, etc.

Resumindo:
- `.keys()` → só as chaves
- `.values()` → só os valores
- `.items()` → pares (chave, valor)'''

###########################################################

novo_dic = {**cliente, **extra} # Junta dois dicionarios: dois '*' para cada um representar chave e valor

print(novo_dic)

for chave, valor in novo_dic.items():
    print(chave, '->', valor)

'''novo_dic representa o dicionário em si.

Se você fizer for chave in novo_dic, o loop vai iterar apenas nas chaves ("nome", "idade", etc.).

novo_dic.items() retorna uma lista de tuplas, onde cada tupla contém o par chave-valor'''

###############################################

# Criar - Adicionar chave+valor

cliente["nome2"] = "Bruno"

print(cliente)

#Ler valor a partir de uma chave

print(cliente["nome2"])

#Update - Alterar valor a partir de uma chave

cliente["nome2"] = "Bruno Rocha"
print(cliente)

#Delete - Remover um valor e sua chave.

#del cliente["nome"]
#A keyword del remove uma variável que foi atribuida e pode ser usada com chaves de dicionários.

