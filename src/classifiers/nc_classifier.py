
from typing import Dict, List
from .classifier_interface import ClassifierInterface
from src.datasets.dataset_interface import DatasetInterface


class NearestCentroidClassifier(ClassifierInterface):
    def __init__(self, config: Dict) -> None:
        super().__init__(config)
        self.train_dataset = 0
        self.centroides = []
        self.dados_treino = []
        self.dados_teste = []

    def train(self, train_dataset: DatasetInterface) -> None:
        """ calcular os centroides por classe """
        self.train_dataset = train_dataset
        for x in range(len(train_dataset.lista)):
           dado = train_dataset.get(x)
           self.dados_treino.append(dado)
        dif_classes = []
        for x in self.dados_treino:
            if len(dif_classes) == 0 or not x[1] in dif_classes:
                 dif_classes.append(x[1])
        for x in dif_classes:
            soma = 0
            contador = 0
            for y in self.dados_treino:
                if y[1] == x:
                    contador +=1
                    if soma ==0:
                        soma = y[0]
                    else:
                        for i in range(len(soma)):
                            soma[i] += y[0][i]
            for i in range(len(soma)):
                soma[i] /= contador
            self.centroides.append((soma,x))

    def predict(self, test_dataset: DatasetInterface) -> List[str]:
        """ para cada amostra no dataset, buscar o centroide mais proximo e respectiva retornar a classe """
        previsoes = []
        if (test_dataset.palavras != "NULL"):
            test_dataset.palavras = self.train_dataset.palavras
        for x in range(len(test_dataset.lista)):
            dado = test_dataset.get(x)
            self.dados_teste.append(dado)
        for teste in self.dados_teste:
            distancias = []
            dic = {}
            previsao = 0 
            for treino in self.centroides:
                d = 0
                for i in range(len(teste[0])):
                    d += (float(treino[0][i])-float(teste[0][i]))**2
                d **= 0.5 
                if len(distancias) == 0:
                    distancias.append((d,treino[1]))
                elif len(distancias) == 1:
                    for i in range(len(distancias)):
                        if d < distancias[i][0]:
                            distancias[i] = (d,treino[1])
                            break
            for i in distancias:
                cont = 0
                if len(dic) == 0:
                    dic = {i[1]:1}
                else:
                    for x in dic:
                        if x == i[1]:
                            dic[x]+=1
                        else:
                            cont+=1
                if cont == len(dic):
                    dic[i[1]]=1
                cont = 0 
            for x in dic:
                if previsao == 0:
                    previsao = (x,dic[x]) 
                else:
                    if dic[x]>previsao[1]:
                        previsao = (x,dic[x])
            previsoes.append(previsao)
        for x in range(len(previsoes)):
         previsoes[x] = previsoes[x][0]
        return previsoes