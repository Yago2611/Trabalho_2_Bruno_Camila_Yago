
from typing import Dict
from .classifier_interface import ClassifierInterface
from .knn_classifier import KnnClassifier
from .nc_classifier import NearestCentroidClassifier


def create_classifier(type: str, config: Dict) -> ClassifierInterface:
    if type == 'knn':
        return KnnClassifier(config)
    elif type == 'nc':
        return NearestCentroidClassifier(config)
    else:
        raise Exception("classifier type not found.")
