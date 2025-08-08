'''
Cadastro de produto usnado dicionário
'''
__version__ = '0.1'
__author__ = 'Aline Costa'

import pprint #formato de print mais bonito

produto = {
    "nome": "Caneta", 
    "cor": "azul",
    "preco": 1.75,
    "codigo": 48569,
    "dimensao": 
    {
        "largura": 0.8,
        "altura": 3.5
    },
    "em_estoque": True
}

cliente = {
    "nome":"Bruno"
}

compra = {
    "cliente" : cliente,
    "produto" : produto,
    "quantidade" : 3
}


'''pprint.pprint(compra)
Retorna: 
{'cliente': {'nome': 'Bruno'},
 'produto': {'codigo': 48569,
             'cor': 'azul',
             'dimensao': {'altura': 3.5, 'largura': 0.8},
             'em_estoque': True,
             'nome': 'Caneta',
             'preco': 1.75},
 'quantidade': 3}
'''
total_compra = compra["produto"]["preco"] * compra["quantidade"]

print(
    f'O cliente', compra["cliente"]["nome"], 'comprou', compra["quantidade"], "unidades de", compra["produto"]["nome"], 'por R$', total_compra, 'reais. '
    f'A', compra["produto"]["nome"], 'tem largura de', compra["produto"]["dimensao"]["altura"], "cm"
)

