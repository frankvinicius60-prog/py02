# VERSÕES EQUIVALENTES EM PORTUGOL
# Todo o conteúdo abaixo está comentado propositalmente.

# ============================================================
# CALCULADORA
# ============================================================

# FUNCAO somar(a, b)
#     RETORNE a + b
# FIM_FUNCAO

# FUNCAO subtrair(a, b)
#     RETORNE a - b
# FIM_FUNCAO

# FUNCAO multiplicar(a, b)
#     RETORNE a * b
# FIM_FUNCAO

# FUNCAO dividir(a, b)
#     SE b = 0 ENTAO
#         ESCREVA "Erro: divisão por zero não é permitida."
#         RETORNE NULO
#     SENAO
#         RETORNE a / b
#     FIM_SE
# FIM_FUNCAO


# ============================================================
# CONVERSOR DE TEMPERATURA
# ============================================================

# FUNCAO converter_temperatura(celsius)
#     fahrenheit <- (celsius * 9 / 5) + 32
#     RETORNE fahrenheit
# FIM_FUNCAO


# ============================================================
# VALIDADOR DE SENHA
# ============================================================

# FUNCAO validar_senha(senha)
#     SE TAMANHO(senha) >= 8 ENTAO
#         RETORNE VERDADEIRO
#     SENAO
#         RETORNE FALSO
#     FIM_SE
# FIM_FUNCAO


# ============================================================
# CAIXA COM VÁRIOS PREÇOS
# ============================================================

# FUNCAO caixa(precos...)
#     total <- 0
#
#     PARA CADA preco EM precos FACA
#         total <- total + preco
#     FIM_PARA
#
#     RETORNE total
# FIM_FUNCAO


# ============================================================
# FICHA DO ALUNO
# ============================================================

# FUNCAO ficha_aluno(dados...)
#     RETORNE dados
# FIM_FUNCAO


# ============================================================
# LISTA SEGURA
# ============================================================

# FUNCAO adicionar_item_seguro(lista_original, item)
#     nova_lista <- COPIA(lista_original)
#     ADICIONE item EM nova_lista
#     RETORNE nova_lista
# FIM_FUNCAO


# ============================================================
# FATORIAL RECURSIVO
# ============================================================

# FUNCAO fatorial(numero)
#     SE numero < 0 ENTAO
#         ESCREVA "Número inválido"
#     SENAO SE numero = 0 OU numero = 1 ENTAO
#         RETORNE 1
#     SENAO
#         RETORNE numero * fatorial(numero - 1)
#     FIM_SE
# FIM_FUNCAO


# ============================================================
# RELATÓRIO
# ============================================================

# FUNCAO relatorio(titulo, linhas..., configuracoes...)
#     ESCREVA titulo
#
#     PARA CADA linha EM linhas FACA
#         ESCREVA linha
#     FIM_PARA
#
#     UTILIZE configuracoes PARA FORMATAR O RELATORIO
# FIM_FUNCAO
