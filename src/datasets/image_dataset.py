
from typing import Tuple, Any, Dict
from .dataset_interface import DatasetInterface
import cv2

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
        path = path.split("/")
        path = f"{path[0]}/{path[1]}/{path[2]}"
        for x in range(len(self.lista)):
            k = self.lista[x][0].split('/')
            if k[1] == "train" or k[1] == "test":
                self.lista[x][0] = f"{path}/{k[1]}/{k[2]}"
            else: 
                self.lista[x][0] = f"{path}/{k[3]}/{k[4]}"

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
