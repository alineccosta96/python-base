'''
Exibe um relatório de crianças por atividades.

Imprimir a lista de crianças agrupadas por sala que frequenta cada uma das
atividades. 
É o mesmo da versão v1, mas, agora usaremos interseção para diminuir processamento. 
Já que o for percorre toda a lista e o set é mais rápido.
''' 
__version__ = '0.1.1'
__autor__ = 'Aline'

#Dados
sala1 = ["Pedro", "Aline", "Barbara", "Miguel", "Lucas"]
sala2 = ["Matheus", "Eric", "Patricia", "Carol"]

#Aulas
aula_ingles = ["Pedro", "Aline", "Matheus", "Patricia"]
aula_musica = ["Aline", "Carol", "Lucas", "Matheus", "Eric"]
aula_danca = ["Eric", "Barbara", "Patricia", "Carol"]

#Atividades - Fiz uma lista e dentro várias  tuplas de nome + lista de atividades

atividades = [("Inglês", aula_ingles), ("Música", aula_musica), ("Dança",aula_danca)]

# Busca o que tem em comum entre lista de alunos e atividades
# Aqui não tem for. O for é substituido por intersection. 
# Em sala 1 busca os nomes de alunos entro de atividades

for nome_atividade, atividade in atividades:
    sala1_atividades = set(sala1).intersection(set(atividade))
    sala2_atividades = set(sala2).intersection(set(atividade))  
    print(f"A {nome_atividade} tem os alunos da sala 1: ",sala1_atividades)  
    print(f"A {nome_atividade} tem os alunos da sala 2: ",sala2_atividades)  
    print('#' * 50)
    
    
