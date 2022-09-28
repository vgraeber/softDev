"""
Ziying Jian, Vivian Graeber
SoftDev
K05 -- bitstream
2022-09-28
time spent: 1
"""
"""
DISCO:

QCC:

OPS: 
"""

info = open("krewes.txt", "r")
fullText = info.read()
fullText = fullText[:-1]
infoChunks = fullText.split("@@@")
infoStrings = []
for i in infoChunks:
    infoStrings.append(i.split("$$$"))
infoStrings.sort()
print(infoStrings)
info.close()