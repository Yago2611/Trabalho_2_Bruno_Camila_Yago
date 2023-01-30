from typing import Dict

def load_config(path: str) -> Dict:
    """ le o arquivo json e retorna como um dicionario """
    arquivo = open(path,"r")
    x = arquivo.read()
    dict = json.loads(x)
    arquivo.close()
    return dict
