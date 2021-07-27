# 2016 majus emelt erettsegi programozas

# 1. Feladat
FILENAME = "penztar.txt"
lista = []
templista = []
with open(FILENAME) as f:
    for line in f:
        if line[:-1] == "F":
            lista.append(templista)
            templista = []
        else:
            templista.append(line[:-1])
listahossz = len(lista)
# 2. Feladat
print("2. Feladat")
print(f"A fizetések száma: {listahossz}\n")

# 3. Feladat
print("3. Feladat")
print(f"Az első vásárló {len(lista[0])} darab árucikket vásárolt.\n")

# 4. Feladat
print("4. Feladat")
sorszam = int(input("Adja meg egy vásárlás sorszámát! "))
termek = input("Adja meg egy árucikk nevét! ")
darab = int(input("Adja meg a vásárolt darabszámot!"))
print("\n")

# 5. Feladat
print("5. Feladat")
counter5 = 0
elso = listahossz
utolso = 0
for i in range(listahossz):
    if termek in lista[i]:
        if i < elso:
            elso = i
        else:
            utolso = i
for i in range(listahossz):
    for j in range(len(lista[i])):
        if lista[i][j] == termek:
            counter5 += 1

print(f"Az első vásárlás sorszáma: {elso + 1}")
print(f"Az utolsó vásárlás sorszáma: {utolso + 1}")
print(f"{counter5} vásárlás során vettek belőle.\n")

# 6. Feladat
print("6. Feladat")
def ertek(darab):
    akcio = 500 + 450 + 400
    if darab > 3:
        vegleges = akcio + (darab-3) * 400
    elif darab == 3:
        vegleges = akcio
    elif darab == 2:
        vegleges = 950
    elif darab == 1:
        vegleges = 500
    return vegleges
print(f"{darab} darab vételekor fizetendő: {ertek(darab)}\n")

# 7. Feladat
print("7. Feladat")
darabCounter = 1
counter7 = len(lista[sorszam - 1])
currentLine = lista[sorszam - 1].copy()
sideCounter7 = 0
while counter7 > 0:
    currentItem = currentLine[0]
    for i in range(1, len(currentLine)):
        if currentLine[i] == currentItem:
            darabCounter += 1
    print(f"{darabCounter} {currentItem}")
    counter7 -= darabCounter
    darabCounter = 1
    while currentItem in currentLine:
        if currentLine[sideCounter7] == currentItem:
            del currentLine[sideCounter7]
            sideCounter7 = 0
        else:
            sideCounter7 += 1

# 8. Feladat
FILEWRITETO = "osszeg.txt"
for k in range(listahossz):
    vegosszeg = 0
    counter8 = len(lista[k])
    currentLine8 = lista[k]
    darabCounter = 1
    sideCounter8 = 0
    while counter8 > 0:
        currentItem = currentLine8[0]
        for i in range(1, len(currentLine8)):
            if currentLine8[i] == currentItem:
                darabCounter += 1
        vegosszeg += int(ertek(darabCounter))
        counter8 -= darabCounter
        darabCounter = 1
        while currentItem in currentLine8:
            if currentLine8[sideCounter8] == currentItem:
                del currentLine8[sideCounter8]
                sideCounter8 = 0
            else:
                sideCounter8 += 1
    else:
        with open(FILEWRITETO, "a") as f:
            f.write(f"{k+1}: {vegosszeg}\n")
