palavra = "python"
palavra_secreta = "_" * len(palavra)
letras_adivinhadas = []
max_tentativas = 5

while True:
    print(palavra_secreta)
    letra = input("Digite uma letra: ").lower()

    if letra in letras_adivinhadas:
        print("Você já digitou essa letra. Tente outra.")
        continue

    letras_adivinhadas.append(letra)

    if letra in palavra:
        lista = []
        for indice in range(len(palavra)):
            if letra == palavra[indice]:
                lista.append(letra)
            else:
                lista.append(palavra_secreta[indice])
        palavra_secreta = "".join(lista)
    else:
        max_tentativas -= 1
        print(f"Letra não encontrada, você tem {max_tentativas} tentativas restantes.")

    if palavra_secreta == palavra:
        print(f"Parabéns! Você ganhou! A palavra era '{palavra}'.")
        break

    if max_tentativas == 0:
        print(f"Você perdeu! A palavra era '{palavra}'.")
        break
