# 2020 Majus emelt informatika erettsegi


# 1. Feladat
FILENAME = "tavirathu13.txt"
lista = []
with open(FILENAME, encoding="utf-8") as f:
    for line in f:
        line = line[:-1]
        lista.append(line.split(" "))

listahossz = len(lista)
# 2. Feladat
print("2. Feladat")
varos = input("Adja meg egy település kódját! Település: ")
savedVaros = None
for i in range(listahossz):
    if lista[i][0] == varos:
        savedVaros = lista[i]

if savedVaros:
    print(f"Az utolsó mérési adat a megadott településről {savedVaros[1][0:2]}:{savedVaros[1][2:]}-kor érkezett.\n")
else:
    print("Nincs ilyen varos a rendszerben!\n")

# 3. Feladat
print("3. Feladat")
legalacsonyabb = None
legmagasabb = None

for i in range(listahossz):
    if not legalacsonyabb or int(lista[i][3]) < int(legalacsonyabb[3]):
        legalacsonyabb = lista[i]
    elif not legmagasabb or int(lista[i][3]) > int(legmagasabb[3]):
        legmagasabb = lista[i]
print(f"A legalacsonyabb hőmérséklet: {legalacsonyabb[0]} {legalacsonyabb[1][0:2]}:{legalacsonyabb[1][2:]} {legalacsonyabb[3]} fok. ")
print(f"A legalacsonyabb hőmérséklet: {legmagasabb[0]} {legmagasabb[1][0:2]}:{legmagasabb[1][2:]} {legmagasabb[3]} fok.\n")


# 4. Feladat
print("4. Feladat")
voltE = False
for i in range(listahossz):
    if lista[i][2] == "00000":
        print(f"{lista[i][0]} {lista[i][1][0:2]}:{lista[i][1][2:]}")
        voltE = True

if not voltE:
    print("Nem volt szélcsend a mérések idején.")
print("\n")

# 5. Feladat
print("5. Feladat")

varosok = []
for i in range(listahossz):
    if lista[i][0] not in varosok:
        varosok.append(lista[i][0])



while varosok:
    idopontok = ['01', '07', '13', '19']
    idopontok2 = idopontok.copy()
    legalacsonyabbHomerseklet = None
    legmagasabbHomerseklet = None
    homersekletekSzama = 0
    homersekletekOsszege = 0
    for i in range(listahossz):
        if lista[i][0] == varosok[0]:
            if lista[i][1][:2] in idopontok:
                if lista[i][1][:2] in idopontok2:
                    idopontok2.remove(lista[i][1][:2])
                homersekletekOsszege += int(lista[i][3])
                homersekletekSzama += 1
            if not legalacsonyabbHomerseklet or legalacsonyabbHomerseklet > int(lista[i][3]):
                legalacsonyabbHomerseklet = int(lista[i][3])
            elif not legmagasabbHomerseklet or legmagasabbHomerseklet < int(lista[i][3]):
                legmagasabbHomerseklet = int(lista[i][3])
    if idopontok2:
        print(f"{varosok[0]} NA; Hőmérséklet-ingadozás: {abs(legmagasabbHomerseklet - legalacsonyabbHomerseklet)}")
    else:
        print(f"{varosok[0]} Középhőmérséklet: {homersekletekOsszege // homersekletekSzama}; Hőmérséklet-ingadozás: {abs(legmagasabbHomerseklet - legalacsonyabbHomerseklet)}")
    varosok.pop(0)
print("\n")

# 6. Feladat
print("6. Feladat")
varosok6 = []
for s in range(listahossz):
    if lista[s][0] not in varosok6:
        varosok6.append(lista[s][0])
print(varosok6)
for varos6 in varosok6:
    FILEWRITETO = varos6
    with open(FILEWRITETO, 'a') as f:
        f.write(varos6 + "\n")
        for k in range(listahossz):
            if lista[k][0] == FILEWRITETO:
                f.write(f"{lista[k][1][0:2]}:{lista[k][1][2:]} {int(lista[k][2][-2:]) * '#'}\n")