'''
Exibe um relatório de crianças por atividades.

Imprimir a lista de crianças agrupadas por sala que frequenta cada uma das
atividades
'''
__version__ = '0.1.0'
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


for nome_atividade, atividade in atividades:
    sala1_atividades = []
    sala2_atividades = []
    for aluno in atividade:
        if aluno in sala1:
            sala1_atividades.append(aluno)
        elif aluno in sala2:
            sala2_atividades.append(aluno)
    print(f"A {nome_atividade} tem os alunos da sala 1: ",sala1_atividades)  
    print(f"A {nome_atividade} tem os alunos da sala 2: ",sala2_atividades)  
    print('#' * 50)
    
    
