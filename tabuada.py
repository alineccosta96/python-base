'''
Esse programa imprime a tabuada do 1 ao 10.

---Tabuada 1---:
    1 X 1 = 1
    1 X 2 = 2
    1 X 3 = 3
...

##########
---Tabuada 2---:
    2 X 1 = 2
    2 X 2 = 4
'''
__version__ = '0.1.1'
__author__ = "Aline Costa"

#numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros = list(range(1,11))
# range não é incremental para ir até o último sempre colcoar +1

# para cada numero (singular) em numeros (plural - pega o range)
for numero in numeros:
    tabuada = f"Tabuada do {numero}"    
    print("{:-^30}".format(tabuada))
    print() #linha em branco
    for outro_numero in numeros:  
        cal = f"{numero} * {outro_numero} = {numero * outro_numero}"
        print("{:^20}".format(cal))
    print() #linha em branco        
    print("#" * 30)