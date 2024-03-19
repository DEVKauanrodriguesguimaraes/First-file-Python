## Conhecendo métodos úteis na classe string
nome = "kaUan"
print(nome.upper())
print(nome.lower())
print(nome.title())

## Eliminando espaço em branco
texto = "  Olá Mundo    "
print(texto + ".")
print(texto.strip()+ ".")
print(texto.rstrip()+ ".")
print(texto.lstrip()+ ".")

## Junções e centralização
menu = "Python"
print("##"+ menu + "##")
print(menu.center(10, "#"))
print(menu.center(10))
print("P-y-t-h-o-n")
print("-".join(menu))
