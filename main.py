# Define a palavra que o jogador precisa adivinhar.
palavra = "python"

# Cria uma sequência de "_" com o mesmo tamanho da palavra,
# representando as letras que ainda não foram descobertas.
palavra_secreta = "_" * len(palavra)

# Cria uma lista vazia para armazenar as letras já digitadas.
letras_adivinhadas = []

# Define a quantidade inicial de tentativas disponíveis.
max_tentativas = 5

# Mantém o jogo em execução até que o jogador ganhe ou perca.
while True:
    # Exibe o progresso atual da palavra.
    print(palavra_secreta)

    # Solicita uma letra ao jogador e converte a entrada para minúsculas.
    letra = input("Digite uma letra: ").lower()

    # Verifica se a letra já foi digitada anteriormente.
    if letra in letras_adivinhadas:
        # Informa que a letra já foi utilizada.
        print("Você já digitou essa letra. Tente outra.")

        # Retorna ao início do laço sem gastar uma tentativa.
        continue

    # Adiciona a nova letra à lista de letras digitadas.
    letras_adivinhadas.append(letra)

    # Verifica se a letra digitada pertence à palavra original.
    if letra in palavra:
        # Cria uma lista temporária para reconstruir a palavra
        # revelando as letras corretas e mantendo os "_" restantes.
        lista = []

        # Percorre todas as posições da palavra original.
        for indice in range(len(palavra)):
            # Verifica se a letra atual corresponde à letra digitada.
            if letra == palavra[indice]:
                # Adiciona a letra correta à posição correspondente.
                lista.append(letra)
            else:
                # Mantém o caractere que já estava naquela posição,
                # preservando letras descobertas e espaços ocultos.
                lista.append(palavra_secreta[indice])

        # Junta os caracteres da lista em uma única string,
        # atualizando a representação da palavra secreta.
        palavra_secreta = "".join(lista)

    else:
        # Se a letra não existir na palavra, reduz uma tentativa.
        max_tentativas -= 1

        # Informa ao jogador quantas tentativas ainda restam.
        print(
            f"Letra não encontrada, você tem "
            f"{max_tentativas} tentativas restantes."
        )

    # Verifica se todas as letras da palavra foram descobertas.
    if palavra_secreta == palavra:
        # Exibe a mensagem de vitória e revela a palavra.
        print(f"Parabéns! Você ganhou! A palavra era '{palavra}'.")

        # Encerra o laço porque o jogador venceu.
        break

    # Verifica se todas as tentativas foram utilizadas.
    if max_tentativas == 0:
        # Exibe a mensagem de derrota e revela a palavra.
        print(f"Você perdeu! A palavra era '{palavra}'.")

        # Encerra o laço porque o jogador perdeu.
        break
```
