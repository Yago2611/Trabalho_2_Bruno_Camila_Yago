path = "data/datasets/news-tiny/train.txt"
lista = []
treino = []
arquivo = open(path,"r")
linhas = arquivo.readlines()
for linha in linhas:
    objeto = linha.split()
    lista.append(objeto)
arquivo.close()
stopwords = ['de', 'a', 'o', 'que', 'e', 'do', 'da', 'em', 'um', 'para', 'e', 'com', 'nao', 'uma', 'os', 'no', 'se', 'na', 'por', 'mais', 'as', 'dos', 'como', 'mas', 'foi', 'ao', 'ele', 'das', 'tem', 'a', 'seu', 'sua', 'ou', 'ser', 'quando', 'muito', 'ha', 'nos', 'ja', 'esta', 'eu', 'tambem', 'so', 'pelo', 'pela', 'ate', 'isso', 'ela', 'entre', 'era', 'depois', 'sem', 'mesmo', 'aos', 'ter', 'seus', 'quem', 'nas', 'me', 'esse', 'eles', 'estão', 'voce', 'tinha', 'foram', 'essa', 'num', 'nem', 'suas', 'meu', 'as', 'minha', 'tem', 'numa', 'pelos', 'elas', 'havia', 'seja', 'qual', 'sera', 'nos', 'tenho', 'lhe', 'deles', 'essas', 'esses', 'pelas', 'este', 'fosse', 'dele', 'tu', 'te', 'voces', 'vos', 'lhes', 'meus', 'minhas', 'teu', 'tua', 'teus', 'tuas', 'nosso', 'nossa', 'nossos', 'nossas', 'dela', 'delas', 'esta', 'estes', 'estas', 'aquele', 'aquela', 'aqueles', 'aquelas', 'isto', 'aquilo', 'estou', 'esta', 'estamos', 'estao', 'estive', 'esteve', 'estivemos', 'estiveram', 'estava', 'estavamos', 'estavam', 'estivera', 'estiveramos', 'esteja', 'estejamos', 'estejam', 'estivesse', 'estivessemos', 'estivessem', 'estiver', 'estivermos', 'estiverem', 'hei', 'ha', 'havemos', 'hao', 'houve', 'houvemos', 'houveram', 'houvera', 'houveramos', 'haja', 'hajamos', 'hajam', 'houvesse', 'houvessemos', 'houvessem', 'houver', 'houvermos', 'houverem', 'houverei', 'houvera', 'houveremos', 'houverao', 'houveria', 'houveriamos', 'houveriam', 'sou', 'somos', 'sao', 'era', 'eramos', 'eram', 'fui', 'foi', 'fomos', 'foram', 'fora', 'foramos', 'seja', 'sejamos', 'sejam', 'fosse', 'fossemos', 'fossem', 'for', 'formos', 'forem', 'serei', 'sera', 'seremos', 'serao', 'seria', 'seriamos', 'seriam', 'tenho', 'tem', 'temos', 'tem', 'tinha', 'tinhamos', 'tinham', 'tive', 'teve', 'tivemos', 'tiveram', 'tivera', 'tiveramos', 'tenha', 'tenhamos', 'tenham', 'tivesse', 'tivessemos', 'tivessem', 'tiver', 'tivermos', 'tiverem', 'terei', 'tera', 'teremos', 'terao', 'teria', 'teriamos', 'teriam']
path = path.split("/")
path = f"{path[0]}/{path[1]}/{path[2]}"
for x in range(len(lista)):
        lista[x][0] = f"{path}/{lista[x][0]}"
textos_corrigidos = []
for x in range(len(lista)):
    arquivo = open(lista[x][0],"r")
    texto = arquivo.read()
    texto = texto.split()
    texto_corrigido = []
    for palavra in texto:
        if not(palavra in stopwords or palavra.isnumeric()):
            texto_corrigido.append(palavra)
    arquivo.close() 
    textos_corrigidos.append([texto_corrigido,lista[x][1]])
palavras = []
contador = 0
for x in textos_corrigidos:
    for palavra in x[0]:
        if len(palavras) == 0:
            palavras.append(palavra)
        else:
            for word in palavras:
                if palavra == word:
                    contador = 0
                    break
                else:
                    contador+=1
                if contador == len(palavras):
                    palavras.append(palavra)
vetor = []
for idx in range(len(lista)):
    for palavra in palavras:
            vetor.append(textos_corrigidos[idx][0].count(palavra))
    treino.append((vetor,textos_corrigidos[idx][1]))
    vetor = []


