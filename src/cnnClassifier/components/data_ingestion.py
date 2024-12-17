import os , sys
import zipfile
import gdown
from src.cnnClassifier.logging.logger import logging
from src.cnnClassifier.utils.common import get_size
from src.cnnClassifier.config.configuration import DataIngestionConfig


class DataIngestion:
    def __init__(self , config: DataIngestionConfig):
        self.config = config
        print(self.config.root_dir)

    def download_file(self) -> str:

        try:
            dataset_url = self.config.source_URL
            zip_download_dir = self.config.local_data_file

            os.makedirs(self.config.root_dir , exist_ok=True)
            logging.info(f"Downloading data from {dataset_url} into file {zip_download_dir}")

            file_id = dataset_url.split("/")[-2]
            prefix =  'https://drive.google.com/uc?/export=download&id='
            gdown.download(prefix + file_id , zip_download_dir)

            logging.info(f"Downloaded data from {dataset_url} into file {zip_download_dir}")
        except Exception as e:
            raise e
        
    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path , exist_ok=True)

        with zipfile.ZipFile(self.config.local_data_file , 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
            