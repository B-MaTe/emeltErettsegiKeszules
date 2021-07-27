# 2015 emelt informatika erettsegi programozas



# 1. Feladat
FILENAME = "veetel.txt"
lista = []
tempLista = []
with open(FILENAME, encoding="UTF-8") as f:
    for index, line in enumerate(f, 1):
        line = line[:-1]
        if index % 2 != 0:
            tempLista.append(line.split(" "))
        else:
            tempLista.append(line)
            lista.append(tempLista)
            tempLista = []
listahossz = len(lista)
# 2. Feladat
print("2. Feladat")
print(f"Az első üzenet rögzítője: {lista[0][0][-1]}")
print(f"Az utolsó üzenet rögzítője: {lista[-1][0][-1]}")


# 3. Feladat
print("3. Feladat")
keresettSzo = "farkas"
for i in range(listahossz):
    for j in range(len(lista[i][1]) - len(keresettSzo)):
        if lista[i][1][j:j + len(keresettSzo)] == keresettSzo:
            print(f"{lista[i][0][0]}. nap {lista[i][0][1]}. rádióamatőr")

# 4. Feladat
print("4. Feladat")

napok = [x for x in range(1, 12)]

for nap in napok:
    feljegyzes = 0
    for i in range(listahossz):
        if lista[i][0][0] == str(nap):
            feljegyzes += 1
    print(f"{nap}. nap: {feljegyzes} rádióamatőr")



# 5. Feladat
FILEWRITETO = "adaas.txt"

def uzenetDecode(helyzet, nap, uzenet):
    for i in range(listahossz):
        if lista[i][0][0] == str(nap):
            if lista[i][1][helyzet] != "#":
                return uzenet + lista[i][1][helyzet]
    return uzenet + "#"

uzenetHossz = 90
for nap in napok:
    uzenet = ""
    helyzet = 0
    for i in range(uzenetHossz):
        uzenet = uzenetDecode(i, nap, uzenet)
    #with open(FILEWRITETO, "a") as f:
        #f.write(f"{nap}. nap: {uzenet}\n")



# 6. Feladat

def szame(szo):
    valasz = True
    for i in range(1, len(szo)):
        if szo[i] < '0' or szo[i] > '9':
            valasz = False

    return valasz

# 7. Feladat
print("7. Feladat")
napSzam = int(input("Adja meg a nap sorszámát! "))
radioAmator = int(input("Adja meg a rádióamatőr sorszámát! "))
volt = False
valasztottRekord = None
if napSzam in napok:
    for i in range(listahossz):
        if int(lista[i][0][0]) == napSzam:
            if int(lista[i][0][1]) == radioAmator:
                valasztottRekord = lista[i][1][:5]
                volt = True
                break
    if not volt:
        print("Nincs ilyen feljegyzes")
        quit()
else:
    print("Nincs ilyen feljegyzes")
    quit()

if valasztottRekord and "/" in valasztottRekord:
    kisFarkas = 0
    nagyFarkas = 0
    flag = False
    for jel in range(len(valasztottRekord)):
        try:
            jel = int(jel)
            if not flag and valasztottRekord[jel+1] == "/":
                kisFarkas = int(valasztottRekord[jel])
            elif valasztottRekord[jel+2] == "/":
                flag = True
                kisFarkas = int(valasztottRekord[jel:jel + 2])
            elif valasztottRekord[jel+1] == " ":
                nagyFarkas = int(valasztottRekord[jel])
            elif valasztottRekord[jel+2] == " ":
                nagyFarkas = int(valasztottRekord[jel:jel + 2])
                break
        except:
            continue
    print(f"A megfigyelt egyedek száma: {kisFarkas + nagyFarkas}")
else:
    print("Nincs információ")