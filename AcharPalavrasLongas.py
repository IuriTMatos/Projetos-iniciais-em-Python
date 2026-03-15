texto = input("Digite um texto: ")

palavras = texto.split()
palavras_longas = []
print("")
for palavra in palavras:
    if len(palavra) > 10:
        palavras_longas.append(palavra)

if len(palavras_longas) > 0:
    print(f"Palavras longas encontradas:", {", ".join(palavras_longas)})

else:
    print("nenhuma palavra encontrada")