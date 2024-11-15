num1 = int(input("Digite o primeiro número para a operação: "))
num2 = int(input("Digite o segundo número: "))

operacao = input("Digite o método de operação (+, -, *, /): ")

if operacao == '+':
    print(num1 + num2)
elif operacao == '-':
    print(num1 - num2)
elif operacao == '*':
    print(num1 * num2)
elif operacao == '/':
    print(num1 / num2)
else:
    print("Operação Inválida!")