
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
        previsoes = []
        for x in range(len(test_dataset.lista)):
            dado = test_dataset.get(x)
            self.dados_teste.append(dado)
        for teste in self.dados_teste:
            distancias = []
            for treino in self.dados_treino:
                d = 0
                for i in range(len(teste[0])):
                    d += (float(treino[0][i])-float(teste[0][i]))**2
                d **= 0.5 
                if len(distancias) < 5:
                    distancias.append((d,treino[1]))
                elif len(distancias) == 5:
                    for i in range(len(distancias)):
                        if d < distancias[i][0]:
                            distancias[i] = (d,treino[1])
        for i in distancias:
            pass
        return []
