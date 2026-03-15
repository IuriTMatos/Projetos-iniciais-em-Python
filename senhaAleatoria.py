import random
import string

# Garantir pelo menos de um de cada tipo

maiscula = random.choice(string.ascii_uppercase)
minuscula = random.choice(string.ascii_lowercase)
numero = random.choice(string.digits)
especial = random.choice(string.punctuation)

# print(f"Maiscula:", maiscula)
# print(f"minuscula:", minuscula)
# print(f"numero:", numero)
# print(f"especial:", especial)

# juntar todos os caracteres possíveis

todos = string.ascii_letters + string.digits + string.punctuation

#completar até 12 caracteres
restante = [random.choice(todos) for _ in range(8) ]

# juntar tudo

senha_lista = [maiscula, minuscula, numero, especial] + restante

# Embaralhar a senha

random.shuffle(senha_lista)

# transformar em string

senha = "".join(senha_lista)

print(f"Senha gerada: {senha}")