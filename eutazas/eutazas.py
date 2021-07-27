# 2019 oktober emelt informatika erettsegi



# 1. Feladat
FILENAME = "utasadat.txt"
lista = []
templista = []
with open(FILENAME) as f:
    for line in f:
        line = line[:-1]
        lista.append(line.split(" "))

listahossz = (len(lista))

# 2. Feladat
print("2. Feladat")
print(f"A buszra {listahossz} utas akart felszállni.\n")

# 3. Feladat
print("3. Feladat")
counter3 = 0
for i in range(listahossz):
    if lista[i][-2] != "JGY":
        if int(lista[i][1][:8]) > int(lista[i][-1]):
            counter3 += 1
    else:
        if lista[i][-1] == "0":
            counter3 += 1
print(f"A buszra {counter3} utas nem szállhatott fel.\n")

# 4. Feladat
print("4. Feladat")

foDb = 0
megallo = 0
tempFo = 1
for i in range(1, listahossz):
    if lista[i][0] == lista[i-1][0]:
        tempFo += 1
    else:
        if tempFo > foDb:
            foDb = tempFo
            megallo = lista[i-1][0]
        tempFo = 0


print(f"A legtöbb utas ({foDb}) a {megallo}. megállóban próbált felszállni.\n")

# 5. Feladat
print("5. Feladat")
kedvezmenyes = 0
ingyenes = 0
kedvezmenyesLista = ["TAB", "NYB"]
ingyenesLista = ["NYP", "RVS", "GYK"]
for i in range(listahossz):
    if lista[i][-2] in kedvezmenyesLista:
        if int(lista[i][1][:8]) <= int(lista[i][-1]):
            kedvezmenyes += 1
    elif lista[i][-2] in ingyenesLista:
        if int(lista[i][1][:8]) <= int(lista[i][-1]):
            ingyenes += 1

print(f"Ingyenesen utazók száma: {ingyenes} fő")
print(f"A kedvezményesen utazók száma: {kedvezmenyes} fő")


# 6. Feladat

def napokszama(e1, h1, n1, e2, h2, n2):
    h1 = (h1 + 9) % 12
    e1 = e1 - h1 // 10
    d1 = 365 * e1 + e1 // 4 - e1 // 100 + e1 // 400 + (h1 * 306 + 5) // 10 + n1 - 1
    h2 = (h2 + 9) % 12
    e2 = e2 - h2 // 10
    d2= 365 * e2 + e2 // 4 - e2 // 100 + e2 // 400 + (h2 * 306 + 5) // 10 + n2 - 1
    return d2-d1

# 7. Feladat

FILETOWRITE = "figyelmeztetes.txt"
with open(FILETOWRITE, "a") as f:
    for i in range(listahossz):
        if lista[i][-2] != "JGY":
            felszallasEv = int(lista[i][1][:4])
            felszallasHonap = int(lista[i][1][4:6])
            felszallasNap = int(lista[i][1][6:8])
            ervenyessegEv = int(lista[i][-1][:4])
            ervenyessegHonap = int(lista[i][-1][4:6])
            ervenyessegNap = int(lista[i][-1][6:8])
            if napokszama(felszallasEv, felszallasHonap, felszallasNap, ervenyessegEv, ervenyessegHonap, ervenyessegNap) <= 3:
                f.write(f"{lista[i][-3]} {ervenyessegEv}-{ervenyessegHonap}-{ervenyessegNap}\n")