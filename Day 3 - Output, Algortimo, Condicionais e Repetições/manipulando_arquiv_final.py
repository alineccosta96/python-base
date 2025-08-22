'''
Esse programa tem como objetivo relembrar tudo que eu fiz de arquivo. Usando o import OS
'''

import os

#criar diretório
path = os.curdir #Pega o diretório local

#Cria um diretório 
filepath = os.path.join(path, "Final Aquivo")
os.makedirs(filepath, exist_ok = True) #Verifica se ele já existe, se não, gera erro. 

#Cria um arquivo

arquivo = os.path.join(filepath, "arquivo_final.txt")

with open(arquivo, 'a') as f:
    f.write("Escreva o teste\n")

with open(arquivo, 'r') as f:
    print(f.readl()) #lê todo o conteúdo do arquivo de uma vez.Depois disso, o ponteiro interno do arquivo vai para o final.



