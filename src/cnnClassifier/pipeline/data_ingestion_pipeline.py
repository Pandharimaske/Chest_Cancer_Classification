from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.components.data_ingestion import DataIngestion


class DataIngestionPipeline:
    def __init__(self):
        pass

    def initiate_data_ingestion(self):

        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()

        except Exception as e:
            raise e
