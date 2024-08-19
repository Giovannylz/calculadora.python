def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Erro: Divisão por zero não é permitida."
    return a / b

def calculator():
    print("Calculadora simples")
    print("Escolha uma operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    while True:
        choice = input("Digite o número da operação (1/2/3/4) ou 'sair' para encerrar: ")
        
        if choice == 'sair':
            print("Saindo da calculadora.")
            break

        if choice in ['1', '2', '3', '
