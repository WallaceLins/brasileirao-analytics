import os
import psycopg2
from dotenv import load_dotenv


# ============================================================
# CONFIGURAÇÕES
# ============================================================

load_dotenv()

SEASON = 2026

# ------------------------------------------------------------
# MÉDIAS HISTÓRICAS DOS ÚLTIMOS 5 CAMPEONATOS
# ------------------------------------------------------------

MEDIA_CAMPEAO = 78.60
MEDIA_LIBERTADORES = 66.95
MEDIA_SUL_AMERICANA = 53.97

# Média histórica dos 16º colocados
# utilizada como referência para o risco de rebaixamento

MEDIA_REBAIXAMENTO = 43.80

# ------------------------------------------------------------
# CONFIGURAÇÕES DO CAMPEONATO
# ------------------------------------------------------------

TOTAL_JOGOS = 38
PONTOS_POR_JOGO = 3


# ============================================================
# CONECTAR AO POSTGRESQL
# ============================================================

def conectar_banco():

    conexao = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT", "5432"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

    return conexao


# ============================================================
# BUSCAR CLASSIFICAÇÃO
# ============================================================

def buscar_classificacao():

    conexao = conectar_banco()
    cursor = conexao.cursor()

    try:

        cursor.execute("""
            SELECT
                posicao,
                time,
                pontos,
                jogos
            FROM classificacao_atual
            ORDER BY posicao;
        """)

        dados = cursor.fetchall()

        return dados

    except Exception as erro:

        print()
        print("Erro ao buscar classificação:")
        print(erro)

        return []

    finally:

        cursor.close()
        conexao.close()


# ============================================================
# CALCULAR APROVEITAMENTO
# ============================================================

def calcular_aproveitamento(pontos, jogos):

    if jogos == 0:
        return 0

    pontos_disputados = jogos * PONTOS_POR_JOGO

    aproveitamento = pontos / pontos_disputados

    return aproveitamento


# ============================================================
# CALCULAR PROJEÇÃO DE PONTOS
# ============================================================

def calcular_projecao(pontos, jogos):

    aproveitamento = calcular_aproveitamento(
        pontos,
        jogos
    )

    projecao = (
        aproveitamento
        * TOTAL_JOGOS
        * PONTOS_POR_JOGO
    )

    return projecao


# ============================================================
# CALCULAR PONTOS NECESSÁRIOS
# ============================================================

def calcular_pontos_necessarios(pontos, media):

    if pontos >= media:

        return 0

    pontos_necessarios = media - pontos

    return round(pontos_necessarios)


# ============================================================
# CALCULAR PERCENTUAL NECESSÁRIO
# ============================================================

def calcular_percentual_necessario(
    pontos_necessarios,
    jogos_restantes
):

    if jogos_restantes <= 0:

        return 0

    pontos_restantes = (
        jogos_restantes
        * PONTOS_POR_JOGO
    )

    percentual = (
        pontos_necessarios
        / pontos_restantes
    ) * 100

    return percentual


# ============================================================
# DEFINIR OBJETIVO ATUAL
# ============================================================

def definir_objetivo(posicao):

    if posicao == 1:

        return "Campeão"

    elif 2 <= posicao <= 5:

        return "Libertadores"

    elif 6 <= posicao <= 11:

        return "Sul-Americana"

    elif 17 <= posicao <= 20:

        return "Rebaixamento"

    else:

        return "Sem competição CONMEBOL"


# ============================================================
# CALCULAR ÍNDICE DE RISCO DE REBAIXAMENTO
# ============================================================

def calcular_indice_risco(pontos):

    if pontos >= MEDIA_REBAIXAMENTO:

        return 0, "Sem risco pela referência histórica"

    elif pontos >= 40:

        return 25, "Baixo"

    elif pontos >= 35:

        return 50, "Moderado"

    elif pontos >= 30:

        return 75, "Alto"

    else:

        return 100, "Muito alto"


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

