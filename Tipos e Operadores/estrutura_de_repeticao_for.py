texto = input("Informe um texto: ")
VOGAIS = "AEIOU"


# Informa cada vogal que existe mo texto informado
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="") # end substitui o fim do print por algo, neste caso ele dubstitui por um espaço
else:
    print()  # adiciona uma quebra de linha


# Exemplo utilizando a função built-in range
#range(stop) / range(fim)
#range(start, stop, step) / range(inicio, fim, passo)
for numero in range(0, 51, 5):
    print(numero, end=" ")
