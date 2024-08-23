# Operador 'in'
frutas = ['maçã', 'banana', 'laranja']

print('banana' in frutas)  # True, porque 'banana' está na lista 'frutas'
print('uva' in frutas)     # False, porque 'uva' não está na lista 'frutas'

# Operador 'not in'
print('uva' not in frutas)  # True, porque 'uva' não está na lista 'frutas'
print('maçã' not in frutas) # False, porque 'maçã' está na lista 'frutas'
#Uso com Strings

texto = "Python é incrível"
print('Python' in texto)      # True, porque 'Python' está em 'texto'
print('python' in texto)      # False, porque a busca é sensível a maiúsculas e minúsculas
print('Python' not in texto)  # False, porque 'Python' está em 'texto'

#Uso com Dicionários

pessoa = {'nome': 'João', 'idade': 30}
print('nome' in pessoa)       # True, porque 'nome' é uma chave no dicionário 'pessoa'
print('João' in pessoa)       # False, porque 'João' não é uma chave, mas sim um valor
print('idade' not in pessoa)  # False, porque 'idade' é uma chave no dicionário 'pessoa'