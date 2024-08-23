nome = "pAULo"
#Maiusculo, Minusculo e Titulo
print(nome.upper())
print(nome.lower())
print(nome.title())

texto = "  Olá mundo!    "

#Eliminando espaços da string
#strip remove da direita e da esquerda
#rstrip da direita, lstrip da esquerda
print(texto + ".")
print(texto.strip() + ".")
print(texto.rstrip() + ".")
print(texto.lstrip() + ".")

menu = "Python"

#Junção e Centralização
#center acrecenta o numero de caracteres que vc informar a string string_nome.center(10,#) 
# o segundo campo informa com qual caractere voce quer preencher
print("####" + menu + "####")
print(menu.center(14))
print(menu.center(14, "#"))
#join voce informa qual caracter voce que juntar e entre parenteses a variavel ".".join(variavel) 
print("-".join(menu))