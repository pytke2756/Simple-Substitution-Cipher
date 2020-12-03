import random

def titkosit(a):
    ekezet = ["á", "é", "í", "ó", "ö", "ő", "ü", "ű"]
    ekezetNo = ["a", "e", "i", "o", "o", "o", "u", "u"]

    abc = ["a", "b", "c", "d", "e", "f", "g", "h",
        "i", "j", "k", "l", "m", "n", "o", "p",
        "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    ekezetNelkul = ekezetIrtas(ekezet, ekezetNo, a)
    uj = ""

    tabla = encryption_tableCopy(ekezetNelkul, abc)

    for i in range(0, len(ekezetNelkul)):
        char = ekezetNelkul[i]
        for i in range(0, len(char)):
            for j in range(0, len(tabla)):
                if char == tabla[j][0]:
                    uj += tabla[j][1]
    return uj, tabla

def ekezetIrtas(ekezet, ekezetnelkul, word):
    ujSzo = ""
    for i in range(0, len(word)):
        if word[i] in ekezet:
            ujSzo += ekezetnelkul[ekezet.index(word[i])]
        else:
            ujSzo += word[i]
    return ujSzo

def encryption_tableCopy(a, abc):
    normalLetter = []
    encryptedLetter = []
    table = []
    jelenlegi = ""
    for i in range(0, len(a)):
        jelenlegi = a[i]
        abcIndex = random.randint(0, len(abc)-1)

        if jelenlegi == " ":
            if jelenlegi in normalLetter:
                continue
            else:
                normalLetter.append(jelenlegi)
                encryptedLetter.append(jelenlegi)
  
        elif jelenlegi not in normalLetter and abc[abcIndex] in encryptedLetter:
            while abc[abcIndex] in encryptedLetter:
                abcIndex = random.randint(0, len(abc)-1)

        elif jelenlegi not in normalLetter and abc[abcIndex] not in encryptedLetter:
            normalLetter.append(jelenlegi)
            encryptedLetter.append(abc[abcIndex])
        
        jelenlegi = ""

    for i in range(0, len(normalLetter)):
        table.append([normalLetter[i], encryptedLetter[i]])

    return table



a = input("Add meg a titkosítandó karaktersorozatot (szám és egyéb karakter nem lehet): ")
print(titkosit(a))