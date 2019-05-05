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
        

n = coleta_entrada()
if primo(n):
    print("É primo")
else:
    print("Nao é primo")
