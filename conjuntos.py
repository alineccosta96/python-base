'''
Em pyhton, temos o operador set. Ele pode ser representado por: 
a = {1,2,3} ou a= set((1,2,3)) (o último é mais recomendado pq pode ser confundido com lista ou tupla)
'''

# União (pode ser representado por "|" ou union)
# Remove os duplicados - Não garante ordem que retorna no print

conjunto_a = set([1,2,3,4,5]) 
conjunto_b = set([4,5,6,7,8])
conjunto_banana = set("banana") 
print(conjunto_a | conjunto_b)
print(conjunto_a.union(conjunto_b)) 
print(conjunto_banana)

# Interseção (pode ser representado por & ou intersection)
# Mostra quem tem em comum
print(conjunto_a & conjunto_b)
print(conjunto_a.intersection(conjunto_b))

# Diferença (pode ser representado por - ou difference)
# aqui a ordem importa
print(conjunto_a - conjunto_b)
print(conjunto_a.difference(conjunto_b)) # mostra quem está no a e não está no b
print(conjunto_b.difference(conjunto_a)) # mostra quem está no b e não está no a


#Diferença simetrica: Usar somente o que está no A e o que está no B e são diferentes
# pode ser presentado por ^ ou symmetric_difference
print(conjunto_a ^ conjunto_b)
print(conjunto_a.symmetric_difference(conjunto_b))




