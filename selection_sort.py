def ordena(lista):
    for i in range(len(lista)-1):
        for j in range(i,len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista