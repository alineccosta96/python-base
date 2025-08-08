import pprint 

#Dados 
sala1 = ["Pedro", "Aline", "Barbara", "Miguel", "Lucas"] 
sala2 = ["Matheus", "Eric", "Patricia", "Carol"] 

#Aulas 
aula_ingles = { "alunos": ["Pedro", "Aline", "Matheus", "Patricia"] } 
aula_musica = { "alunos": ["Aline", "Carol", "Lucas", "Matheus", "Eric"] } 
aula_danca = { "alunos": ["Eric", "Barbara", "Patricia", "Carol"] } 

#Atividades - Fiz uma lista e dentro várias tuplas de nome + lista de atividades 
atividades = [("Inglês", aula_ingles), ("Música", aula_musica), ("Dança",aula_danca)] 
#pprint.pprint(atividades) 

for nome_atividade, atividade in atividades: 
    sala1_atividades = [] 
    sala2_atividades = [] 
    for chave, lista_aluno in atividade.items(): 
        #print(lista_aluno)      
        for aluno in lista_aluno:
            if aluno in sala1: 
                sala1_atividades.append(aluno) 
            if aluno in sala2: 
                sala2_atividades.append(aluno) 
    print(f"A {nome_atividade} tem os alunos da sala 1: ", sala1_atividades)  
    print(f"A {nome_atividade} tem os alunos da sala 2: ", sala2_atividades)  
    print('#' * 50)