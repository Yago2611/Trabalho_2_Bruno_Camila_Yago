
from typing import Tuple, Any, Dict
from .dataset_interface import DatasetInterface


class NewsDataset(DatasetInterface):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        # ler arquivo contendo os nomes dos arquivos de noticias e as classes
        self.lista = []
        arquivo = open(path,"r")
        linhas = arquivo.readlines()
        for linha in linhas:
            objeto = linha.split()
            self.lista.append(objeto)
        arquivo.close()
        stopwords = ['de', 'a', 'o', 'que', 'e', 'do', 'da', 'em', 'um', 'para', 'e', 'com', 'nao', 'uma', 'os', 'no', 'se', 'na', 'por', 'mais', 'as', 'dos', 'como', 'mas', 'foi', 'ao', 'ele', 'das', 'tem', 'a', 'seu', 'sua', 'ou', 'ser', 'quando', 'muito', 'ha', 'nos', 'ja', 'esta', 'eu', 'tambem', 'so', 'pelo', 'pela', 'ate', 'isso', 'ela', 'entre', 'era', 'depois', 'sem', 'mesmo', 'aos', 'ter', 'seus', 'quem', 'nas', 'me', 'esse', 'eles', 'estão', 'voce', 'tinha', 'foram', 'essa', 'num', 'nem', 'suas', 'meu', 'as', 'minha', 'tem', 'numa', 'pelos', 'elas', 'havia', 'seja', 'qual', 'sera', 'nos', 'tenho', 'lhe', 'deles', 'essas', 'esses', 'pelas', 'este', 'fosse', 'dele', 'tu', 'te', 'voces', 'vos', 'lhes', 'meus', 'minhas', 'teu', 'tua', 'teus', 'tuas', 'nosso', 'nossa', 'nossos', 'nossas', 'dela', 'delas', 'esta', 'estes', 'estas', 'aquele', 'aquela', 'aqueles', 'aquelas', 'isto', 'aquilo', 'estou', 'esta', 'estamos', 'estao', 'estive', 'esteve', 'estivemos', 'estiveram', 'estava', 'estavamos', 'estavam', 'estivera', 'estiveramos', 'esteja', 'estejamos', 'estejam', 'estivesse', 'estivessemos', 'estivessem', 'estiver', 'estivermos', 'estiverem', 'hei', 'ha', 'havemos', 'hao', 'houve', 'houvemos', 'houveram', 'houvera', 'houveramos', 'haja', 'hajamos', 'hajam', 'houvesse', 'houvessemos', 'houvessem', 'houver', 'houvermos', 'houverem', 'houverei', 'houvera', 'houveremos', 'houverao', 'houveria', 'houveriamos', 'houveriam', 'sou', 'somos', 'sao', 'era', 'eramos', 'eram', 'fui', 'foi', 'fomos', 'foram', 'fora', 'foramos', 'seja', 'sejamos', 'sejam', 'fosse', 'fossemos', 'fossem', 'for', 'formos', 'forem', 'serei', 'sera', 'seremos', 'serao', 'seria', 'seriamos', 'seriam', 'tenho', 'tem', 'temos', 'tem', 'tinha', 'tinhamos', 'tinham', 'tive', 'teve', 'tivemos', 'tiveram', 'tivera', 'tiveramos', 'tenha', 'tenhamos', 'tenham', 'tivesse', 'tivessemos', 'tivessem', 'tiver', 'tivermos', 'tiverem', 'terei', 'tera', 'teremos', 'terao', 'teria', 'teriamos', 'teriam']
        path = path.split("/")
        path = f"{path[0]}/{path[1]}/{path[2]}"
        for x in range(len(self.lista)):
             self.lista[x][0] = f"{path}/{self.lista[x][0]}"
        self.textos_corrigidos = []
        for x in range(len(self.lista)):
            arquivo = open(self.lista[x][0],"r")
            texto = arquivo.read()
            texto = texto.split()
            texto_corrigido = []
            for palavra in texto:
                if not(palavra in stopwords or palavra.isnumeric()):
                    texto_corrigido.append(palavra)
            arquivo.close() 
            self.textos_corrigidos.append([texto_corrigido,self.lista[x][1]])
        self.palavras = []
        contador = 0
        for x in self.textos_corrigidos:
            for palavra in x[0]:
                if len(self.palavras) == 0:
                    self.palavras.append(palavra)
                else:
                    for word in self.palavras:
                        if palavra == word:
                            contador = 0
                            break
                        else:
                            contador+=1
                        if contador == len(self.palavras):
                            self.palavras.append(palavra)

    def size(self) -> int:
        # retornar o numero de noticias no dataset (numero de linhas no arquivo)
        return len(self.lista)

    def get(self, idx: int) -> Tuple[Any, str]:
        # ler a i-esima noticia do disco e retornar o texto como uma string e
        # a classe
        vetor = []
        for palavra in self.palavras:
            vetor.append(self.textos_corrigidos[idx][0].count(palavra))
        return (vetor,self.lista[idx][1])
