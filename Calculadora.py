
def soma(num1, num2):
    num1 = int(input(f'Digite o primeiro valor a somar: '))
    num2 = int(input(f'Digite o segundo valor a somar: '))
    return num1 + num2

def subtrair(num1, num2):
    num1 = int(input(f'Digite o primeiro valor a subtrair: '))
    num2 = int(input(f'Digite o segundo valor a subtrair: '))
    return num1 - num2

def multiplicar(num1, num2):
    num1 = int(input(f'Digite o primeiro valor a multiplicar: '))
    num2 = int(input(f'Digite o segundo valor a multiplicar: '))
    return num1 * num2

def dividir(num1, num2):
    num1 = int(input(f'Digite o primeiro valor a dividir: '))
    num2 = int(input(f'Digite o segundo valor a dividir: '))
    return num1 / num2

num1 = 0
num2 = 0
calcula = 'calcula'

for x in calcula:
    x = (input('Qual operação deseja efetuar? '))
    if x == '+':
        print(soma(num1, num2))
    if x == '-':
        print(subtrair(num1, num2))
    elif x == '*':
        print(multiplicar(num1, num2))
    elif x == '/':
        print(dividir(num1, num2))




       
       
      