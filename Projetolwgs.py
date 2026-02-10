import termo_lib as jogo

tentativas = 6
vitoria = False

print("=" * 33)
print("\033[1;34m JOGO TERMO - ADIVINHE A PALAVRA\033[m")
print("=" * 33)

palavra_secreta = jogo.palavra_aleatoria()
palavra_limpa = jogo.remover_acentos(palavra_secreta)

print(f"Dica: a palavra tem {len(palavra_limpa)} letras.")

for i in range(1, tentativas + 1):

    print(f"\nTentativa {i}/{tentativas}: ", end="")

    tentativa = jogo.palpite(palavra_limpa)

    resultado = jogo.comparar(tentativa, palavra_secreta)
    print(resultado)

    if tentativa == palavra_limpa:
        vitoria = True
        break


if vitoria:
    print(f'\n\033[1;32mBoa! Tu acertaste a palavra','\tSEM BATOTA NÃO É?\033[m', f'\033[4m{palavra_secreta.upper()}\033[m')
else:
    print(f'\n\033[1;31mAcabaram as tentativas!', 'KKKKK, ITs OVER', f'A palavra era:\033[m', f'\033[4m{palavra_secreta.upper()}\033[m')