# 2017 oktober emelt informatika erettsegi
"""

# honap nap
nev karakterkod

karakterkod: 7 karakter hosszu
O: jelen volt
X: igazolt
I: igazolatlan
N: nem volt oraja

max 50 tanulo


lista: [[honap, nap], [vezeteknev, keresztnev, kod]...]
"""

# 1. Feladat
FILENAME = "naplo.txt"
lista = []
tempLista = []
with open(FILENAME, encoding="UTF-8") as f:
    for line in f:
        sor = line[:-1]
        if sor[0] == "#" and len(tempLista) > 0:
            lista.append(tempLista)
            tempLista = [sor[2:].split(" ")]
        else:
            tempLista.append(sor.split(" "))
    else:
        lista.append(tempLista)
    del lista[0][0][0]
listahossz = len(lista)

# 2. Feladat
print("2. Feladat")
szamlalo2 = 0
for i in range(listahossz):
    szamlalo2 += len(lista[i]) - 1
print(f"A naplóban {szamlalo2} bejegyzés van.\n")
# 3. Feladat
print("3. Feladat")
igazolt = 0
igazolatlan = 0
for i in range(listahossz):
    for j in range(1, len(lista[i])):
        for betu in lista[i][j][-1]:
            if betu == "X":
                igazolt += 1
            elif betu == "I":
                igazolatlan += 1
print(f"Az igazolt hiányzások száma {igazolt}, az igazolatlanoké {igazolatlan} óra.\n")

# 4. Feladat

def hetnapja(honap, nap):
    napnev = ["vasarnap", "hetfo", "kedd", "szerda", "csutortok", "pentek", "szombat"]
    napszam = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 335]
    napsorszam = (napszam[honap-1] + nap) % 7
    return napnev[napsorszam]


# 5. Feladat
print("5. Feladat")
honap = int(input("A hónap sorszáma: "))
nap = int(input("A nap sorszáma: "))
print(f"Azon a napon {hetnapja(honap, nap)} volt.\n")

# 6. Feladat
print("6. Feladat")
hianyzas = 0
nap = input("A nap neve: ")
orasorszam = int(input("Az óra sorszáma "))

for i in range(listahossz):
    if hetnapja(int(lista[i][0][0]),int(lista[i][0][1])) == nap:
        for k in range(1, len(lista[i])):
            if lista[i][k][-1][orasorszam-1] in ["X", "I"]:
                hianyzas += 1
print(f"Ekkor összesen {hianyzas} óra hiányzás történt.\n")

# 7. Feladat
print("7. Feladat")


legnagyobb = 0
hianyzok = ""
nevek = []
for i in range(listahossz):
    for k in range(1, len(lista[i])):
        hianyzasok = [x for x in lista[i][k][-1] if x in ["X", "I"]]
        hossz = len(hianyzasok)
        if f"{lista[i][k][0]} {lista[i][k][1]} " not in nevek:
            if hossz > legnagyobb:
                hianyzok = f"{lista[i][k][0]} {lista[i][k][1]} "
                legnagyobb = hossz
            elif hossz == legnagyobb:
                hianyzok += f"{lista[i][k][0]} {lista[i][k][1]} "
        nevek.append(f"{lista[i][k][0]} {lista[i][k][1]} ")

print(f"A legtobbet hianyzok: {hianyzok}")