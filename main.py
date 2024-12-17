from src.cnnClassifier.logging.logger import logging
from src.cnnClassifier.pipeline.data_ingestion_pipeline import DataIngestionPipeline

STAGE_NAME = "DATA INGESION"
try:
    logging.info(f"Initiating {STAGE_NAME} stage")
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logging.info(f"Completed {STAGE_NAME} stage")
except Exception as e:
    logging.exception(e)
    raise e

    











