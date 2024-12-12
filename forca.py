import random

def esc_palabras():
    with open("palavras.txt", "r", encoding="utf-8") as arquivo:
        palavras = arquivo.readlines()
        if palavras:
            return random.choice(palavras).strip()
        else:
            print("O arquivo palavras.txt está vazio.")
            return None

def forca():
    print("Olá, seja muito bem-vindo ao jogo da forca! Para jogar, é simples: daremos uma palavra para você, e você terá que adivinhá-la. Caso você erre a palavra dentro das 10 chances que lhe daremos, você será enforcado. Mas, se você acertar, poderá continuar vivo e em liberdade! Vamos lá. Boa sorte, você vai precisar.")

    while True:
        palavra = esc_palabras()
        if not palavra:
            return
        letras_cert = ["_"] * len(palavra)
        letras_er = []
        tentativas = 10

        while tentativas > 0:
            print("Palavra:", " ".join(letras_cert))
            print("Letras erradas:", " ".join(letras_er))
            print(f"Tentativas restantes: {tentativas}")

            tentativa = input("Qual letra? ")
            if len(tentativa) != 1 or not tentativa.isalpha():
                print("Digite apenas uma letra.")
                continue

            if tentativa in letras_cert or tentativa in letras_er:
                print("Você já tentou essa letra.")
                continue

            if tentativa in palavra:
                for i, letra in enumerate(palavra):
                    if letra == tentativa:
                        letras_cert[i] = tentativa
                if "_" not in letras_cert:
                    print("Parabéns! Você adivinhou a palavra e não será mais enforcado. A palavra era:", palavra)
                    break
            else:
                letras_er.append(tentativa)
                tentativas -= 1

                if tentativas == 0:
                    print("Você não conseguiu adivinhar a palavra. Sendo assim, você será condenado à forca! A palavra era:", palavra)

        dnv = input("Deseja jogar novamente? Digite 's' para sim ou 'n' para não: ")
        if dnv.lower() != "s":
            break
if __name__ == "__main__":
    forca()
