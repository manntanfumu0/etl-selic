from extract import extract_data
from transform import transform_data
from load import load_data
from logger import get_logger

logger = get_logger(__name__)

def run_pipeline():
    logger.info("Iniciando pipeline ETL - SELIC")

    df_raw = extract_data()
    logger.info("Extração concluída com sucesso")

    df_processed = transform_data(df_raw)
    logger.info("Transformação concluída")

    load_data(df_processed)
    logger.info("Pipeline finalizado com sucesso")

if __name__ == "__main__":
    run_pipeline()
