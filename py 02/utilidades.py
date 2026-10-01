"""Módulo com funções utilitárias da prática independente."""


def converter_temperatura(celsius):
    """Converte uma temperatura de Celsius para Fahrenheit."""
    return (celsius * 9 / 5) + 32


def validar_senha(senha):
    """Retorna True se a senha tiver pelo menos 8 caracteres."""
    return len(senha) >= 8


def caixa(*precos):
    """Soma uma quantidade variável de preços."""
    return sum(precos)


def ficha_aluno(**dados):
    """Retorna os dados informados de um aluno."""
    return dados


def adicionar_item_seguro(lista_original, item):
    """Adiciona um item a uma cópia da lista sem alterar a original."""
    nova_lista = lista_original.copy()
    nova_lista.append(item)
    return nova_lista


if __name__ == "__main__":
    print(converter_temperatura(25))
    print(validar_senha("python123"))
    print(caixa(10.0, 20.0, 30.0))
    print(ficha_aluno(nome="Ana", idade=20, curso="Python"))

    lista = ["Python", "HTML"]
    print(adicionar_item_seguro(lista, "CSS"))
    print(lista)
