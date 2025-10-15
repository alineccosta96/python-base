'''Exemplo de criação de função. '''

# Em python toda função começa a ser escrita como def e tem que ter um retorno

#SOLID - Single Responsibility - cada função faz um papel

def f(x):
    result = 5 * (x / 2)
    return result

if f(10) == 25: 
    print(f(10))

# Funcao que não tem retorno é uma procedure

def print_upper(text):
    print(text.upper())

print_upper("aline")

'''
Vamos calcular a A Fórmula de Heron: 
é uma maneira elegante de calcular a área de um triângulo quando você conhece 
apenas os comprimentos dos três lados — sem precisar saber a altura.
'''

import math

#Podemos definir a função como heron(a,b,c) (chama-se argumentos posicionais) 
# ou heron( a:int, b:int, c:int) -> int (chama-se argumentos nominais)
# QUe mostra cada tipo das variaveis e mostra o retorno dela que é "-> int"

def heron(a, b, c):
    perimeter = a+b+c
    sp = perimeter/2
    area = sp * ((sp - a) * (sp - b) * (sp - c))
    result = math.sqrt(area)
    return result

triangulos = {
    (5,8,12),
    (6,9,10)
}

for t in triangulos: 
    #print(f"A area do triangulo é: ", heron(a=t[0], b=t[1], c=t[2]))
    print(f"A area do triangulo é: ", heron(t[0], t[1], t[2]))

def oi():
    return ("Olá")
    
print(oi())

#argumentos nomianis
def outra_funcao(a: int, b: int, c: int):
    '''
        Essa função é só um teste de tuplas
    '''
    return a*2 , b*2 , c*2

print(outra_funcao(1,2,3))

valor_1, valor_2, valor_3 = outra_funcao(1,2,3)
print(valor_1, valor_2, valor_3)

#Pegar somente o primeiro valor. Na tupla o *_ ignora todo o resto
valor_1, *_ = outra_funcao(1,2,3)
print(valor_1)

args = {"n1": 20, "n2":30, "n3": 60}
resposta = outra_funcao(args["n1"], args["n2"], args["n3"])
print(resposta)

#=========================================

# fazer coisas interessantes com elas como atribuição de multiplas variáveis e desempacotamento.

coordenadas = 1, 2, 3  # atribuição multipla
x, y, x = coordenadas  # desempacotamento

# Isto também é bastante útil em funções pois elas podem retornar tuplas.

def nome_da_funcao():
    return 1, 2, 3  # tupla

x, y, z = nome_da_funcao()

# E também podemos usar o desempacotamento para passar argumentos para funções, neste caso usamos um * para forçar o desempacotamento.

triangulo = (3, 4, 5)
area = heron(*triangulo)  # desempacotamento das posições da tupla
print(f"A area do triangulo é {area}")

# E o mesmo funciona quando os valores estão em um dicionário.

triangulo = {'a': 3, 'b': 4, 'c': 5}
area = heron(**triangulo)  # desempacotamento dos valores do dicionário
print(f"A area do triangulo é {area}")


# Os argumentos de uma função podem ter um valor por defeito, em inglês default que é 
# o valor que será assumido caso nenhum valor seja passado.

def imprime_nome(nome, sobrenome="Sabugosa"):
    print(nome, sobrenome)

imprime_nome("Bruno")
# Bruno Sabugosa

imprime_nome("Bruno", "Rocha")
# Bruno Rocha


#Aplicando funções me funções: ver lambdas.py

