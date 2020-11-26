#2. Faça uma função que receba uma string e imprima esta string na forma vertical. Por exemplo, se receber python, deve imprimir:
#Dica: uma string do python funciona como uma lista! Crie também um código para testar sua função.
def vertical(string):
    for s in range(0, len(string)) :
        print(string[s])

vertical('python')   
