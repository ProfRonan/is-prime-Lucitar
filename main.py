a = int(input())

if a <= 0:
    print("Número inválido")
else:
    div = 0
    for i in range(1, a):
        if a % i == 0:
            div += 1
    if div == 1:
        print("Primo")
    else:
        print("Não primo")

