# Encontrando o mínimo valor de uma lista:

minha_lista = [4,7,3,9,11]
tam_lista = len(minha_lista)
minimo_valor = minha_lista[0]

for i in range(tam_lista):
    if minha_lista[i] < minimo_valor:
        minimo_valor = minha_lista[i] 

# selection sort:  

def selection_sort(lista):
    for j in range(tam_lista -1):
        min_index = j
        for i in range(j,tam_lista):
            if lista[i] < lista[min_index]:
                min_index = i
        if lista[j] > lista[min_index]:
            var_auxiliar = lista[j]
            lista[j] = lista[min_index]
            lista[min_index] = var_auxiliar
    print(lista)

# Buble sort:
            
def buble_sort(lista):
    for iteracao_auxiliar in range(tam_lista - 1):
        for iteracao_principal in range(tam_lista - 1):
            if lista[iteracao_principal] > lista[iteracao_principal + 1]:
                var_auxiliar = lista[iteracao_principal]
                lista[iteracao_principal] = lista[iteracao_principal + 1]
                lista[iteracao_principal] = var_auxiliar
    print(lista)



selection_sort(minha_lista)
buble_sort(minha_lista)