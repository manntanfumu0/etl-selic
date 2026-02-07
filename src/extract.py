import requests
import pandas as pd
import json
from logger import get_logger

logger = get_logger(__name__)

URL = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json&dataInicial=07/02/2016&dataFinal=07/02/2026"
RAW_PATH = "data/raw/selic_raw.json"

def extract_data() -> pd.DataFrame:
    response = requests.get(URL)

    if response.status_code != 200:
        logger.error(f"Erro ao acessar API do BCB. Status: {response.status_code}")
        raise Exception("Falha na extração dos dados")

    data = response.json()

    with open(RAW_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    logger.info(f"Dados RAW salvos em: {RAW_PATH}")

    return pd.DataFrame(data)
