import csv
import operator

def knn_1element(metric, k, elementToclassify):

    #lista con los k elementos mas cercanos al elementToClassify
    #cada elemento de esta lista es un diccionario con: clase y distancia
    kElementos = []

    with open('data/_train.csv', 'rb') as f:
        setofTrain = csv.reader(f)
        next(setofTrain)

        for line in setofTrain:
            #el primer elemento de la linea es la clase
            clase = int(line[0])
            #el primer elemento de la linea es la clase, asi q la saco del vector
            #ademas convierto el vector de strings a un vector de enteros
            element = map(int, line[1:])

            info_elem = { 'clase': clase, 'distancia': metric(elementToclassify, element) }

            #cargo los k elementos mas cercanos al vector segun vayan apareciendo
            #orderno la lista para q el ultimo elemento siempre sea el mas grande, fiaca
            if (len(kElementos) < k):
                kElementos.append(info_elem)
                kElementos.sort(key = operator.itemgetter('distancia'))
            #si el vector ya tiene k elementos saco al de distancia mayor y
            #en lugar de ese pongo al nuevo elemento que tiene distancia menor
            else:
                if (info_elem['distancia'] < kElementos[k-1]['distancia']):
                    kElementos[k-1] = info_elem
                    kElementos.sort(key = operator.itemgetter('distancia'))

        #lista con la cantidad de apariciones de cada clase que aparecen
        #en la lista de los k elementos mas cercanos
        cantidadXclase = [0] * 10

        for info_elem in kElementos:
            cantidadXclase[info_elem['clase']] += 1


        #busco la clase que tiene mayor cantidad de elementos
        #en la lista de los k elementos mas cercanos
        indiceClaseMayor = 0
        cantidadMayor = 0
        for i in range(0, len(cantidadXclase)):
            if (cantidadXclase[i] > cantidadMayor):
                cantidadMayor = cantidadXclase[i]
                indiceClaseMayor = i

        #devuelvo la clase del elementToclassify
        return indiceClaseMayor