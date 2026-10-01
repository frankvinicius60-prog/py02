"""Script principal do projeto."""

import calculadora
import utilidades
from estatistica import fatorial, media, mediana, moda, relatorio


def main():
    """Executa chamadas das funções dos módulos do projeto."""
    print("=== CALCULADORA ===")
    print("Soma:", calculadora.somar(10, 5))
    print("Subtração:", calculadora.subtrair(10, 5))
    print("Multiplicação:", calculadora.multiplicar(10, 5))
    print("Divisão:", calculadora.dividir(10, 5))
    print("Divisão por zero:", calculadora.dividir(10, 0))

    print("\n=== UTILIDADES ===")
    print("25°C em Fahrenheit:", utilidades.converter_temperatura(25))
    print("Senha válida:", utilidades.validar_senha("python123"))
    print("Total do caixa:", utilidades.caixa(10.50, 20.00, 7.25))

    aluno = utilidades.ficha_aluno(
        nome="Fernando",
        idade=20,
        curso="Python",
    )
    print("Ficha do aluno:", aluno)

    lista_original = ["Python", "HTML"]
    nova_lista = utilidades.adicionar_item_seguro(lista_original, "CSS")
    print("Lista original:", lista_original)
    print("Nova lista:", nova_lista)

    print("\n=== BÔNUS ===")
    valores = [1, 2, 2, 3, 4]
    print("Média:", media(valores))
    print("Mediana:", mediana(valores))
    print("Moda:", moda(valores))
    print("Fatorial de 5:", fatorial(5))

    relatorio(
        "Resumo do projeto",
        "Módulos carregados com sucesso.",
        "Funções executadas sem erros.",
        separador="=",
        largura=45,
    )


if __name__ == "__main__":
    main()
