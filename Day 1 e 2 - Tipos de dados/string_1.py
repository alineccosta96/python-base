nome = "Aline"
sobrenome = "Costa"

print(nome[0]) #Retorna a primeira letra "A"
print(nome.startswith("a")) #Verifica se a primeira letra é "a"
print(nome.endswith("e")) #Verifica se a última letra é "e"

print(sorted(nome)) #Ordena os caracteres de acorodo com a posição na tabela ascii

irma = "alana costa"

print(irma.capitalize()) #Retorna a primeira letra maiscula
print(irma.title()) #Retorna as primerias letras maiiscula
print(irma.split()) #Separa em "listas"

nome_1 = input("Qual seu nome? ").strip()  
#função TRIM do SQL / tb tem o lstrip 
# pode ser usado como strip('-') que remove o caractere que está entre (), no caso o '-' 
idade = int(input("Qual sua idade? ")) 
#precisa sempre converter o tipo de dado se não ele entende como string

if idade > 18:
    print("Parabéns, vc é maior de idade")