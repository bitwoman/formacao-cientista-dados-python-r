#3. Crie um programa que leia o peso de uma carga em números inteiros. Se o peso for até 10 kg, informe que o valor será de R$ 50,00. 
#Entre 11 e 20 kg, informe que o valor será de R$ 80. Se for maior que 20 informe que o transporte não é aceito. Teste vários pesos.
weightLoad = int(input('Enter the weight of load: '))

if(weightLoad <= 10):
    print('The price is $50.00')
elif(weightLoad >= 11 and weightLoad <= 20):
    print('The price is $80.00')
else:
    print('Shipping is not accepted!')
