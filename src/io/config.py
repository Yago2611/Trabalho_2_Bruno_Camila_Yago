from typing import Dict

def load_config(path: str) -> Dict:
    """ le o arquivo json e retorna como um dicionario """
    arquivo = open(path,"r")
    x = arquivo.readlines()
    index = 0
    for y in x:
        y = y.replace("{","")
        y = y.replace("}","")
        y = y.replace(":","")
        y = y.replace("\n","")
        y = y.replace("\"","")
        y = y.strip()
        if " " in y:
            y = y.split()
        x[index] = y
        print(y)
        index+=1
    x.remove("")
    x.remove("")
    x.remove(",")
    x.remove(",")
    print(x)
    dict = {x[0]:{x[1][0]:x[1][1],x[2][0]:x[2][1]},x[3]:{x[4][0]:x[4][1],x[5][0]:x[5][1]},x[6]:{x[7][0]:x[7][1]}}
    arquivo.close()
    return dict
