nome = "Guilherme"
idade = 26
profissao = "Programador"
linguagem = "Python"
saldo = 49.475

dados = {"nome":"Guilherme", "idade": 26}

print("Nome : %s , idade: %d" %(nome, idade))
print("Nome : {} , idade: {}" .format(nome, idade))
print("Nome : {nome} , idade: {idade}" .format(**dados))
print(f"Nome: {nome}, idade: {idade}, saldo: {saldo: 2.2f}")