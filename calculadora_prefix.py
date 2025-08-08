''''
Esse programa tem como objetivo o usuário digitar a operação e dois numero e calcular o retorno.

Operações: 
sum -> +
sub -> -
mult -> * 
div -> /
'''
__version__ = '0.1'
__author__ = "Aline Costa"


argumentos = {
    "sum": '+',
    "sub": '-',
    "mult": '*', 
    'div': '/'
}

operacao = input("Digite a operação: ")


if operacao not in argumentos.keys():
    print(f"Operação Inválida!")
else:
    # Basicamente eu disse: argumentos["sum"] 
    # que é: Pegue o valor correspondente à chave que o usuário digitou.
    simbolo = argumentos[operacao]   
    print(f"A operação escolhida foi: {simbolo}")  
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    if simbolo == '+':        
        total = num1 + num2
    elif simbolo == '-':       
        total = num1 - num2
    elif simbolo == '*':        
        total = num1 * num2
    elif simbolo == '/':        
        total = num1 / num2

print(f"O total da operação é:", total)



