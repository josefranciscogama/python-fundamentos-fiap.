"""Simulador de parcelamento de dívida com juros crescentes por faixa de parcelas."""

TAXA_BASE = 5            # % aplicada a cada faixa
PARCELAS_POR_FAIXA = 3
MAXIMO_PARCELAS = 12


def ler_valor_positivo(mensagem):
    """Pede um valor numérico até receber um número maior que zero."""
    while True:
        try:
            valor = float(input(mensagem).replace(",", "."))
        except ValueError:
            print("Digite um número válido.")
            continue
        if valor > 0:
            return valor
        print("O valor deve ser maior que zero.")


def calcular_parcelamento(divida, parcelas):
    """Retorna (total, juros, valor_da_parcela) para o número de parcelas informado."""
    taxa = TAXA_BASE + (parcelas / PARCELAS_POR_FAIXA) * TAXA_BASE
    total = divida * (1 + taxa / 100)
    juros = total - divida
    return total, juros, total / parcelas


def exibir_linha(total, juros, parcelas, valor_parcela):
    print(
        f"Total: R$ {total:.2f} | Juros: R$ {juros:.2f} | "
        f"Parcelas: {parcelas} | Valor da parcela: R$ {valor_parcela:.2f}"
    )


def main():
    divida = ler_valor_positivo("Digite o valor da dívida: ")

    # Pagamento à vista (1 parcela, sem juros)
    exibir_linha(divida, 0.0, 1, divida)

    for parcelas in range(PARCELAS_POR_FAIXA, MAXIMO_PARCELAS + 1, PARCELAS_POR_FAIXA):
        total, juros, valor_parcela = calcular_parcelamento(divida, parcelas)
        exibir_linha(total, juros, parcelas, valor_parcela)


if __name__ == "__main__":
    main()
