import os
import requests
from dotenv import load_dotenv


# ============================================================
# CONFIGURAÇÕES
# ============================================================

load_dotenv()

API_KEY = os.getenv("HIGHLIGHTLY_KEY")

BASE_URL = "https://soccer.highlightly.net"

LEAGUE_ID = 61205
SEASON = 2026


# ============================================================
# HEADERS
# ============================================================

headers = {
    "x-rapidapi-key": API_KEY,
    "x-rapidapi-host": "football-highlights-api.p.rapidapi.com"
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

    response = requests.get(
        url,
        headers=headers,
        params=params,
        timeout=30
    )

    if response.status_code != 200:

        raise Exception(
            f"Erro na API Highlightly: "
            f"{response.status_code} - "
            f"{response.text}"
        )

    dados = response.json()

    return dados