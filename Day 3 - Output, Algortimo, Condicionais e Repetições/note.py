'''
Esse progrma simula um bloco de notas. 
Quando o usuário rodar "new". Ele cria um titulo, uma tag e um texto para salvar: 

python note.py new 
"minha nota"
tag: tech
texto: Esse bloco de notas é de tecnologia

Quando o usupario digitar "read" ele lê o texto da tag que o usuário informar:
python note.py read tech

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

while True:
    if arguments[0] == "new":
        with open(filepath , 'a', encoding="utf-8") as f:
            titulo = input("Digite o titulo:")
            f.write(titulo+ "\t")
            tag = input("Digite a tag: ")
            f.write(tag.lower()+ "\t")        
            texto = input("Digite o conteudo: ")
            f.write(texto+ "\n")

    if arguments[0] == "read":
        try:
            tag_read = arguments[1].lower()            
        except IndexError:
            tag_read = input("Digite a tag:").strip().lower()

            for line in open(filepath):        
                titulo, tag, texto = line.split("\t") 
                tags.append(tag)       

                if tag_read in tags:                      
                   if tag.lower() == tag_read:            
                       print(f"Titulo: {titulo}")
                       print(f"Texto: {texto}")
                else:
                   print("Tag informnada não existe")
    
    resp = input(f"Quer continuar {arguments[0]}? [n/y]").strip().lower()
    if resp == 'n' or resp != 'y':
        break
    else:
        continue
      
   

