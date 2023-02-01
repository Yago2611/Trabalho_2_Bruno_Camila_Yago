texto = input("")
texto = texto.split()
for x in range(len(texto)):
    for y in range(x+1,len(texto)):
        if texto[x].upper() > texto[y].upper():
            temp = texto[x]
            texto[x] = texto[y]
            texto[y] = temp
dic = {}
cont = 0
for i in texto:
    if len(dic) == 0:
        dic = {i.lower():1}
    else:
        for x in dic:
            if x.upper() == i.upper():
                dic[x]+=1
            else:
                cont+=1
    if cont == len(dic):
        dic[i.lower()]=1
    cont = 0 
for x in dic:
    print(x,dic[x])