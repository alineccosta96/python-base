################
# Usanto template para montar email e somente usar as inciais
# %s string
# %i inteiro
# %f float (%.2) define 2 casas decimais
################

email_template = '''
Olá, %(nome)s! 

Tem interesse em comprar o %(produto)s?
Esse produto é ótimo para resolver %(coisas)s

Clique agora em %(link)s

Apenas %(quantidades)d disponiveis. 

Preço promocional %(preco).2f
'''

clientes = ["Maria", "Joao", "Paulo"]

for c in clientes: 
    print(email_template % {"nome": c,"produto": "caneta", "coisas": "escrever textos importantes", "link": "https://caneta.com", "quantidades": 1, "preco": 25.98 })
    print("-" * 20)