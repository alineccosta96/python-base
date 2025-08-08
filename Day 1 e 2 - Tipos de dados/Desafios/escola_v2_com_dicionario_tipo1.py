'''
Exibe um relatório de crianças por atividades.

Imprimir a lista de crianças agrupadas por sala que frequenta cada uma das
atividades. 
É o mesmo da versão v1, mas, agora usaremos interseção para diminuir processamento. 
Já que o for percorre toda a lista e o set é mais rápido.
''' 
__version__ = '0.1.2'
__autor__ = 'Aline'

import pprint

#Dados
sala1 = ["Pedro", "Aline", "Barbara", "Miguel", "Lucas"]

sala2 = ["Matheus", "Eric", "Patricia", "Carol"]

#Aulas

aula_ingles = {
    "alunos": ["Pedro", "Aline", "Matheus", "Patricia"]
}

aula_musica = {
    "alunos": ["Aline", "Carol", "Lucas", "Matheus", "Eric"]
}

aula_danca = {
    "alunos": ["Eric", "Barbara", "Patricia", "Carol"]
}

#Atividades - Fiz uma lista e dentro várias  tuplas de nome + lista de atividades

atividades = [("Inglês", aula_ingles), ("Música", aula_musica), ("Dança",aula_danca)]


#pprint.pprint(atividades)

for nome_atividade, atividade in atividades:
    sala1_atividades = []
    sala2_atividades = []

    alunos = atividade["alunos"]  
    # atividade -> tem a estrutura ('Inglês', {'alunos': ['Pedro', 'Aline', 'Matheus', 'Patricia']})
    # portanto preciso pegar somente o que tem dentro de "alunos" para retornar só a lista
    #print(alunos)

    for a in alunos:
        if a in sala1: 
            sala1_atividades.append(a)
        if a in sala2: 
            sala2_atividades.append(a)
    print(f"A {nome_atividade} tem os alunos da sala 1: ", sala1_atividades)  
    print(f"A {nome_atividade} tem os alunos da sala 2: ", sala2_atividades)  
    print('#' * 50)
    
 
           
    



    
