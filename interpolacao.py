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

'''Exemplo de como pegar o texto de uma tupla: '''
compra = ("Bruno", "caneta")
print(f"O cliente {compra[0]} comprou {compra[1]}")

'''Exemplo de como pegar o texto de uma var: '''
nome = "Aline"
saldo = 30.00 #float

print("O saldo da "+ nome + " é de " + str(saldo)) #Converter para str

'''Exemplo de como pegar o texto de uma var: '''
msg2 = "Olá, {nome}. Você é o jogador {play:03d} e tem {pontos:.3f} pontos"
msg_formatada2 = msg2.format(play=1,nome="Maria", pontos=154.20) #imita um dicionario e garante que não se perde
print(msg_formatada2)
