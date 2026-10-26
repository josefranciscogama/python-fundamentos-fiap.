"""Simulador de compra de veículo: desconto à vista e parcelamento em até 60x."""

DESCONTO_A_VISTA = 0.20
ACRESCIMO_POR_FAIXA = 0.03   # 3% a cada faixa de 6 parcelas
PARCELAS_POR_FAIXA = 6
MAXIMO_PARCELAS = 60


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


def preco_a_vista(valor_veiculo):
    return valor_veiculo * (1 - DESCONTO_A_VISTA)


def preco_parcelado(valor_veiculo, parcelas):
    faixas = parcelas // PARCELAS_POR_FAIXA
    return valor_veiculo * (1 + ACRESCIMO_POR_FAIXA * faixas)


def main():
    valor_veiculo = ler_valor_positivo("Digite o preço do carro: ")

    print(f"Preço à vista com desconto de 20%: R$ {preco_a_vista(valor_veiculo):.2f}")

    for parcelas in range(PARCELAS_POR_FAIXA, MAXIMO_PARCELAS + 1, PARCELAS_POR_FAIXA):
        total = preco_parcelado(valor_veiculo, parcelas)
        valor_parcela = total / parcelas
        print(f"{parcelas:>2}x: total R$ {total:.2f} | parcela R$ {valor_parcela:.2f}")


if __name__ == "__main__":
    main()
