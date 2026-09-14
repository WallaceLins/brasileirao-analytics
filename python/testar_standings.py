import os
import requests
from dotenv import load_dotenv, find_dotenv


# ============================================================
# CARREGAR ARQUIVO .ENV
# ============================================================

arquivo_env = find_dotenv()

print("Arquivo .env encontrado:")
print(arquivo_env)

load_dotenv(arquivo_env)


# ============================================================
# CONFIGURAÇÕES
# ============================================================

API_KEY = os.getenv("HIGHLIGHTLY_KEY")

BASE_URL = "https://soccer.highlightly.net"

LEAGUE_ID = 61205
SEASON = 2026


# ============================================================
# VERIFICAR API KEY
# ============================================================

print()
print("API Key encontrada:", bool(API_KEY))

if API_KEY:
    print("Tamanho da chave:", len(API_KEY))
else:
    print("ERRO: API Key não encontrada.")


# ============================================================
# TESTAR ENDPOINT /STANDINGS
# ============================================================

url = f"{BASE_URL}/standings"

params = {
    "leagueId": LEAGUE_ID,
    "season": SEASON
}

headers = {
    "x-rapidapi-key": API_KEY
}


print()
print("==========================================")
print("Testando endpoint /standings...")
print("==========================================")

print("Liga:", LEAGUE_ID)
print("Temporada:", SEASON)


# ============================================================
# FAZER REQUISIÇÃO
# ============================================================

response = requests.get(
    url,
    headers=headers,
    params=params
)


# ============================================================
# MOSTRAR RESULTADO
# ============================================================

print()
print("Status:", response.status_code)

print()
print("Resposta da API:")

print(response.text)