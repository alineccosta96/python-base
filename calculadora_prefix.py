''''
Esse programa tem como objetivo o usuário digitar a operação e dois numero e calcular o retorno.

Operações: 
sum -> +
sub -> -
mult -> * 
div -> /
'''
__version__ = '0.1'
__author__ = "Aline Costa"

import os

from pathlib import Path
from datetime import datetime

# Day 3 ... poderia ser substituido por Path('.') que pega o diretório atual 
# sempre fazer para saber onde salvar ou passar o caminho

#Cria o caminho do log
filepath = Path("Day 3 - Output, Algortimo, Condicionais e Repetições") / Path("Calculadora Prefix - Aline")

arquivo = filepath / Path("log_calculadora_prefix.txt")

#Verifica se existe, se não, cria a subpastas do arquivo e o arquivo
filepath.mkdir(parents=True, exist_ok=True)

argumentos = {
    "sum": '+',
    "sub": '-',
    "mult": '*', 
    'div': '/'
}

operacao = input("Digite a operação - <sum><sub><mult><div>: ")


if operacao not in argumentos.keys():
    print(f"Operação Inválida!")
else:
    # Basicamente eu disse: argumentos["sum"] 
    # que é: Pegue o valor correspondente à chave que o usuário digitou.
    simbolo = argumentos[operacao]   
    print(f"A operação escolhida foi: {simbolo}")  
    num1 = input("Digite o primeiro número: ")
    num2 = input("Digite o segundo número: ")
    if ('.' in num1) or ('.' in num2):
        num1 = float(num1)
        num2 = float(num2)
    else: 
        num1 = int(num1)
        num2 = int(num2)
    if simbolo == '+':        
        total = num1 + num2       
    elif simbolo == '-':       
        total = num1 - num2
    elif simbolo == '*':        
        total = num1 * num2
    elif simbolo == '/':        
        total = num1 / num2
    
with (arquivo.open("a")) as f:   
    # Não funciona assim porque a linha só aceita um parametro de string, no caso abaixo usei 2
    #f.write(f"O resultado da operação é:", num1, simbolo, num2, "=", total)
    data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")    
    f.write(f"{data} - O resultado da operação é: {num1} {simbolo} {num2} = {total}\n")
    print("Salvando no log....")

print(f"O total da operação é:", total)



