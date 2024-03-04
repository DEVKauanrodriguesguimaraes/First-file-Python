
def sacar(valor_saque: float):
    saldo = 500

    if saldo >= valor_saque:
        saldo -= valor_saque
        print("Valor sacado")
        mensagem = f"O saldo atual é {saldo}"
        print(mensagem)
       
sacar(100)
print("Obrigado por ser nosso cliente")

