def coleta_entrada():
    x = int(input('n: '))
    while x <= 0:
        x = int(input('n: '))
    return x

def conta_divisores(y):
    qtd = 0
    for divisor in range(1, y+1):
        resto = y % divisor
        if resto == 0:
            qtd = qtd + 1
    return qtd

def primo(x):
    return conta_divisores(x) == 2

# Essa função exibe no intervalo de de dois numeros os primos crescentes
def crescentePrimos(a, b):
    for num in range(a, b+1):
        if primo(num):
            print(num)

a = int(input())
b = int(input())
crescentePrimos(a, b)