if __name__ == "__main__":

    print()
    print("=" * 70)
    print("ANÁLISE DE PROBABILIDADES - BRASILEIRÃO 2026")
    print("=" * 70)


    # ========================================================
    # BUSCAR CLASSIFICAÇÃO
    # ========================================================

    print()
    print("Buscando classificação no PostgreSQL...")

    classificacao = buscar_classificacao()

    print()
    print(
        f"Times encontrados: {len(classificacao)}"
    )

    if not classificacao:

        print()
        print("Nenhum time encontrado.")
        print(
            "Verifique a tabela classificacao_atual."
        )

        exit()


    # ========================================================
    # PROJEÇÃO DO CAMPEONATO
    # ========================================================

    print()
    print("=" * 70)
    print("PROJEÇÃO DO BRASILEIRÃO 2026")
    print("=" * 70)


    for posicao, time, pontos, jogos in classificacao:

        aproveitamento = calcular_aproveitamento(
            pontos,
            jogos
        )

        projecao = calcular_projecao(
            pontos,
            jogos
        )

        objetivo = definir_objetivo(
            posicao
        )

        print(
            f"{posicao:2}º | "
            f"{time:<25} | "
            f"Pontos: {pontos:2} | "
            f"Jogos: {jogos:2} | "
            f"Aproveitamento: "
            f"{aproveitamento * 100:6.2f}% | "
            f"Projeção: {projecao:6.2f} | "
            f"Objetivo: {objetivo}"
        )


    # ========================================================
    # PONTOS NECESSÁRIOS PARA CADA OBJETIVO
    # ========================================================

    print()
    print("=" * 70)
    print("PONTOS NECESSÁRIOS PARA CADA OBJETIVO")
    print("=" * 70)


    for posicao, time, pontos, jogos in classificacao:

        jogos_restantes = (
            TOTAL_JOGOS - jogos
        )

        print()
        print("-" * 70)

        print(
            f"{posicao:2}º | {time}"
        )

        print(
            f"Pontos atuais: {pontos}"
        )

        print(
            f"Jogos disputados: {jogos}"
        )

        print(
            f"Jogos restantes: {jogos_restantes}"
        )

        print()


        # ====================================================
        # CAMPEÃO
        # ====================================================

        pontos_campeao = (
            calcular_pontos_necessarios(
                pontos,
                MEDIA_CAMPEAO
            )
        )

        percentual_campeao = (
            calcular_percentual_necessario(
                pontos_campeao,
                jogos_restantes
            )
        )

        if pontos >= MEDIA_CAMPEAO:

            print(
                "🏆 Campeão: "
                "média histórica já alcançada"
            )

        elif pontos_campeao > (
            jogos_restantes * PONTOS_POR_JOGO
        ):

            print(
                "🏆 Campeão: "
                "não é mais possível alcançar "
                "a média histórica"
            )

        else:

            print(
                f"🏆 Campeão: precisa de "
                f"{pontos_campeao} pontos "
                f"({percentual_campeao:.2f}% "
                f"dos pontos restantes)"
            )


        # ====================================================
        # LIBERTADORES
        # ====================================================

        pontos_libertadores = (
            calcular_pontos_necessarios(
                pontos,
                MEDIA_LIBERTADORES
            )
        )

        percentual_libertadores = (
            calcular_percentual_necessario(
                pontos_libertadores,
                jogos_restantes
            )
        )

        if pontos >= MEDIA_LIBERTADORES:

            print(
                "🟢 Libertadores: "
                "média histórica já alcançada"
            )

        elif pontos_libertadores > (
            jogos_restantes * PONTOS_POR_JOGO
        ):

            print(
                "🟢 Libertadores: "
                "não é mais possível alcançar "
                "a média histórica"
            )

        else:

            print(
                f"🟢 Libertadores: precisa de "
                f"{pontos_libertadores} pontos "
                f"({percentual_libertadores:.2f}% "
                f"dos pontos restantes)"
            )


        # ====================================================
        # SUL-AMERICANA
        # ====================================================

        pontos_sulamericana = (
            calcular_pontos_necessarios(
                pontos,
                MEDIA_SUL_AMERICANA
            )
        )

        percentual_sulamericana = (
            calcular_percentual_necessario(
                pontos_sulamericana,
                jogos_restantes
            )
        )

        if pontos >= MEDIA_SUL_AMERICANA:

            print(
                "🔵 Sul-Americana: "
                "média histórica já alcançada"
            )

        elif pontos_sulamericana > (
            jogos_restantes * PONTOS_POR_JOGO
        ):

            print(
                "🔵 Sul-Americana: "
                "não é mais possível alcançar "
                "a média histórica"
            )

        else:

            print(
                f"🔵 Sul-Americana: precisa de "
                f"{pontos_sulamericana} pontos "
                f"({percentual_sulamericana:.2f}% "
                f"dos pontos restantes)"
            )


    # ========================================================
    # ANÁLISE DE RISCO DE REBAIXAMENTO
    # ========================================================

    print()
    print("=" * 70)
    print("ANÁLISE DE RISCO DE REBAIXAMENTO")
    print("=" * 70)

    print()
    print(
        "Referência: média histórica dos 16º colocados = "
        f"{MEDIA_REBAIXAMENTO:.2f} pontos"
    )

    print(
        "O índice abaixo é um indicador baseado "
        "na pontuação atual."
    )

    print(
        "Não representa uma probabilidade estatística real."
    )


    for posicao, time, pontos, jogos in classificacao:

        # ----------------------------------------------------
        # JOGOS RESTANTES
        # ----------------------------------------------------

        jogos_restantes = (
            TOTAL_JOGOS - jogos
        )

        # ----------------------------------------------------
        # MÁXIMO DE PONTOS QUE AINDA PODE CONQUISTAR
        # ----------------------------------------------------

        pontos_maximos_restantes = (
            jogos_restantes
            * PONTOS_POR_JOGO
        )

        # ----------------------------------------------------
        # PONTUAÇÃO MÁXIMA POSSÍVEL
        # ----------------------------------------------------

        pontuacao_maxima = (
            pontos
            + pontos_maximos_restantes
        )

        # ----------------------------------------------------
        # PONTOS NECESSÁRIOS PARA ALCANÇAR A MÉDIA
        # ----------------------------------------------------

        pontos_necessarios = (
            MEDIA_REBAIXAMENTO
            - pontos
        )

        # ----------------------------------------------------
        # ÍNDICE DE RISCO
        # ----------------------------------------------------

        indice_risco, nivel_risco = (
            calcular_indice_risco(pontos)
        )


        print()
        print("-" * 70)

        print(
            f"{posicao:2}º | {time}"
        )

        print(
            f"Pontos atuais: {pontos}"
        )

        print(
            f"Jogos restantes: {jogos_restantes}"
        )

        print(
            f"Máximo de pontos restantes: "
            f"{pontos_maximos_restantes}"
        )

        print(
            f"Pontuação máxima possível: "
            f"{pontuacao_maxima}"
        )

        print(
            f"Média histórica do 16º colocado: "
            f"{MEDIA_REBAIXAMENTO:.2f}"
        )


        # ====================================================
        # TIME MATEMATICAMENTE REBAIXADO
        # ====================================================

        if pontuacao_maxima < MEDIA_REBAIXAMENTO:

            print()
            print(
                "🔴 TIME REBAIXADO"
            )

            print(
                "Não é mais possível alcançar "
                "a média histórica do 16º colocado."
            )


        # ====================================================
        # TIME JÁ ACIMA DA MÉDIA
        # ====================================================

        elif pontos >= MEDIA_REBAIXAMENTO:

            print()
            print(
                "🟢 Não há risco de rebaixamento, "
                "ultrapassou a média histórica."
            )

            print(
                f"Índice de risco: "
                f"{indice_risco}%"
            )

            print(
                f"Classificação: "
                f"{nivel_risco}"
            )


        # ====================================================
        # TIME AINDA PODE ALCANÇAR A MÉDIA
        # ====================================================

        else:

            print()
            print(
                "🔴 Risco de rebaixamento"
            )

            print(
                f"Precisa conquistar aproximadamente "
                f"{pontos_necessarios:.0f} pontos "
                f"para alcançar a média histórica."
            )

            print(
                f"Índice de risco: "
                f"{indice_risco}%"
            )

            print(
                f"Classificação: "
                f"{nivel_risco}"
            )


    # ========================================================
    # FINAL
    # ========================================================

    print()
    print("=" * 70)
    print("ANÁLISE FINALIZADA")
    print("=" * 70)