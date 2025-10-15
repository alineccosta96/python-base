'''
Alerta de temperatura
'''
try:
    temperatura = float(input("Digite a tempoeratura: "))
    umidade = float(input("Digite a umidade: "))
    if temperatura < 0:
        print("Alerta: Frio extremo")
    elif temperatura > 0 and temperatura < 10:
        print("Frio")
    elif temperatura > 10 and temperatura < 30:
        print("Normal")
    elif temperatura == ( 3 * umidade) or temperatura == umidade:
        print("Alerta: Perigo de Calor umido")
    elif temperatura > 45:
        print("Alerta: Calor extermo")
except ValueError:
        print("Digite um valor e não um texto")

