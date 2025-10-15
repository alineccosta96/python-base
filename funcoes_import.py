import random

'''Função que retorna um número aleatório de 1 a 10'''
print(random.randint(1,10))

'''Função que escolhe uma valor aleatorio'''
cores = ['verde', 'vermelho', 'amarelo', 'azul']
print(random.choice(cores))

''' Função que escolhe uma amostragem. Exemplo, pega 2 registros de cores'''
print(random.sample(cores,2))

'''Função shuffle troca os valores dentro de uma lista, ou seja, altera mesmo.
Se cores tem =  'verde', 'vermelho', 'amarelo', 'azul' nessa ordem, ao rodar o comando, 
ele pode inverter ou misturar.
random.shuffle(lista) embaralha os elementos da lista in-place, ou seja, altera a própria lista.'''

random.shuffle(cores)
print(cores)


import itertools as it

'''A função cycle repete o valor até alguma condição de parada break. Nesse caso, ela repete
o 'abcd' várias vezes até nossa condiççao de parada. 
O enumerate é uma função nativa do python para contar'''

for index, item in enumerate(it.cycle('abcd')): 
    print(index, item)
    if index > 3:
        break

'''
A função repeat do módulo itertools serve para repetir um valor várias vezes, criando um iterador infinito (ou limitado, se você especificar um número de repetições).
Por padrão, ela não retorna uma lista, mas sim um objeto iterável. Para visualizar ou manipular os dados, você precisa transformá-lo em uma lista ou consumir com um loop.
'''

repeticao = it.repeat("Aline", 10)
print(repeticao)
print(list(repeticao))

'''A função accumulate também retorna um iterador, e por isso precisa ser consumida (via list() ou for) para mostrar os resultados.
Ela serve para acumular valores de uma sequência. Por padrão, faz a soma progressiva, mas você pode usar outras operações com o argumento func.'''

numeros = [1,2,3,4,5]
acumula = it.accumulate(numeros)
# print(acumula) sempre que retornar assim 'object at 0x000001B1E3872CF0' transforma em lista
print(list(acumula))

'''A função product() gera o produto cartesiano dos elementos fornecidos. Isso significa que ela combina todos os elementos possíveis entre os iteráveis, como se fosse uma multiplicação de conjuntos.
Quando usamos o argumento repeat=2, estamos dizendo que queremos combinar os elementos com eles mesmos, duas vezes.'''

produto = it.product('ABC', repeat=2)
print(list(produto))


'''A função permutations() gera todas as possíveis ordenações (sem repetição de elementos) de um iterável, considerando um número específico de elementos por combinação.
Por padrão, ela usa o comprimento total do iterável, mas você pode passar um segundo argumento para definir o tamanho das permutações.'''


permuta = it.permutations('ABC', 2)
print(list(permuta))


'''A função combinations() gera todas as combinações possíveis de elementos únicos, sem repetição e sem considerar a ordem.
Ou seja, diferente de permutations(), onde a ordem importa, aqui (A, B) é igual a (B, A) — então só aparece uma vez.'''


combinacoes = it.combinations('ABC', 2)
print(list(combinacoes))


import functools as ft
'''
A função partial() serve para criar uma nova função com alguns argumentos já definidos (pré-configurados). É muito útil quando você quer reutilizar uma função com certos parâmetros fixos.
Você está criando uma versão personalizada da função print, onde o separador (sep) entre os argumentos será sempre '---'.
'''
myprint = ft.partial(print, sep='---')
myprint("Aline", "Costa")

import statistics as st

'''statistics.mean() calcula a média aritmética dos valores em uma lista'''
notas = [1,2,3,4,5,5,5]
print(st.mean(notas))

'''statistics.median() calcula a mediana aritmética dos valores em uma lista'''
print(st.median(notas))

import getpass 

'''O módulo getpass é usado para capturar entradas do usuário sem exibir o que está sendo digitado no terminal — ideal para senhas ou informações sensíveis.'''

senha = getpass.getpass("Digita a senha:")

'''getuser mostra o usuário do sistema operacional'''
print(getpass.getuser())