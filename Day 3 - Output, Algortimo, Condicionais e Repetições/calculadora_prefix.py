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
import sys

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
    
try:
    with (arquivo.open("a")) as f:     
        data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")    
        f.write(f"{data} - O resultado da operação é: {num1} {simbolo} {num2} = {total}\n")
        print("Salvando no log....")
except PermissionError:
    print(f"Error: Por favor solicitar permissão de escrita no arquivo {arquivo}")
    sys.exit()

print(f"O total da operação é:", total)



