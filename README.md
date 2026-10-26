# Python: Fundamentos (FIAP)

Quatro programas de console em Python que simulam cenários do dia a dia (votação, financiamento, dívida e investimentos). Desenvolvidos durante o curso de Análise e Desenvolvimento de Sistemas na FIAP e refatorados depois, com foco em código limpo, validação de entrada e funções reutilizáveis.

## Programas

| Pasta | O que faz |
|---|---|
| `01_votacao_dia_semana` | Colaboradores votam no melhor dia da semana. O programa valida o voto, apura o resultado e trata empates. |
| `02_parcelamento_veiculo` | Calcula o preço à vista (20% de desconto) e o valor parcelado em 6x até 60x, com acréscimo de 3% a cada 6 parcelas. |
| `03_parcelas_divida` | Mostra o total, os juros e o valor da parcela de uma dívida em 1x, 3x, 6x, 9x e 12x. |
| `04_imposto_investimentos` | Calcula o imposto de renda no resgate de CDB (tabela regressiva por prazo) e informa a isenção de LCI e LCA. |

## Conceitos praticados

- Entrada e saída de dados (`input`, f-strings, formatação monetária)
- Estruturas condicionais (`if / elif / else`)
- Laços `for` e `while`, incluindo validação de entrada
- Funções e organização do código (`main`, `if __name__ == "__main__"`)
- Dicionários, listas e `max()` na apuração de resultados
- Constantes nomeadas no lugar de "números mágicos"

## Como executar

Requer Python 3.8 ou superior.

```bash
git clone <URL-DO-REPOSITORIO>
cd python-fundamentos-fiap
python 01_votacao_dia_semana/votacao.py
```

Troque o caminho para executar os demais programas.

## Possíveis evoluções

- Testes automatizados com `pytest` para as funções de cálculo
- No exercício de investimentos, aplicar a alíquota apenas sobre o rendimento (e não sobre o valor total resgatado), como ocorre na prática
- Interface web simples com JavaScript para os simuladores financeiros

## Autor

José Francisco Gama Magalhães de Freitas | 
