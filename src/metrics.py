
from typing import List


def accuracy(true_classes: List[str], predicted_classes: List) -> float:
    """  calcula o percentual de acerto """
    acertos = 0
    for x in range(len(true_classes)):
        if predicted_classes[x] == true_classes[x]:
            acertos+=1
    return f"{acertos/len(true_classes):.2f}"


def confusion_matrix(true_classes: List[str], predicted_classes: List) -> List[List[int]]:
    """  retorna a matriz de confusao """
    dif_classes = []
    for x in true_classes:
        if len(dif_classes) == 0 or not x in dif_classes:
            dif_classes.append(x)
    matriz = []
    for x in dif_classes:
        vetor = []
        for y in dif_classes:
            valor = 0
            for n in range(len(true_classes)):
                if true_classes[n] == x and predicted_classes[n] == y:
                    valor +=1
            vetor.append(valor)
        matriz.append(vetor)
    matriz_confusao = ""
    for x in matriz:
            matriz_confusao += f"\n{x}"
    return f"{dif_classes} --> {matriz_confusao}"
