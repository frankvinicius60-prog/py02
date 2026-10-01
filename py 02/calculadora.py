"""Módulo com operações matemáticas básicas."""


def somar(a, b):
    """Retorna a soma de dois números."""
    return a + b


def subtrair(a, b):
    """Retorna a subtração de dois números."""
    return a - b


def multiplicar(a, b):
    """Retorna a multiplicação de dois números."""
    return a * b


def dividir(a, b):
    """Retorna a divisão de a por b, tratando divisão por zero."""
    if b == 0:
        print("Erro: divisão por zero não é permitida.")
        return None
    return a / b


if __name__ == "__main__":
    print(somar(10, 5))
    print(subtrair(10, 5))
    print(multiplicar(10, 5))
    print(dividir(10, 5))
    print(dividir(10, 0))
