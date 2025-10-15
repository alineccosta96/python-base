'''
Faça um programa de quarto de hotel que mostre uma lista de quartos para alugar e o preço
de cada quarto. Essas informações estão num arquivo texto chamado "quartos.txt"

quartos.txt
#codigo, nome, preco
1, Master, 500
2, Familia, 200
3, Solteiro, 50

O programa pergunta ao usuário o nome, qual número do quarto e quantidade de dias e, no final, 
exibe o valor a ser pago. 

O programa deve salvar em outro arquivo contento as reservas. 

reservas.txt
#cliente, quarto, dias
Aline,3, 2

Se outro usuário tentar reservar o quarto o programa exibe uma mensagem que o quarto está reservado.
'''

import os
import sys
import logging

path = os.curdir
filepath = os.path.join(path, "reservas_hotel")
os.makedirs(filepath, exist_ok = True) #Verifica se ele já existe, se não, gera erro. 
arquivo_reserva = os.path.join(filepath, "reservas.txt")
arquivo_quarto = os.path.join(filepath, "quartos.txt")


var_nome = input("Qual seu nome? ")

dic_quarto_hotel = {}
lista_quarto_reservados = []

print("Lista de quartos")
print("-"*50)
with open(arquivo_quarto, 'r') as f:
   for line in f:     
    codigo, nome, valor =  line.strip().split(",") 
    print(f"Opção {codigo}- Suite{nome} no valor da diária de R$ {float(valor):.2f}")
    dic_quarto_hotel[codigo.strip()] = {"nome": nome.strip(), "valor": valor.strip()} 

print("-"*50)
var_quarto = input("Qual o número do quarto que deseja reservar? ")
var_dias = input("Quantidade de dias? ")


with open(arquivo_reserva, 'r') as f:
  for line in f:     
     nome, quarto, dias =  line.strip().split(",") 
     lista_quarto_reservados.append(quarto)
     if var_quarto.strip() == quarto.strip():
       logging.error("Quarto já reservado")      
       sys.exit() 

if var_quarto.strip() not in dic_quarto_hotel: 
    logging.error("Quarto não existe")
    sys.exit()
       
#print(dic_quarto_hotel.keys()) 
with open(arquivo_reserva, 'a') as f: 
   f.write("\n")
   f.write(f"{var_nome}, {var_quarto}, {var_dias}")   
   valor_quarto = dic_quarto_hotel[var_quarto]["valor"]
   try:
       total_pagar = int(var_dias) * float(valor_quarto)
       print(f"{var_nome}, o valor que você vai pagar pelo quarto {dic_quarto_hotel[var_quarto]["nome"]} é: R${total_pagar:.2f}")
   except ValueError: 
      logging.error("Impossivel calcular o valor")
      sys.exit()
   






    

 

