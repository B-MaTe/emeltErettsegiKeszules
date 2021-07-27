# 2020 Oktober emelt informatika erettsegi sorozatok feladat

# 1. Feladat
FILENAME = "lista.txt"
lista = []
templista = []
counter1 = 0

with open(FILENAME) as f:
    for line in f:
        if counter1 == 5:
            counter1 = 0
            lista.append(templista)
            templista = [line[:-1]]
        else:
            templista.append(line[:-1])
        counter1 += 1
listalen = len(lista)
#print(lista)
# 2. Feladat
print("2. Feladat\n")
counter2 = 0
for i in range(listalen):
    if lista[i][0] != "NI":
        counter2 += 1
print(f"A listában {counter2} db vetítési dátummal rendelkező epizód van.\n")


# 3. Feladat
print("3. Feladat\n")
lattaCounter3 = 0
for i in range(listalen):
    if lista[i][4] == "1":
        lattaCounter3 += 1
print(f"A listában lévő epizódok {round(lattaCounter3 * 100 / listalen, 2)} % látta.\n")

# 4. Feladat
print("4. Feladat\n")
counter4 = 0
for i in range(listalen):
    if lista[i][4] == "1":
        counter4 += int(lista[i][3])

days = counter4 // 1440
counter4 -= days * 1440
hours = counter4 // 60
counter4 -= hours * 60
minutes = counter4
print(f"Sorozatnézéssel {days} napot {hours} órát és {minutes} percet töltött.\n")

# 5. Feladat
print("5. Feladat\n")

datum = input("Adjon meg egy datumot(éééé.hh.nn): ")
datum = datum.split(".")
for i in range(listalen):
    if lista[i][0] != "NI":
        if lista[i][4] == "1":
            currentDate = "".join(lista[i][0]).split(".")
            if int(datum[0]) >= int(currentDate[0]) and int(datum[1]) >= int(currentDate[1]):
                if  int(datum[2]) >= int(currentDate[2]):
                    print(f"{lista[i][2]}   {lista[i][1]}")

# 6. Feladat

def Hetnapja(ev, ho, nap):
    napok = ["v", "h", "k", "sze", "cs", "p", "szo"]

    honapok = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    if ho < 3:
        ev -= 1
    return napok[(ev + ev // 4 - ev // 100 + ev // 400 + honapok[ho-1] + nap) % 7]

# 7. Feladat
print("7. Feladat\n")
napInput = input("Adja meg a hét egy napját (például cs)! Nap=")
counter7 = 0
for i in range(listalen):
    if lista[i][0] != "NI":
        currDate7 = lista[i][0].split(".")
        if Hetnapja(int(currDate7[0]), int(currDate7[1]), int(currDate7[2])) == napInput:
            print(lista[i][1])
            counter7 += 1
if counter7 == 0:
    print("Az adott napon nem kerül adásba sorozat.")



# 8. Feladat
FILEWRITETO = "summa.txt"
currentName = None
currentMins = 0
currentEps = 0
with open(FILEWRITETO, "a") as f:
    for i in range(listalen):
        if i == 0:
            currentName = lista[0][1]
            currentMins += int(lista[0][3])
            currentEps += 1
        else:
            if lista[i][1] == lista[i-1][1]:
                currentMins += int(lista[i][3])
                currentEps += 1
            else:
                f.write(f"{currentName} {currentMins} {currentEps}\n")
                currentName = lista[i][1]
                currentMins = 0
                currentEps = 0


