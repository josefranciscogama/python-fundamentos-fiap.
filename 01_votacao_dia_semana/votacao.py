"""Votação do melhor dia da semana entre colaboradores, com tratamento de empates."""

DIAS = {
    "SEGUNDA-FEIRA": "Segunda-Feira",
    "TERCA-FEIRA": "Terça-Feira",
    "QUARTA-FEIRA": "Quarta-Feira",
    "QUINTA-FEIRA": "Quinta-Feira",
    "SEXTA-FEIRA": "Sexta-Feira",
}


def ler_numero_colaboradores():
    """Pede o número de colaboradores até receber um inteiro positivo."""
    while True:
        try:
            numero = int(input("Informe o número de colaboradores: "))
        except ValueError:
            print("Digite um número inteiro.")
            continue
        if numero > 0:
            return numero
        print("O número de colaboradores deve ser maior que zero.")


def ler_voto():
    """Pede o dia preferido até receber um dia válido (aceita com ou sem cedilha)."""
    while True:
        escolha = input(
            "Informe o dia da sua preferência "
            "(Segunda-Feira, Terça-Feira, Quarta-Feira, Quinta-Feira ou Sexta-Feira): "
        )
        chave = escolha.strip().upper().replace("Ç", "C")
        if chave in DIAS:
            return DIAS[chave]
        print("Dia inválido. Tente novamente.")


def apurar_votos(votos):
    """Retorna a lista de dias mais votados e a quantidade de votos de cada um."""
    maior = max(votos.values())
    vencedores = [dia for dia, quantidade in votos.items() if quantidade == maior]
    return vencedores, maior


def main():
    numero_colaboradores = ler_numero_colaboradores()
    votos = {dia: 0 for dia in DIAS.values()}

    for _ in range(numero_colaboradores):
        votos[ler_voto()] += 1

    vencedores, maior = apurar_votos(votos)

    if len(vencedores) > 1:
        print(f"Dias empatados: {', '.join(vencedores)}")
        print(f"Houve um empate: cada um recebeu {maior} votos.")
    else:
        print(f"O dia escolhido pelos colaboradores é: {vencedores[0]}")


if __name__ == "__main__":
    main()
