'''
Faça um programa que o usuário digite as palavras e você imprima as vogais duplicadas.

Ex.: 
Digite a palavra <enter para sair>: "Aline"
AAliinee
'''

while True: 
    
    palavra = input("Digite a palavra: ").upper()

    if palavra.strip() == '':
        print ("Recomeçe: Digite uma palavra válida")
        break

    vogais = ['A', 'E', 'I', 'O', 'U']
    mostra = ''

    for letra in palavra:
        if letra in vogais:
            mostra = mostra +letra * 2
        else: mostra = mostra + letra

    print(f"A palavra com as vogais duplicadas é: {mostra}")

    prox = input("Deseja continuar? <s/n> ")
    if prox == 's':
        continue
    else: 
        break
