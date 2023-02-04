
from typing import Union, Dict, List
from src.datasets.dataset_interface import DatasetInterface
from src.classifiers.classifier_interface import ClassifierInterface
from src.metrics import accuracy, confusion_matrix
import time


class Experiment:
    def __init__(self,
                 train_dataset: DatasetInterface,
                 test_dataset: DatasetInterface):
        self.train_dataset = train_dataset
        self.test_dataset = test_dataset
        self.true_classes = self._get_true_classes_from_dataset(
            self.test_dataset)

    def run(self, classifier: ClassifierInterface) -> Dict[str, Union[float, List]]:
        """ executa o experimento """
        tamanho = self.train_dataset.size()
        inicio = time.time()
        classifier.train(self.train_dataset)
        tempo_treino = self.get_time(inicio)/tamanho
        tamanho = self.test_dataset.size()
        inicio = time.time()
        pred_classes = classifier.predict(self.test_dataset)
        tempo_previsao = self.get_time(inicio)/tamanho
        metrics = {
            "training time per sample": f"{tempo_treino:.3f}s",
            "inference time per sample": f"{tempo_previsao:.3f}s",
            "accuracy": accuracy(self.true_classes, pred_classes),
            "confusion_matrix": confusion_matrix(self.true_classes, pred_classes)
        }
        return metrics

    def _get_true_classes_from_dataset(self, dataset: DatasetInterface) -> List[str]:
        true_classes = []
        for idx in range(dataset.size()):
            _, sample_class = dataset.get(idx)
            true_classes.append(sample_class)
        return true_classes
    
    def get_time(self,inicio: float):
        return time.time() - inicio

