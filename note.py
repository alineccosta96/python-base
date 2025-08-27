'''
Esse progrma simula um bloco de notas. 
Quando o usuário rodar "new". Ele cria um titulo, uma tag e um texto para salvar: 

note.py new "Minha Nota"
tag: tech
texto: Esse bloco de notas é de tecnologia

Quando o usupario digitar "read" ele lê o texto da tag que o usuário informar:
note.py read tech
'''

__version__ = "0.1.0"

import os
import sys

path = os.curdir
filepath = os.path.join(path, "note.txt")

arguments = sys.argv[1:]
cmds = ["read", "new"]

if not arguments:
    print(f"Sem argumentos. Os válidos são {cmds}")
    sys.exit()


if arguments[0] not in cmds:
    print(f"Argument inválido {arguments[0]}")

tags = []

if arguments[0] == "new":
    with open(filepath , 'a', encoding="utf-8") as f:
        titulo = input("Digite o titulo:")
        f.write(titulo+ "\t")
        tag = input("Digite a tag: ")
        f.write(tag+ "\t")        
        texto = input("Digite o conteudo: ")
        f.write(texto+ "\n")

if arguments[0] == "read":
    try:
        for line in open(filepath):        
            titulo, tag, texto = line.split("\t") 
            tags.append(tag)        

        if arguments[1] in tags:
            if tag.lower() == arguments[1].lower():
                print(f"Titulo: {titulo}")
                print(f"Texto: {texto}")
        else:
            print("Tag informnada não existe")
    except IndexError:
        print("Você precisa passar uma tag como parametro")
      
   

