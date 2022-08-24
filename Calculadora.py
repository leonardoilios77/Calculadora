
def soma(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def multip(num1, num2):
    return num1 * num2

def elev(num1, num2):
    return num1 ** num2

def div(num1, num2):
    if num1 == 0 and num2 == 0:
        print("Divisão por zero não é possivel \U0001F621")
        main()
    if num2 == 0:
        print("Divisão por zero não é possivel \U0001F621")
        main()     
    return num1 / num2

def seleciona_operacao():
    print("+ soma | - sub | * multip | / div | ** elevado")
    op = input("qual op deseja realizar? ")
    return op

operações = {'+': soma, '-': sub, '*': multip, '/': div, "**": elev}

def num1():
    return float(input("Digite o primeiro valor: "))

def num2():
    return float(input("Digite o segundo valor: "))

def retorna_valor(conta,num1,num2):
    resultado = operações[conta](num1,num2)
    return resultado

def repete_conta(num3):
    conta = seleciona_operacao()
    rp_num1 = num3
    rp_num2 = num2()
    num3 = retorna_valor(conta, rp_num1,rp_num2)
    print(num3) 

    repete = input("Deseja continua? s/n")
    if repete == 's':
          return repete_conta(num3)
    else:
         encerrar = input("Deseja começar nova conta (n) ou encerrar (e) ? \n")
    if encerrar == 'n':
        main()
    else:
        print("Falou meu querido \U0001F604")
    
def main():
    conta = seleciona_operacao()
    numero1 = num1()
    numero2 = num2()
    numero3 = retorna_valor(conta, numero1, numero2)
    print(numero3)
 
    repete = input("Deseja continua? s/n")
    if repete == 's':
          return repete_conta(numero3)
    else:
         encerrar = input("Deseja começar nova conta (n) ou encerrar (e) ? \n")
    if encerrar == 'n':
        main()
    else:
        print("Falou meu querido \U0001F604")

main()



       
       
      
