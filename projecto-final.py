# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 17:07:00 2017

@author: Luis Nerio
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 01:57:05 2017

@author: Luis Nerio
"""

import random
import numpy
import copy

"""******************************************************************************************
############################################################################################
Función para crear números aleatorios, toma como parametros n, que es la cantidad de números
que deseas y  lim_inf y lim_sup que son parametros para indicar el intervalo en el que deben
estar los números aleatorios generados
############################################################################################
******************************************************************************************"""
def ran_num(n,lim_inf=0, lim_sup=100):
    arreglo = []
    for i in range(n):
        arreglo.append(random.randint(lim_inf, lim_sup))
    return arreglo


"""******************************************************************************************
############################################################################################
                                    Quicksort
Función para ordenar un arreglo de longitud arbitraria con el algoritmo quicsort , toma como
parametro el arreglo, el indice menor y mayor del arreglo
############################################################################################
******************************************************************************************"""
def quicksort(arreglo,low,high ):
    if low < high:
        m = particion(arreglo, low, high)    
        quicksort(arreglo,low,m-1)
        quicksort(arreglo, m+1 , high)


"""******************************************************************************************
############################################################################################
                                    Partición
Función para realizar una subrutina del algoritmo quicksort
la función regresa el indice del valor pivote en su orden respectivo en el arreglo
############################################################################################
******************************************************************************************"""
def particion(arreglo, low, high):
    pivote = arreglo[high]
    wall = low-1
    for j in range(low, high):
        if arreglo[j]<pivote:
            wall = wall + 1
            swap(arreglo,wall,j)
    if(arreglo[high]< arreglo[wall+1]):
        swap(arreglo,wall+1,high)
    return wall+1

"""******************************************************************************************
############################################################################################
                                            swap
Función que realiza un intercambio de posición de valores dentro de un arreglo, toma como parametros
el arreglo  y los indices de los valores a cambiar
############################################################################################
******************************************************************************************"""
def swap(arreglo, a, b):
    aux = arreglo[a]
    arreglo[a]= arreglo[b]
    arreglo[b]= aux


"""******************************************************************************************
############################################################################################
                                            Mediana
Función que encuentra la mediana de un arreglo
############################################################################################
******************************************************************************************"""

def mediana(arr):
        if (((len(arr))%2)!=0):
            med=        arr[int(len(arr)/2)] 
        else:
            med =    (arr[int(len(arr)/2)-1]+arr[int(len(arr)/2)] ) /2 
        return med
        


###########################################################################
#Ejemmplo
###########################################################################
arr1 = ran_num(6)                             ##arreglo desordenado
arr2 = copy.deepcopy(arr1)                               ##arreglo ordenado
quicksort(arr2,0,len(arr2)-1) 
print("Arreglo desordenado", arr1)
print("Arreglo ordenado" ,arr2)


print("\n" +"Mediana calculada con funcion de python " + str(numpy.median(arr1 )) )
print("Mediana calculada con funcion de Reynolds y Daniela " + str(mediana(arr2)))





