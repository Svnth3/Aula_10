
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


numero1 = float(input("Informe o primeiro número: "))
numero2 = float(input("Informe o segundo número: "))


soma = adicionar(numero1, numero2)
sub = subtrair(numero1, numero2)
div = dividir(numero1, numero2)
mult = multiplicar(numero1, numero2)

print(f'O resultado da soma é {soma}.')
print(f'O resultado da subtação é {sub}.')
print(f'O resultado da divisão é {div}.')
print(f'O resultado da multiplicação é {mult}.')
