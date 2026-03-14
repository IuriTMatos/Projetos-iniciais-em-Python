total = float(int(input("Digite o Valor Total da Conta: ")))
gorjeta = float(int(input("Digite a Porcentagem da Gorjeta: ")))
print("-" * 35)

def calcular_gorjeta(total, gorjeta):
    return total * (gorjeta / 100)

print(f"O valor da gorjeta é: R${calcular_gorjeta(total, gorjeta)}")
print(f"O valor total a ser pago é: R${total + calcular_gorjeta(total, gorjeta)}")