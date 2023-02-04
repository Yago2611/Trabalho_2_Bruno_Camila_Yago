import sys
import json
import cv2
from time import time
from abc import ABC, abstractmethod
from typing import Tuple,Any,Dict,List,Union

class DatasetInterface(ABC):
    def __init__(self, path: str) -> None:
        """ inicializa o dataset considerando os dados de configuracao """

    @abstractmethod
    def size(self) -> int:
        """ retorna o numero de elementos no dataset """

    @abstractmethod
    def get(self, i: int) -> Tuple[Any, str]:
        """ le o i-esimo dado (imagem ou noticia) do HD e retorna com a respectiva classe """

class ImageDataset(DatasetInterface):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        # ler arquivo contendo os nomes das imagens e as classes e armazenar
        # em uma lista
        self.lista = []
        arquivo = open(path,"r")
        linhas = arquivo.readlines()
        for linha in linhas:
            objeto = linha.split()
            self.lista.append(objeto)
        arquivo.close()

    def size(self) -> int:
        # retornar tamanho do dataset (numero de linhas do arquivo)
        return len(self.lista)

    def get(self, idx: int) -> Tuple[Any, str]:
        # ler a i-esima imagem do disco usando a biblioteca cv2 e retornar
        # a imagem e a respectiva classe
        img = cv2.imread(self.lista[idx][0],0) 
        img = img.tolist()
        image = []
        for y in img:
            for x in y:
                image.append(x)
        return (image,self.lista[idx][1])

class NewsDataset(DatasetInterface):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        # ler arquivo contendo os nomes dos arquivos de noticias e as classes

    def size(self) -> int:
        # retornar o numero de noticias no dataset (numero de linhas no arquivo)
        return 0

    def get(self, idx: int) -> Tuple[Any, str]:
        # ler a i-esima noticia do disco e retornar o texto como uma string e
        # a classe
        return 0, ""

class ClassifierInterface(ABC):
    def __init__(self, config: Dict) -> None:
        """ inicializa a classe considerando os dados de configuracao """

    @abstractmethod
    def train(self, train_dataset: DatasetInterface) -> None:
        """ usa os dados do dataset para treinar o classificador """

    @abstractmethod
    def predict(self, test_dataset: DatasetInterface) -> List[str]:
        """ prediz as classes de todos os elementos da base de dados """

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
    
class NearestCentroidClassifier(ClassifierInterface):
    def __init__(self, config: Dict) -> None:
        super().__init__(config)

    def train(self, train_dataset: DatasetInterface) -> None:
        """ calcular os centroides por classe """

    def predict(self, test_dataset: DatasetInterface) -> List[str]:
        """ para cada amostra no dataset, buscar o centroide mais proximo e respectiva retornar a classe """
        return []

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
        inicio = time.time()
        classifier.train(self.train_dataset)
        pred_classes = classifier.predict(self.test_dataset)

        metrics = {
            "time": self.get_time(inicio),
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

def load_config(path: str) -> Dict:
    """ le o arquivo json e retorna como um dicionario """
    arquivo = open(path,"r")
    x = arquivo.read()
    dict = json.loads(x)
    arquivo.close()
    return dict

def create_dataset(path: str, type: str) -> DatasetInterface:
    if type == 'image':
        return ImageDataset(path)
    elif type == 'news':
        return NewsDataset(path)
    else:
        raise Exception("Dataset type not found.")

def create_classifier(type: str, config: Dict) -> ClassifierInterface:
    if type == 'knn':
        return KnnClassifier(config)
    elif type == 'nc':
        return NearestCentroidClassifier(config)
    else:
        raise Exception("classifier type not found.")

def accuracy(true_classes: List[str], predicted_classes: List) -> float:
    """  calcula o percentual de acerto """
    acertos = 0
    for x in range(len(true_classes)):
        if predicted_classes[x] == true_classes[x]:
            acertos+=1
    return acertos/100


def confusion_matrix(true_classes: List[str], predicted_classes: List) -> List[List[int]]:
    """  retorna a matriz de confusao 
    veja explicacao em [1] ou [2], mas note que no trabalho nao eh permitido
    usar bibliotecas para calcular a matriz de confusao.

    [1] https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html
    [2] https://en.wikipedia.org/wiki/Confusion_matrix
    """
    return [[]]

args = sys.argv
config = load_config(args[1])

train_config = config['train_dataset']
test_config = config['test_dataset']
classifier_config = config['classifier']

train_dataset = create_dataset(train_config["path"], train_config["type"])
test_dataset = create_dataset(test_config["path"], test_config["type"])
classifier = create_classifier(classifier_config["type"], config)

experiment = Experiment(train_dataset, test_dataset)
metrics = experiment.run(classifier)
