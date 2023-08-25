# 2𝑥² + 2𝑥 − 6

def fx():
    print('Sabendo que a equação de segundo grau é determinada por ax² + bx - c, informe: ')
    a = int(input('O valor de a: '))
    b = int(input('O valor de b: '))
    c = (int(input('O valor de c: ')) * (-1))

    delta = b ** 2 - 4 * a * c

    x1 = (-b + (delta ** (1 / 2))) / (2 * a)
    x2 = (-b - (delta ** (1 / 2))) / (2 * a)

    for calculo in (x1, x2):
        print(calculo)


fx()
