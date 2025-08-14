import os 

#Cria diretório se exsitir
# Day 3 ... poderia ser substituido por os.curdir() que pega o diretório atual 
# sempre fazer para saber onde salvar ou passar o caminho
os.curdir()
PATH = os.path.join ("Day 3 - Output, Algortimo, Condicionais e Repetições", "Arquivos_Manipulados")
os.makedirs(PATH, exist_ok=True)

#Cria diretório do arquivo de texto
arquivo = os.path.join(PATH, "escreva_aqui.txt")

text = [ "Titulo\n",
        "Esse aquivo é texto\n", 
        "blalblalbla\n"]

with open(arquivo, "a") as f: 
   f.writelines(text) #Escreve todo o texto da lista

print (f"Aquivo criado em ", arquivo)