# algorítimo para buscar menor valor de uma lista:
lista = [5,7,2,0,9,3]
tamanho = len(lista)
minimo_valor = lista[0]

for i in range(tamanho):
    if lista[i] < minimo_valor:
        minimo_valor = lista[i]
print(minimo_valor)       

#  Selectionsort:

lista = [8,3,6,9,1,2,7]

def Selection_sort(lista):
    tamanho = len(lista)
    for j in range(tamanho - 1, tamanho):
        minimo_index = j
        for i in range(j, tamanho -1):
            if lista[i] < lista[minimo_index]:
                minimo_index = i

        j = 0
        if lista[j] > lista[minimo_index]:
            aux = lista[j]
            lista[j] = minimo_index
            minimo_index = aux

Selection_sort(lista)
print(Selection_sort)