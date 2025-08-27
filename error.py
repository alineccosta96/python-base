'''
Explica como usar o try except

Em python, "É mais fácil pedir perdão do que permissão

'''

import sys


try:
    names = open("names.txt").readlines() #prga todas as linhas
    # names = open("names.txt").readline() #pega somente a linha única   
except FileNotFoundError:
    print("Error: Arquivo não existe.")
    sys.exit()
except ZeroDivisionError:
    print("Error: Não existe divisão por zero")
    sys.exit()
except AttributeError as e: 
    print(f"Error: {str(e)}")
    sys.exit()
else: #executa somente se não encontrar nenhum erro
    print("Sucesso ao abrir o arquivo name.txt")
finally: #executa sempre - tendo erro ou não
    print("Executa sempre!!")


try:
    print(names[2])
except:
    print("Error: Nome não encontrado")
    sys.exit()