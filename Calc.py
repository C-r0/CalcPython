// Pergunta ao usuario a opção que deseja e armazena na variavel numC
numC = int(input("1: Somar 2: Subtrair 3: Multiplicação 4: Divisão "))
// Verifica se numC é maior que 4 assim a opção sendo invalida
if numC > 4:
    print("Coloque uma opção valida.")
    quit()
// Variavel num1 onde tem o primeiro numero
num1 = int(input("Primeiro Numero: "))
// Variavel num2 onde tem o segundo numero
num2 = int(input("Segundo Numero: "))
// Verifica se numC é 1 assim somando os valores
if numC == 1:
    Resultado = num1 + num2
    print("A Resposta de Sua Soma é:", Resultado)
// Verifica se numC é 2 assim subtraindo os valores
if numC == 2:
    Resultado = num1 - num2
    print("A Resposta de Sua Subtração é:", Resultado)
// Verifica se numC é 3 assim multiplicando os valores
if numC == 3:
    Resultado = num1 / num2
    print("A Resposta de Sua Multiplicação é:", Resultado)
// Verifica se numC é 4 assim dividindo os valores
if numC == 4:
    Resultado = num1 * num2
    print("A Resposta de Sua Divisão é:", Resultado)
    
// Fiz para não fechar o cmd ao abrir
input()
