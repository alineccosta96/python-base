clientes = {
    "nome": "Aline",
    "idade": 29,
    "sexo": "feminino"
}

var = 29

#Retorna somente as chaves em formato de dic: 
# clientes.keys() -> Retorno: dict_keys(['nome', 'idade', 'sexo'])

#Retorna somente os valores em formato de dic: 
# clientes.values() -> Retorno: dict_values(['Aline', 29, 'feminino'])

#Retorna conjunto de chave e valor em formato de dic: 
# clientes.items() -> Retorno: dict_items([('nome', 'Aline'), ('idade', 29), ('sexo', 'feminino')])

for chave in clientes.keys():
    if var == chave:
        print(f"A variável é igual à chave: {chave}")

for valor in clientes.values():
    if var == valor:
        print(f"A variável é igual ao valor: {valor}")

for chave, valor in clientes.items():
    if var == chave:
        print(f"A variável é igual à chave: {chave}")
    elif var == valor:
        print(f"A variável é igual ao valor: {valor}")
