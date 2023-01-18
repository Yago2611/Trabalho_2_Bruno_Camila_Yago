
from typing import List


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
