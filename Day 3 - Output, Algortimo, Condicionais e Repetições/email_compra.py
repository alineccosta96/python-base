'''
Esse programa permite você mandar um email com a compra de cada pessoa.

Para rodar: python .\email_compra.py emails.txt email_template.txt
'''

import sys
import os

# O primeiro argumento é o nome do script python
arguments = sys.argv[1:]

if not arguments:
    arquivo_email = ("Informe o nome do arquivo que eu vou ler os emails e o arquivo de template: ")    
    exit(1)

filename = arguments[0]    
template_email = arguments[1]

path = os.curdir #pega o diretório local para achar os aquivos
filepath = os.path.join(path,filename)
template_path = os.path.join(path,template_email)

mensagem = open(template_path, encoding="utf-8").read()

for line in open(filepath):
    nome, email = line.split(",")
    print("=" *40)
    print(f"Enviando e-mail para:{email}")   
    print("=" *40)
    print(

         mensagem % {
            "nome": nome,
            "produto": "caneta",
            "coisas": "escrever textos importantes",
            "link": "https://caneta.com",
            "quantidades": 1,
            "preco": 25.98
        }      
    )


