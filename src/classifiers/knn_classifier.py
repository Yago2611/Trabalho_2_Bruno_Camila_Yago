
from typing import Dict, List
from .classifier_interface import ClassifierInterface
from src.datasets.dataset_interface import DatasetInterface


class KnnClassifier(ClassifierInterface):
    def __init__(self, config: Dict) -> None:
        super().__init__(config)
        self.dados_treino = []
        self.dados_teste = []
        self.distancias = []

    def train(self, train_dataset: DatasetInterface) -> None:
        for x in range(len(train_dataset.lista)):
           dado = train_dataset.get(x)
           self.dados_treino.append(dado)

    def predict(self, test_dataset: DatasetInterface) -> List[str]:
        """ para cada amostra no dataset, buscar os k vizinhos mais proximos e 
        retornar a classe mais frequente entre eles """
        for x in range(len(test_dataset.lista)):
            dado = test_dataset.get(x)
            self.dados_teste.append(dado)
        for teste in self.dados_teste:
            for treino in self.dados_treino:
                pass
        return []
