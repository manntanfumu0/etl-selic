from logger import get_logger

logger = get_logger(__name__)

def load_data(df, path="data/processed/selic_processed.csv"):
    df.to_csv(path, index=False)
    logger.info(f"Dados salvos em: {path}")
