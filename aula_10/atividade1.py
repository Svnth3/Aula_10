import random
import os
os.system('cls')


def adicionar(n1, n2): 
    resultado = n1 + n2
    return resultado


def subtrair(n1, n2):
    resultado = n1 - n2
    return resultado


def dividir(n1, n2):
    resultado = n1 / n2
    return resultado


def multiplicar(n1, n2):
    resultado = n1 * n2
    return resultado


numero1 = random.randint(1, 100)
numero2 = random.randint(1, 100)
print('multiplicar [*], adição [+], divisão [/], subtração [-]')
operacao = input("Qual operação: ")
print(f'Os numeros gerados foram {numero1} e {numero2}')

soma = adicionar(numero1, numero2)
sub = subtrair(numero1, numero2)
div = dividir(numero1, numero2)
mult = multiplicar(numero1, numero2)

match operacao:
    case "+":
        print(f'O resultado da soma é {soma}.')
    case "-":
        print(f'O resultado da subtação é {sub}.')
    case "/":
        print(f'O resultado da divisão é {div}.')
    case "*":
        print(f'O resultado da multiplicação é {mult}.')
    case _:
        print("Operador inválido")