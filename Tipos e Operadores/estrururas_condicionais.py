idade = int(input("Informe sua idade: "))

if idade >= 18:
    print("Maior de idade, pode tirar a CHN.")
else:
    print("Ainda não pode tirar a CNH.")

if idade >= 18:
    print("Maior de idade, pode tirar a CHN.")
elif idade == 17:
    print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas.")
else:
    print("Ainda não pode tirar a CNH.")

