from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.components.training import Training

class TrainingPipeline:
    def __init__(self):
        pass

    def initiate_training_pipeline(self):
        try:
            config = ConfigurationManager()
            training_config = config.get_training_config()
            training = Training(config=training_config)
            training.get_base_model()
            training.train_valid_generator()
            training.train()

        except Exception as e:
            raise e