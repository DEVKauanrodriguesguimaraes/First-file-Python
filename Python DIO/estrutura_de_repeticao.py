texto = input("informe um texto:")
VOGAIS = "A, E, I, O, U"

#Exemplo utilizando iterário:
for letra in texto:
     if letra.upper() in VOGAIS:
          print(letra, end=" ")
else:
    print(end="\n")

#Exemplo utilizando built-in range:
for numero in range(0,81,8):
     print(numero, end=" ")

