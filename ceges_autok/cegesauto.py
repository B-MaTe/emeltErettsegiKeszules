# 2019 Majus emelt informatika erettsegi programozas Python

INFOFILE = "autok.txt"
#1. Feladat
file = open(INFOFILE)
infoList = []
for line in file:
    infoList.append(line[0:-1].split(" "))
file.close()
listLen = len(infoList)
#2. Feladat
print("2. Feladat\n")

for i in range(listLen):
    if infoList[i][5] == '0':
        index = i
        vegso = infoList
print(f"{vegso[index][0]}. nap rendszam: {vegso[index][2]}\n")


#3. Feladat

kiBeList = [
    "ki", "be"
]
print("3. Feladat\n")
nap = input("Adjon meg egy napot: ")
print(f"Forgalom a(z) {nap}. napon: ")
for i in range(listLen):
    if nap == infoList[i][0]:
        print(f"{infoList[i][1]} {infoList[i][2]} {infoList[i][3]} {kiBeList[int(infoList[i][5])]}\n")

#4. Feladat
print("4. Feladat\n")
counter4 = 0
for i in range(listLen):
    if infoList[i][5] == '0':
        counter4 += 1
    elif infoList[i][5] == '1':
        counter4 -= 1
print(f"A hónap végén {counter4} autót nem hoztak vissza.\n")

#5. Feladat
print("5. Feladat\n")
carList = []
for i in range(listLen):
    if infoList[i][2] not in carList:
        carList.append(infoList[i][2])
carListLen = len(carList)
counter5 = 0
currentKm = 0
kiKm = 0
while counter5 < carListLen:
    for i in range(listLen):
        if infoList[i][2] == carList[0]:
            if infoList[i][5] == '0':
                kiKm = infoList[i][4]
            else:
                currentKm += int(infoList[i][4]) - int(kiKm)
    counter5 += 1
    print(f"{carList[0]} {currentKm} km")
    carList.pop(0)
    currentKm = 0
    kiKm = 0

#6. Feladat
print("6. Feladat\n")
personList = []
for i in range(listLen):
    if infoList[i][3] not in personList:
        personList.append(infoList[i][3])
personListLen = len(personList)
counter6 = 0
highest = 0
highestPerson = 0
tempCounter6 = 0
kiKm = 0
while counter6 < personListLen:
    for i in range(listLen):
        if infoList[i][3] == personList[0]:
            if infoList[i][5] == '0':
                kiKm = infoList[i][4]
            else:
                if int(infoList[i][4]) - int(kiKm) > tempCounter6:
                    tempCounter6 = int(infoList[i][4]) - int(kiKm)
    if tempCounter6 > highest:
        highestPerson = infoList[i][3]
        highest = tempCounter6
    counter6 += 1
    personList.pop(0)
    tempCounter6 = 0
    kiKm = 0
print(f"Leghosszabb út: {highest} km, személy: {highestPerson}\n")

#7. Feladat
print("7. Feladat\n")
# 588 21. 16:58 13452 km 23. 20:28 14335 km
rendszam = input("Adjon meg egy rendszamot: ")
FILE = f"{rendszam}_menetlevel.txt"

with open(FILE, "a") as f:
    for i in range(listLen):
        flag = False
        if infoList[i][2] == rendszam:
            if infoList[i][5] == '0':
                for j in range(i + 1, listLen):
                    if infoList[j][2] == rendszam and infoList[j][5] == '1':
                        flag = True
                        f.write(f"{infoList[i][3]}    {infoList[i][0]}. {infoList[i][1]}    {infoList[i][4]}   {infoList[j][0]}. {infoList[j][1]}    {infoList[j][4]}\n")
                        break
                if not flag:
                    f.write(f"{infoList[i][3]}    {infoList[i][0]}. {infoList[i][1]}    {infoList[i][4]}\n")
    print("Menetrend kesz!")


