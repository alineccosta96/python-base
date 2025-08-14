'''
Esse programa permite você mandar um email com a compra de cada pessoa
'''

email_template = '''
Olá, %(nome)s! 

Tem interesse em comprar o %(produto)s?
Esse produto é ótimo para resolver %(coisas)s

Clique agora em %(link)s

Apenas %(quantidades)d disponiveis. 

Preço promocional %(preco).2f
'''

import sys

# O primeiro argumento é o nome do script python
arguments = sys.argv[1:]

if not arguments:
    arquivo_email = input("Digite o nome do arquivo que eu vou ler os emails: ")
    exit(1)
    filename = arguments[0]

print(sys.argv)

clientes = ["Maria", "Joao", "Paulo"]

'''for c in clientes: 
    print(email_template % {"nome": c,"produto": "caneta", "coisas": "escrever textos importantes", "link": "https://caneta.com", "quantidades": 1, "preco": 25.98 })
    print("-" * 20)


compra = ("Bruno", "caneta")
print(f"O cliente {compra[0]} comprou {compra[1]}")'''

