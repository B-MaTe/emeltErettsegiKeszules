# 2018 oktober emelt informatika erettsegi

# 1. Feladat
FILENAME = "kerites.txt"
lista = []
with open(FILENAME) as f:
    for line in f:
        line = line[:-1]
        lista.append(line.split(" "))
listahossz = len(lista)
# 2. Feladat
print("2. Feladat")
print(f"Az eladott telkek száma: {listahossz}\n")

# 3. Feladat
print("3. Feladat")
counter3 = 0
oldalDict = {
    "0": "páros",
    "1": "páratlan"
}
paros = 0
paratlan = 0
for i in range(listahossz):
    if lista[i][0] == "0":
        paros += 1
    else:
        paratlan += 1
    utsoOldal = lista[i][0]
if lista[-1][0] == "0":
    hazszam = paros * 2
else:
    hazszam = paratlan * 2 - 1
print(f"A {oldalDict[utsoOldal]} oldalon adták el az utolsó telket. ")
print(f"Az utolsó telek házszáma: {hazszam} ")

# 4. Feladat
print("4. Feladat")

def getszembeSzomszed(haz, sor):
    lineCounter1 = 0
    oldal1 = 1
    while lineCounter1 != sor:
        if haz[0] == lista[lineCounter1][0]:
            oldal1 += 1
        lineCounter1 += 1

    lineCounter2 = 0
    oldal2 = 0
    while oldal2 != oldal1 and lineCounter2 < listahossz:
        if haz[0] != lista[lineCounter2][0]:
            oldal2 += 1
        lineCounter2 += 1
    return lista[lineCounter1], lista[lineCounter2-1], oldal1
for i in range(listahossz):
    if lista[i][0] == "1":
        if lista[i][2] not in [":", "#"]:
            if getszembeSzomszed(lista[i], i)[0][2] == getszembeSzomszed(lista[i], i)[1][2]:
                print(getszembeSzomszed(lista[i], i)[0], getszembeSzomszed(lista[i], i)[1])
                print(f"A szomszédossal egyezik a kerítés színe: {getszembeSzomszed(lista[i], i)[2]}\n")



# 5. Feladat
print("5. Feladat")
hazszam5 = int(input("Adjon meg egy házszámot!"))
if hazszam5 % 2 == 0:
    oldal = "0"
    div = 0
else:
    oldal = "1"
    div = 1
oldal5 = div
sor5 = 0
while oldal5 - div < hazszam5:
    try:
        if lista[sor5][0] == oldal:
            oldal5 += 2
        sor5 += 1
    except IndexError:
        print("Nincs ekkoraa hazszam az utcaban")
        quit()

lehetosegek = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(f"A kerítés színe / állapota: {lista[sor5-1][2]}")
counter5 = 1
while True:
    if lista[sor5-1-counter5][0] == lista[sor5-1][0]:
        visszaSzomszed = lista[sor5-1-counter5]
        break
    counter5 += 1

counter51 = 1
while True:
    if lista[sor5-1+counter51][0] == lista[sor5-1][0]:
        eloreSzomszed = lista[sor5-1-counter51]
        break
    counter51 += 1

foglaltSzinek = [lista[sor5-1][2], eloreSzomszed[2], visszaSzomszed[2]]
for szin in lehetosegek:
    if szin not in foglaltSzinek:
        veglegesSzin = szin
        break
print(f"Egy lehetséges festési szín: {veglegesSzin}")


# 6. Feladat
FILEWRITETO = "utcakep.txt"
firstStr = ""
secondStr = ""
counter6 = 1
optimizer = 1
for i in range(listahossz):
    if len(str(counter6)) > len(str(counter6 - 2)):
        optimizer += 1
    if lista[i][0] == "1":
        firstStr += int(lista[i][1]) * lista[i][2]
        secondStr += str(counter6) + (int(lista[i][1]) - optimizer) * " "
    counter6 += 2
with open(FILEWRITETO, "a") as f:
    f.write(firstStr + "\n")
    f.write(secondStr)
