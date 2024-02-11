numC = int(input("1: Somar 2: Subtrair 3: Divisão 4: Multiplicaçao "))
if numC > 4:
    print("Coloque uma opção valida.")
    quit()

num1 = int(input("Primeiro Numero: "))
num2 = int(input("Segundo Numero: "))
if numC == 1:
    num3 = num1 + num2
    print("A Resposta de Sua Soma é:",num3)
if numC == 2:
    num4 = num1 - num2
    print("A Resposta de Sua Subtração é:", num4)
if numC == 3:
    num5 = num1 / num2
    print("A Resposta de Sua Divisão é:", num5)
if numC == 4:
    num6 = num1 * num2
    print("A Resposta de Sua Multiplicação é:",num6)

input()
