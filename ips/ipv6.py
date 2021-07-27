# 2014 tavasz emelt informatika erettsegi feladat


# 1. Feladat
IPS = "ip.txt"

file = open(IPS)

# 2. Feladat
print("2. Feladat")
counter = 0
for line in file:
    counter += 1
print(f"Az allomanyban {counter} IP van.")
file.close()

# 3. Feladat
print("3. Feladat")
file = open(IPS)
hexavalues = {
    "a": 10,
    "b": 11,
    "c": 12,
    "d": 13,
    "e": 14,
    "f": 15
}
lowest = None
temp = 0
linecounter = 0
savedline = 0
for char in file.read():
    if char == "\n":
        linecounter += 1
        if lowest is None or temp < lowest:
            lowest = temp
            savedline = linecounter
        temp = 0
        continue
    elif char == ":" or char == 0:
        continue
    try:
        temp += int(char)
    except:
        temp += hexavalues[char]


file.close()
file = open(IPS)

for pos, line in enumerate(file, start=1):
    if pos == savedline:
        print(f"A legrovidebb IP cim: {line}")
        break
file.close()


# 4. Feladat

file = open(IPS)
print("4. Feladat")

dokumentacios = 0
globalis = 0
helyi = 0
for line in file:
    if line[:9] == '2001:0db8':
        dokumentacios += 1
    elif line[:7] == '2001:0e':
        globalis += 1
    elif line[:2] == 'fc' or line[:2] == 'fd':
        helyi += 1
file.close()

print(f"Dokumentációs cím: {dokumentacios}")
print(f"Globális egyedi cím: {globalis}")
print(f"Helyi egyedi cím: {helyi}")

# 5. Feladat

file = open(IPS)
file_save_to = "sok.txt"
for i, line in enumerate(file, start=1):
    zeros = 0
    active = True
    counter5 = 0
    while active:
        if line[counter5] == '0':
            zeros += 1
        if zeros >= 18:
            with open(file_save_to, "a") as f:
                #f.write(f"{i} {line}")
                active = False
        if line[counter5] == '\n':
            active = False
        counter5 += 1

f.close()

# 6. Feladat

print("6. Feladat")

file = open(IPS)
lineInput = int(input("Adjon meg egy sorszamot: "))
for index, line in enumerate(file, start=1):
    if index == lineInput:
        choosenLine = line
        break

print(choosenLine[:-1])
lineList = list(choosenLine)
counter6 = 0
tempCounter = 0
while True:
    if lineList[-1] == lineList[counter6]:
        break
    elif str(lineList[counter6]) == '0':
        if lineList[counter6: counter6 + 4] == ['0', '0', '0', '0']:
            del lineList[counter6: counter6 + 3]
            counter6 += 2
        else:
            lineList.pop(counter6)
    else:

        while True:
            if lineList[-1] == lineList[counter6]:
                break
            elif lineList[counter6] == ':':
                counter6 += 1
                break
            counter6 += 1


final6 = "".join(lineList)
print(final6)

# 7. Feladat
print("7. Feladat")
counter7 = 0
shortenedIp = lineList
i = 0
tempCounter = 0
zeroCounter = 0
zeroI = 0
while True:
    #print(zeroCounter)
    if shortenedIp[counter7 + i] == '\n':
        if tempCounter > zeroCounter:
            zeroCounter = tempCounter
        break
    elif shortenedIp[counter7 + i: counter7 + 2 + i] == [':', '0']:
        print('a')
        tempCounter += 1
        zeroI = counter7
        i += 2
    else:
        if tempCounter > zeroCounter:
            zeroCounter = tempCounter
        counter7 += i + 1
        tempCounter = 0
        i = 0
if zeroI != 0:
    del shortenedIp[zeroI: zeroI + zeroCounter * 2]
    shortenedIp.insert(zeroI, ":")
if "".join(shortenedIp) == final6:
    print("Nem rövidíthető tovább.")
else:
    print("".join(shortenedIp))


