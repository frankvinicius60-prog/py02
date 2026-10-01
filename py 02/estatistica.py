"""Módulo opcional com funções estatísticas e desafios bônus."""

from statistics import mean as media, median as mediana, mode as moda

est = "estatistica"


def fatorial(numero):
    """Calcula o fatorial de um número inteiro não negativo usando recursão."""
    if numero < 0:
        raise ValueError("O número deve ser maior ou igual a zero.")
    if numero in (0, 1):
        return 1
    return numero * fatorial(numero - 1)


def relatorio(titulo, *linhas, **config):
    """Exibe um relatório com título, linhas e configurações adicionais."""
    separador = config.get("separador", "-")
    largura = config.get("largura", 40)

    print(separador * largura)
    print(titulo)
    print(separador * largura)

    for linha in linhas:
        print(linha)

    print(separador * largura)


if __name__ == "__main__":
    valores = [1, 2, 2, 3, 4]
    print("Média:", media(valores))
    print("Mediana:", mediana(valores))
    print("Moda:", moda(valores))
    print("Fatorial de 5:", fatorial(5))

    relatorio(
        "Relatório de exemplo",
        "Linha 1",
        "Linha 2",
        separador="=",
        largura=30,
    )
