from sklearn.metrics import mean_absolute_error,mean_squared_error
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import pickle
from src.utils.utils import load_object
from src.logger.logging import logging
from src.exception.exception import CustomException

import os
import sys

from dataclasses import dataclass
from pathlib import Path


@dataclass
class ModelEvaluationConfig:
    pass


class ModelEvaluation:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        try:
            pass
        except Exception as e:
            logging.info()
            raise CustomException(e,sys)