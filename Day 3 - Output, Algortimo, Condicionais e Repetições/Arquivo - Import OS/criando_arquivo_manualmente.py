'''
Esse programa cria arquivo manualmente precisando o close() para fechar o arquivo.
De preferência sempre usar o jeito de "manipulando_pasta_arquivo" com o with open(arquivo_path, 'w') as f
que fecha automatico.
'''
import os

# Define o caminho da pasta e do arquivo
# Day 3 ... poderia ser substituido por os.curdir() que pega o diretório atual 
# sempre fazer para saber onde salvar ou passar o caminho
PATH = os.path.join("Day 3 - Output, Algortimo, Condicionais e Repetições", "Arquivos_Manuais")
os.makedirs(PATH, exist_ok=True)

#Cria o arquivo
arquivo_path = os.path.join(PATH, "arquivo_manual_log.txt")

# Abre o arquivo manualmente no modo de escrita
f = open(arquivo_path, 'w')  # 'w' = escrita (cria ou sobrescreve)
f.write("Log iniciado manualmente...\n")

# Fecha o arquivo manualmente
f.close()

print(f"Arquivo criado e fechado manualmente em: {arquivo_path}")
