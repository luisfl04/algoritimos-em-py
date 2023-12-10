# Encontrando o mínimo valor de uma lista:

minha_lista = [4,7,3,9,11]
tam_lista = len(minha_lista)
minimo_valor = minha_lista[0]

for i in range(tam_lista):
    if minha_lista[i] < minimo_valor:
        minimo_valor = minha_lista[i] 

# selection sort:  

def selection_sort(lista):
    for index in range( tam_lista - 1):
        menor_index = index
        for valores in range(index, tam_lista):
            if lista[valores] < lista[menor_index]:
                menor_index = valores
        if lista[index] > lista[menor_index]:
            var_auxiliar = lista[index]
            lista[index] = lista[menor_index]
            lista[menor_index] = var_auxiliar
    print(lista)

selection_sort(minha_lista)
