'''
Cadastro de produto
'''
__version__ = '0.1'
__author__ = 'Aline Costa'

produto_nome = 'Caneta'
cor = "Azul"
preco = 1.75
dimensao_largura = 0.8
dimensao_altura = 3.5
produto_codigo = 48569

compra = ("Bruno", produto_nome, 3)
total_compra = compra[2] * preco
print(f'O cliente', compra[0], 'comprou uma ', compra[1], 'por R$', total_compra, ' reais')