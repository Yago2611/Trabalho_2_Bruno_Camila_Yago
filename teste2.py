import cv2

path = "data/datasets/img_small/train.txt"
lista = []
dados_treino = []
arquivo = open(path,"r")
linhas = arquivo.readlines()
for linha in linhas:
    objeto = linha.split()
    lista.append(objeto)
arquivo.close()
for x in range(len(lista)):
    img = cv2.imread(lista[x][0],0) 
    img = img.tolist()
    image = []
    for y in img:
        for x in y:
            image.append(x)
    dado = (image,lista[x][1])
    dados_treino.append(dado)
print(dados_treino)