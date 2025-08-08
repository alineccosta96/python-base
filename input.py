nome = input("Qual seu nome? ").strip()  
#função TRIM do SQL / tb tem o lstrip 
# pode ser usado como strip('-') que remove o caractere que está entre (), no caso o '-' 
idade = int(input("Qual sua idade? ")) 
#precisa sempre converter o tipo de dado se não ele entende como string

if idade > 18:
    print("Parabéns, vc é maior de idade")