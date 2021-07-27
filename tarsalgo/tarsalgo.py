# 2019 Majus emelt informatika erettsegi programozas


# 1. Feladat
lista = []
FILENAME = "ajto.txt"
with open(FILENAME, encoding="UTF-8") as f:
    for line in f:
        line = line[:-1]
        line = line.split(" ")
        for i in range(len(line)):
            try:
                line[i] = int(line[i])
            except:
                pass
        lista.append(line)

listahossz = len(lista)
# 2. Feladat
print("2. Feladat")
print(f"Az első belépő: {lista[0][2]}")
utolso = None
for i in range(listahossz):
    if lista[i][3] == "ki":
        utolso = lista[i][2]
print(f"Az utolsó kilépő: {utolso}\n")

# 3. Feladat
FILEWRITETO = "athaladas.txt"
emberek = []
for i in range(listahossz):
    if lista[i][2] not in emberek:
        emberek.append(lista[i][2])
emberek.sort()

for ember in emberek:
    athaladas = 0
    for i in range(listahossz):
        if lista[i][2] == ember:
            athaladas += 1
    with open(FILEWRITETO, "a") as f:
        f.write(f"{ember} {athaladas}\n")

# 4. Feladat
print("4. Feladat")
vegso = []
for ember in emberek:
    bentVan = False
    for i in range(listahossz):
        if lista[i][2] == ember:
            bentVan = not bentVan
    if bentVan:
        vegso.append(str(ember))
print(f"A végén a társalgóban voltak: {' '.join(vegso)}")

# 5. Feladat
print("5. Feladat")

def idoAtvalo(ido1, ido2):
    if ido1 < 10:
        ido1 = str(ido1)
        if ido2 < 10:
            ido2 = str(ido2)
            return '0' + ido1 + ':' + '0' + ido2
        ido2 = str(ido2)
        return '0' + ido1 + ':' + ido2
    elif ido2 < 10:
        ido1 = str(ido1)
        ido2 = str(ido2)
        return ido1 + ':' + '0' + ido2
    ido1 = str(ido1)
    ido2 = str(ido2)
    return ido1 + ':' + ido2

legmagasabb = 0
szemelyek = 0
idopont = None
for i in range(listahossz):
    if lista[i][3] == "be":
        szemelyek += 1
        if szemelyek >= legmagasabb:
            legmagasabb = szemelyek
            idopont = f"{idoAtvalo(lista[i][0],lista[i][1])}"
    else:
        szemelyek -= 1

print(f"Például {idopont}-kor voltak a legtöbben a társalgóban.")

# 6. Feladat
print("6. Feladat")
ID = int(input("Adja meg a személy azonosítóját! "))

# 7. Feladat
print("7. Feladat")

flag = True
teljesIdo = 0
for i in range(listahossz):
    if lista[i][2] == ID:
        if flag:
            firstPart = idoAtvalo(lista[i][0], lista[i][1]) + "-"
            tempIdo = lista[i][0] * 60 + lista[i][1]
            flag = False
        else:
            print(f"{firstPart}{idoAtvalo(lista[i][0], lista[i][1])}")
            teljesIdo += (lista[i][0] * 60 + lista[i][1]) - tempIdo
            flag = True
if not flag:
    teljesIdo += (15 * 60) - tempIdo
    print(firstPart)
print("\n")
# 8. Feladat
print("8. Feladat")
if not flag:
    print(f"A(z) {ID}. személy összesen {teljesIdo} percet volt bent, a megfigyelés végén a társalgóban volt. ")
else:
    print(f"A(z) {ID}. személy összesen {teljesIdo} percet volt bent, a megfigyelés végén nem volt a társalgóban.")