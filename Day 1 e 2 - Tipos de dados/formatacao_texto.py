nome = "Aline"
saldo = 30.00 #float

print("O saldo da "+ nome + " é de " + str(saldo)) #Converter para str

print("-"*20)
################
# Usanto template
# %s string
# %i inteiro
# %f float (%.2) define 2 casas decimais
################

'''
Exemplo de concartenação
concartenação que é o %s -> Usada para log (pq é muito antiga e eles não mudaram isso)
'''

irma = "Alana"
dinheiro = 90.00 #float 
ordem = 1 
#template = "O saldo da %s é de %f reais"
#template = "A %s é irmã da %s"
template = "A %s é a %i filha. Depois vem a %s com %.2f reais"  
a = template %(irma, ordem, nome, dinheiro)
print(a)
print("-"*20)


'''
Exemplo de str.format()
que é o {} -> msg longas e emails
'''

print("{:^11}".format(irma)) # "{^11}" centraliza em 11 carateres o texto que está em "irma"
print("{:<11}".format(irma)) # "{<11}" coloca para direita o texto que está em "irma"
print("{:>11}".format(irma)) # "{<11}" coloca para esquerda o texto que está em "irma"

print("-"*20)
print("Se eu quiser preencher os espaçoes é somente eu fazer assim. Colocar o '-' antes")
print("{:-^11}".format(irma))

msg = "Olá, {}. Você é o jogador {:03d} e tem {:.3f} pontos"
msg_formatada = msg.format("Aline", 1, 985.58)
print(msg_formatada)

print("-"*20)

msg2 = "Olá, {nome}. Você é o jogador {play:03d} e tem {pontos:.3f} pontos"
msg_formatada2 = msg2.format(play=1,nome="Maria", pontos=154.20) #imita um dicionario e garante que não se perde
print(msg_formatada2)

print("-"*20)
'''
Exemplo de f string (precisa colocar a letra f e a string) 
Usada para o restante, print, error..
'''

msg_nova = f"Olá, {nome}" #coloca esse F na frente e coloca as chaves com a var
print(msg_nova)

girafa = "🦒"
print(girafa)
print("\U0001F992") #CÓDIGO DA TABELA DE UNICODE EXPLORE (\u)
print("\N{mouse}") #NOME DO EMOJI NA TABELA UNICODE (\n) de name



