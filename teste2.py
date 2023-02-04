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
    for i in img:
        for j in i:
            image.append(j)
    dado = (image,lista[x][1])
    dados_treino.append(dado)

path = "data/datasets/img_small/test.txt"
lista = []
dados_teste = []
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
    for i in img:
        for j in i:
            image.append(j)
    dado = (image,lista[x][1])
    dados_teste.append(dado)

cicloides = []
dif_classes = []
for x in dados_treino:
    if len(dif_classes) == 0 or not x[1] in dif_classes:
        dif_classes.append(x[1])
for x in dif_classes:
    soma = 0
    contador = 0
    for y in dados_treino:
        if y[1] == x:
            contador +=1
            if soma ==0:
                soma = y[0]
            else:
                for i in range(len(soma)):
                    soma[i] += y[0][i]
    for i in range(len(soma)):
        soma[i] /= contador
    cicloides.append((soma,x))
for x in cicloides:
    print(x)
"""previsoes = []
for teste in dados_teste:
    distancias = []
    dic = {}
    previsao = 0 
    for treino in dados_treino:
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
                    break
    for i in distancias:
        cont = 0
        if len(dic) == 0:
            dic = {i[1]:1}
        else:
            for x in dic:
                if i[1] == x:
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
classes = []
for x in lista:
    classes.append(x[1])
dif_classes = []
for x in classes:
    if len(dif_classes) == 0 or not x in dif_classes:
        dif_classes.append(x)
matriz = []
for x in dif_classes:
    vetor = []
    for y in dif_classes:
        valor = 0
        for n in range(len(classes)):
            if classes[n] == x and previsoes[n] == y:
                valor +=1
        vetor.append(valor)
    matriz.append(vetor)"""