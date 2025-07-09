'''
Você tem uma lista de crianças com suas respectivas salas e atividades. 
Crie um relatório que agrupa as crianças por atividade, e dentro de cada atividade, organiza por sala.
'''

crianças = [
    ("Ana", "Sala 1", "Pintura"),
    ("Bruno", "Sala 2", "Futebol"),
    ("Carla", "Sala 1", "Pintura"),
    ("Daniel", "Sala 2", "Música"),
    ("Eva", "Sala 1", "Futebol"),
    ("Felipe", "Sala 2", "Pintura"),
]

atividade_pintura_sala1 = []
atividade_pintura_sala2 = []
atividade_futebol_sala1 = []
atividade_futebol_sala2 = []
atividade_musica_sala1  = []
atividade_musica_sala2  = []


for crianca, sala, atividade in crianças: 
    match sala:
        case  "Sala 1":
            if atividade == "Pintura":
                atividade_pintura_sala1.append(crianca)
            if atividade == "Futebol":
                atividade_futebol_sala1.append(crianca)
            if atividade == "Música":
                atividade_musica_sala1.append(crianca)
        case  "Sala 2":
            if atividade == "Pintura":
                atividade_pintura_sala2.append(crianca)
            if atividade == "Futebol":
                atividade_futebol_sala2.append(crianca)
            if atividade == "Música":
                atividade_musica_sala2.append(crianca)

print("=" * 15)
print("Relatório de crianças por sala e atividade: ")
print("=" * 15)
atividade_unica = []
for _, _, atividade in crianças: 
    if atividade not in atividade_unica:
        atividade_unica.append(atividade)
for atividade in atividade_unica:
    print(f"Atividade: {atividade}")
    if atividade == "Pintura": 
        print(f"Sala 1: {atividade_pintura_sala1}")
        print(f"Sala 2: {atividade_pintura_sala2}")
    print("=" * 15)
    if atividade == "Futebol":  
        print(f"Sala 1: {atividade_futebol_sala1}")
        print(f"Sala 2: {atividade_futebol_sala2}")
    print("=" * 15)
    if atividade == "Música": 
        print(f"Sala 1: {atividade_musica_sala1}")
        print(f"Sala 2: {atividade_musica_sala2}")
    print("=" * 15)





#explode por atividade, dps por sala e faz o append da crianca




       
        