path = "data/datasets/news-tiny/test.txt"
lista = []
teste = []
arquivo = open(path,"r")
linhas = arquivo.readlines()
for linha in linhas:
    objeto = linha.split()
    lista.append(objeto)
arquivo.close()
stopwords = ['de', 'a', 'o', 'que', 'e', 'do', 'da', 'em', 'um', 'para', 'e', 'com', 'nao', 'uma', 'os', 'no', 'se', 'na', 'por', 'mais', 'as', 'dos', 'como', 'mas', 'foi', 'ao', 'ele', 'das', 'tem', 'a', 'seu', 'sua', 'ou', 'ser', 'quando', 'muito', 'ha', 'nos', 'ja', 'esta', 'eu', 'tambem', 'so', 'pelo', 'pela', 'ate', 'isso', 'ela', 'entre', 'era', 'depois', 'sem', 'mesmo', 'aos', 'ter', 'seus', 'quem', 'nas', 'me', 'esse', 'eles', 'estão', 'voce', 'tinha', 'foram', 'essa', 'num', 'nem', 'suas', 'meu', 'as', 'minha', 'tem', 'numa', 'pelos', 'elas', 'havia', 'seja', 'qual', 'sera', 'nos', 'tenho', 'lhe', 'deles', 'essas', 'esses', 'pelas', 'este', 'fosse', 'dele', 'tu', 'te', 'voces', 'vos', 'lhes', 'meus', 'minhas', 'teu', 'tua', 'teus', 'tuas', 'nosso', 'nossa', 'nossos', 'nossas', 'dela', 'delas', 'esta', 'estes', 'estas', 'aquele', 'aquela', 'aqueles', 'aquelas', 'isto', 'aquilo', 'estou', 'esta', 'estamos', 'estao', 'estive', 'esteve', 'estivemos', 'estiveram', 'estava', 'estavamos', 'estavam', 'estivera', 'estiveramos', 'esteja', 'estejamos', 'estejam', 'estivesse', 'estivessemos', 'estivessem', 'estiver', 'estivermos', 'estiverem', 'hei', 'ha', 'havemos', 'hao', 'houve', 'houvemos', 'houveram', 'houvera', 'houveramos', 'haja', 'hajamos', 'hajam', 'houvesse', 'houvessemos', 'houvessem', 'houver', 'houvermos', 'houverem', 'houverei', 'houvera', 'houveremos', 'houverao', 'houveria', 'houveriamos', 'houveriam', 'sou', 'somos', 'sao', 'era', 'eramos', 'eram', 'fui', 'foi', 'fomos', 'foram', 'fora', 'foramos', 'seja', 'sejamos', 'sejam', 'fosse', 'fossemos', 'fossem', 'for', 'formos', 'forem', 'serei', 'sera', 'seremos', 'serao', 'seria', 'seriamos', 'seriam', 'tenho', 'tem', 'temos', 'tem', 'tinha', 'tinhamos', 'tinham', 'tive', 'teve', 'tivemos', 'tiveram', 'tivera', 'tiveramos', 'tenha', 'tenhamos', 'tenham', 'tivesse', 'tivessemos', 'tivessem', 'tiver', 'tivermos', 'tiverem', 'terei', 'tera', 'teremos', 'terao', 'teria', 'teriamos', 'teriam']
path = path.split("/")
path = f"{path[0]}/{path[1]}/{path[2]}"
for x in range(len(lista)):
        lista[x][0] = f"{path}/{lista[x][0]}"
textos_corrigidos = []
for x in range(len(lista)):
    arquivo = open(lista[x][0],"r")
    texto = arquivo.read()
    texto = texto.split()
    texto_corrigido = []
    for palavra in texto:
        if not(palavra in stopwords or palavra.isnumeric()):
            texto_corrigido.append(palavra)
    arquivo.close() 
    textos_corrigidos.append([texto_corrigido,lista[x][1]])
palavras = []
contador = 0
for x in textos_corrigidos:
    for palavra in x[0]:
        if len(palavras) == 0:
            palavras.append(palavra)
        else:
            for word in palavras:
                if palavra == word:
                    contador = 0
                    break
                else:
                    contador+=1
                if contador == len(palavras):
                    palavras.append(palavra)
vetor = []
for idx in range(len(lista)):
    for palavra in palavras:
            vetor.append(textos_corrigidos[idx][0].count(palavra))
    teste.append((vetor,textos_corrigidos[idx][1]))
    vetor = []

d = 0
for t in teste:
    for tr in treino:
        for i in range(len(teste[0][0])):
            d += (t[0][i] - tr[0][i])**2
        d **= 0.5
        print(d)
        d = 0
