#Operadores Logicos

#(and) Retorna True se ambas as comparações forem verdadeiras.
a = 10
b = 5
c = 7
resultado = (a > b) and (c < a)  # resultado é True

#(or) Retorna True se pelo menos uma das comparações for verdadeira.
a = 10
b = 5
c = 12
resultado = (a > b) or (c < b)  # resultado é True

#(not) Inverte o resultado da comparação.
a = 10
b = 5
resultado = not (a < b)  # resultado é True, porque a < b é False