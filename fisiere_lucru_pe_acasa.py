suma=0
elementul_listei=[]
lista_clasei=[]
lista_engl2=[]
lista1=[]

with open("text.txt","r")as f:
    for i in f:
        elementul_listei=i.split()
        lista_clasei.append(elementul_listei)
        if lista_clasei[0][3]=="engl2":
            lista_engl2.append(i)
        elif lista_clasei[0][3]=="engl1":
            lista1.append(i)
        lista_clasei.clear()
        suma=suma+int(elementul_listei[2])

with open("media_totala.txt","w")as l:
    l.write("media_totala:")
    l.write(str(suma/30))
with open("engleza1.txt","w")as eng1:
    for e in lista1:
        eng1.write(e[0:-1])
        eng1.write("\n")
with open("engleza2.txt","w")as eng2:
    for e in lista_engl2:
        eng2.write(e[0:-1])
        eng2.write("\n")