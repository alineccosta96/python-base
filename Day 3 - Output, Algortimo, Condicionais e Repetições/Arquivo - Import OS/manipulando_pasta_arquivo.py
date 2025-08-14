'''
Esse programa cria arquivo manualmente e não precisado close para fechar o arquivo. 
Usando os.path.join
'''

import os 

# Mostrar uma lista de arquivos que estão no diretório
## print(os.listdir('.'))

#Cria uma subspasta chamada arquivo e se exsitir, ignora a criação
## os.makedirs('Day 3 - Output, Algortimo, Condicionais e Repetições/Arquivos', exist_ok=True)

#Lista tudo que está dentro da pasta "Day 3"
# print(os.listdir('Day 3 - Output, Algortimo, Condicionais e Repetições'))


# Em Microsoft é '/' em Linux é '\' 
# Para saber qual usar o ideial é criar uma var de PATH com os.path.join
# Ela é responsável por criar o caminho e já trata a questão das barrar

# Day 3 ... poderia ser substituido por os.curdir() que pega o diretório atual 
# sempre fazer para saber onde salvar ou passar o caminho
PATH = os.path.join("Day 3 - Output, Algortimo, Condicionais e Repetições", "Arquivos_Manipulados")
os.makedirs(PATH, exist_ok = True)

# Cria o arquivo de forma segura (aqui só monta o caminho do arquivo_manipulados_log.txt)
arquivo_path = os.path.join(PATH, "arquivo_manipulados_log.txt")

# Cria o arquivo oficialmente: open(arquivo_path, 'w')

# r -> Indica que estamos abrindo o arquivo no modo de leitura
# w -> Indica que estamos abrindo o aquivo no modo de escrita
# a -> Indica que estamos abrindo oa arquivo de modo de escrita e APPEND (sem apagar nada)

# Esse bloco automaticamente fecha o arquivo quando termina, então você não precisa chamar close() manualmente.
with open(arquivo_path, 'w') as f:
    f.write("Log iniciado...\n")
    # Tem que colocar \n para na próxima escrita quebrar a linha

print(f"Arquivo criado em: {arquivo_path}")
leitura = (open(arquivo_path, 'r'))
print(leitura.read()) #Aqui ele retorna o que tem dentro do arquivo
print(leitura.read()) 
# Aqui ele já retorna vazio. Pq toda vez que rodamos um read ele lê linha a linha e para de ler de onde parou.
# ótimo para incremetar arquivos. 
# Se quiser ler novamente o arquivo, antes do leitura.read() é só abrir o arquivo novamente open(arquivo_path, 'r')
