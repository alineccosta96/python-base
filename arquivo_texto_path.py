'''
Esse programa deixa de usar o "os.path.join" e usa a lib de path
'''

import os 

from pathlib import Path

# substitui o os.path.join

# Day 3 ... poderia ser substituido por Path('.') que pega o diretório atual 
# sempre fazer para saber onde salvar ou passar o caminho

filepath = Path("Day 3 - Output, Algortimo, Condicionais e Repetições") / Path("Arquivo - PathLib")

# Garante que a pasta existe - parents=True criar todo o caminho das pastas se não existir
# No os.makedirs() já cria os pais automaticamente — por isso não precisa do argumento parents=True
filepath.mkdir(parents=True, exist_ok=True)

# Define o caminho do arquivo
arquivo = filepath / "arquivo_texto_pathlib.txt"

# Escreve no arquivo
with arquivo.open('a') as f:
    f.write("Texto com with - Aline\n")  # fecha aquivo automaticamente

print(f"Arquivo criado em: {arquivo}")

conteudo = arquivo.read_text()
print("Conteúdo do arquivo:", conteudo)

