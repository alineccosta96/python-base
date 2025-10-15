# Conseguimos usar funções em funções

def transforma_minusculo (texto):
    return texto.lower()

def transforma_maisculo (texto):
    return texto.upper()

def divide_por2(numero): 
    return numero / 2

def faz_algo(valor,funcao):
    print(f"Aplicando {funcao} em {valor}")
    return funcao(valor)

retorno = faz_algo("Aline", transforma_maisculo)
print(retorno)

# Lambda: Ele é útil quando você precisa de uma função simples e rápida, 
# geralmente como argumento de outra função, sem a necessidade 
# de definir uma função completa com def.
# chamado de função anonima
print(faz_algo(10, lambda numero: numero * 3))