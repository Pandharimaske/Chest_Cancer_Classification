from src.cnnClassifier.logging.logger import logging
from src.cnnClassifier.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.cnnClassifier.pipeline.prepare_base_model_pipeline import PrepareBaseModelPipeline
from src.cnnClassifier.pipeline.training_pipeline import TrainingPipeline


STAGE_NAME = "DATA INGESION"
try:
    logging.info(f"Initiating {STAGE_NAME} stage")
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logging.info(f"Completed {STAGE_NAME} stage")
    
except Exception as e:
    logging.exception(e)
    raise e

    
STAGE_NAME = "PREPARE BASE MODEL"
try:
    logging.info(f"Initiating {STAGE_NAME} stage")
    prepare_base_model_pipeline = PrepareBaseModelPipeline()
    prepare_base_model_pipeline.initiate_prepare_base_model()
    logging.info(f"Completed {STAGE_NAME} stage")

except Exception as e:
    logging.exception(e)
    raise e


STAGE_NAME = "TRAINIG MODEL"
try:
    logging.info(f"Initiating {STAGE_NAME} stage")
    training_pipeline = TrainingPipeline()
    training_pipeline.initiate_training_pipeline()
    logging.info(f"Completed {STAGE_NAME} stage")

except Exception as e:
    logging.exception(e)
    raise e


from src.cnnClassifier.pipeline.evaluation_pipeline import EvaluationPipeline

STAGE_NAME = "MODEL EVALUATION"
try:
    logging.info(f"Initiating {STAGE_NAME} stage")
    evaluation_pipeline = EvaluationPipeline()
    evaluation_pipeline.initiate_evaluation_pipeline()
    logging.info(f"Completed {STAGE_NAME} stage")

except Exception as e:
    logging.exception(e)
    raise e












