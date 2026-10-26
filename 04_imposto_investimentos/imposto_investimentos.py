"""Cálculo de imposto de renda sobre resgate de investimentos (CDB, LCI e LCA)."""

CDB, LCI, LCA = 1, 2, 3


def ler_inteiro(mensagem, minimo, maximo=None):
    """Pede um inteiro dentro do intervalo informado."""
    while True:
        try:
            numero = int(input(mensagem))
        except ValueError:
            print("Digite um número inteiro.")
            continue
        if numero >= minimo and (maximo is None or numero <= maximo):
            return numero
        print("Valor fora do intervalo permitido.")


def ler_valor_positivo(mensagem):
    while True:
        try:
            valor = float(input(mensagem).replace(",", "."))
        except ValueError:
            print("Digite um número válido.")
            continue
        if valor > 0:
            return valor
        print("O valor deve ser maior que zero.")


def aliquota_cdb(dias):
    """Tabela regressiva do imposto de renda conforme o tempo de aplicação."""
    if dias <= 180:
        return 0.225
    if dias <= 360:
        return 0.20
    if dias <= 720:
        return 0.175
    return 0.15


def main():
    print("Escolha o tipo de investimento:")
    print("1. CDB\n2. LCI\n3. LCA")

    tipo = ler_inteiro("Digite o tipo de investimento (1, 2 ou 3): ", 1, 3)
    valor_resgatado = ler_valor_positivo("Digite o valor resgatado: ")
    dias = ler_inteiro("Digite o número de dias que o valor permaneceu investido: ", 0)

    if tipo == CDB:
        imposto = valor_resgatado * aliquota_cdb(dias)
        print(f"O imposto de renda a ser pago é: R$ {imposto:.2f}")
    else:  # LCI e LCA
        print("O investimento é isento de imposto de renda.")


if __name__ == "__main__":
    main()
