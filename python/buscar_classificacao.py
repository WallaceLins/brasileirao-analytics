import os
import requests
import psycopg2
from dotenv import load_dotenv


# ============================================================
# CONFIGURAÇÕES
# ============================================================

load_dotenv()

API_KEY = os.getenv("HIGHLIGHTLY_KEY")

print("API Key carregada:", bool(API_KEY))
print("Tamanho da API Key:", len(API_KEY) if API_KEY else 0)

BASE_URL = "https://soccer.highlightly.net"

LEAGUE_ID = 61205

SEASON = 2026


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
# VERIFICAR API KEY
# ============================================================

if not API_KEY:

    print("ERRO: API Key não encontrada.")
    print("Verifique o arquivo .env.")

    exit()

print("API Key carregada com sucesso.")


# ============================================================
# HEADERS
# ============================================================

headers = {
    "x-rapidapi-key": API_KEY
}


# ============================================================
# BUSCAR CLASSIFICAÇÃO
# ============================================================

def buscar_classificacao():

    url = f"{BASE_URL}/standings"

    params = {
        "leagueId": LEAGUE_ID,
        "season": SEASON
    }

    print()
    print("Buscando classificação...")
    print(f"Liga: {LEAGUE_ID}")
    print(f"Temporada: {SEASON}")

    response = requests.get(
        url,
        headers=headers,
        params=params
    )

    print()
    print("Status:", response.status_code)

    if response.status_code != 200:

        print("Erro ao consultar a API.")
        print(response.text)

        return None

    dados = response.json()

    return dados


# ============================================================
# EXTRAIR TIMES DA CLASSIFICAÇÃO
# ============================================================

def extrair_classificacao(dados):

    classificacao = []

    grupos = dados.get("groups", [])

    if not grupos:

        print(
            "Nenhum grupo encontrado na resposta da API."
        )

        return classificacao

    standings = grupos[0].get(
        "standings",
        []
    )

    for item in standings:

        time = item.get(
            "team",
            {}
        )

        total = item.get(
            "total",
            {}
        )

        registro = {

            "posicao": item.get(
                "position"
            ),

            "time": time.get(
                "name"
            ),

            "pontos": item.get(
                "points"
            ),

            "jogos": total.get(
                "games"
            ),

            "vitorias": total.get(
                "wins"
            ),

            "empates": total.get(
                "draws"
            ),

            "derrotas": total.get(
                "loses"
            ),

            "gols_pro": total.get(
                "scoredGoals"
            ),

            "gols_contra": total.get(
                "receivedGoals"
            )
        }

        classificacao.append(
            registro
        )

    return classificacao


# ============================================================
# SALVAR CLASSIFICAÇÃO NO POSTGRESQL
# ============================================================

def salvar_classificacao(classificacao):

    if not classificacao:

        print()
        print(
            "Nenhuma classificação para salvar."
        )

        return

    conexao = conectar_banco()

    cursor = conexao.cursor()

    try:

        # ----------------------------------------------------
        # APAGAR CLASSIFICAÇÃO ANTERIOR
        # ----------------------------------------------------

        cursor.execute(
            "DELETE FROM classificacao_atual"
        )

        print()
        print(
            "Classificação anterior removida."
        )

        # ----------------------------------------------------
        # SQL DE INSERÇÃO
        # ----------------------------------------------------

        sql = """
            INSERT INTO classificacao_atual (
                temporada,
                posicao,
                time,
                pontos,
                jogos,
                vitorias,
                empates,
                derrotas,
                gols_pro,
                gols_contra
            )
            VALUES (
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s
            )
        """

        # ----------------------------------------------------
        # INSERIR CADA TIME
        # ----------------------------------------------------

        for time in classificacao:

            cursor.execute(
                sql,
                (
                    SEASON,
                    time["posicao"],
                    time["time"],
                    time["pontos"],
                    time["jogos"],
                    time["vitorias"],
                    time["empates"],
                    time["derrotas"],
                    time["gols_pro"],
                    time["gols_contra"]
                )
            )

        # ----------------------------------------------------
        # CONFIRMAR ALTERAÇÕES
        # ----------------------------------------------------

        conexao.commit()

        print()
        print(
            "Classificação salva no PostgreSQL!"
        )

        print(
            f"Total de times salvos: "
            f"{len(classificacao)}"
        )

    except Exception as erro:

        # ----------------------------------------------------
        # DESFAZER ALTERAÇÕES EM CASO DE ERRO
        # ----------------------------------------------------

        conexao.rollback()

        print()
        print(
            "Erro ao salvar classificação:"
        )

        print(erro)

    finally:

        # ----------------------------------------------------
        # FECHAR CURSOR E CONEXÃO
        # ----------------------------------------------------

        cursor.close()

        conexao.close()

        print()
        print(
            "Conexão com PostgreSQL encerrada."
        )


# ============================================================
# MOSTRAR CLASSIFICAÇÃO
# ============================================================

def mostrar_classificacao(classificacao):

    print()
    print("==========================================")
    print("CLASSIFICAÇÃO BRASILEIRÃO 2026")
    print("==========================================")

    for time in classificacao:

        print(
            f"{time['posicao']:2}º | "
            f"{time['time']:<25} | "
            f"Pontos: {time['pontos']:2} | "
            f"Jogos: {time['jogos']:2} | "
            f"V: {time['vitorias']:2} | "
            f"E: {time['empates']:2} | "
            f"D: {time['derrotas']:2} | "
            f"GP: {time['gols_pro']:2} | "
            f"GC: {time['gols_contra']:2}"
        )


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

if __name__ == "__main__":

    dados = buscar_classificacao()

    if dados:

        print()
        print(
            "Classificação recebida com sucesso!"
        )

        classificacao = extrair_classificacao(
            dados
        )

        print(
            f"Times encontrados: "
            f"{len(classificacao)}"
        )

        if classificacao:

            mostrar_classificacao(
                classificacao
            )

            salvar_classificacao(
                classificacao
            )

        else:

            print(
                "Nenhum time foi encontrado."
            )