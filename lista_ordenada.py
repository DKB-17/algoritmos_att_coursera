def ordenada(lista):
    for i in range(len(lista)-1):
        if lista[i] > lista[(i+1)]:
            return False
    return True

lista1 = [10,20,30,40,50,60]

print(ordenada(lista1))