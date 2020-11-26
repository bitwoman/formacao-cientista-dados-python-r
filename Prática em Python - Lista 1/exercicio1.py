#1. Faça um programa que tenha uma função chamada amplitude. A função deve receber uma lista e imprimir a amplitude.
#Crie também um código para testar sua função.
def amplitude(getList):
    maxList = max(getList)
    minList = min(getList)
    amplitudeList = maxList - minList
    
    return amplitudeList
    
amplitude([1,2,3,4,5,6,7,8,9,10])
