from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.components.model_evaluation import Evaluation


class EvaluationPipeline:
    def __init__(self):
        pass

    def initiate_evaluation_pipeline(self):
        try:
            config = ConfigurationManager()
            eval_config = config.get_evaluation_config()
            eval = Evaluation(config=eval_config)
            eval.evaluation()
            eval.log_into_mlflow()
            

        except Exception as e:
            raise e
        
