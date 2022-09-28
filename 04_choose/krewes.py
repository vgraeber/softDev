"""
TNPG: VAT, Vivian Graeber, Ayman Habib, Talia Hsia

DISCO:
- Files do not need an extension, the computer looks at the metadata inside the file

QCC:

OPS SUMMARY: Given a dictionary of periods with the class roster assigned to each, and a list with the period numbers, the function randomly chooses a number from the list of period numbers, stores it in the variable 'pd', and then accesses the roster for that period using the dictionary. The function then randomly selects a name from the roster and stores the name in the 'name' variable. Then, it prints out the period and the name.

"""
import random
krewes = {
    2:["NICHOLAS", "ANTHONY", "BRIAN", "SAMUEL", "JULIA", "YUSHA", "CRAIG", "FANG MIN", "JEFF", "KONSTANTIN", "AARON", "VIVIAN", "AYMAN", "TALIA", "FAIZA", "ZIYING", "YUK KWAN", "DANIEL", "WEICHEN", "MAYA", "ELIZABETH", "ANDREW", "VANSH", "JONATHAN", "ABID", "WILLIAM", "HUI", "ANSON", "KEVIN", "DANIEL", "IVAN", "JASMINE", "JEFFREY", "Ruiwen"], 
    7:["DIANA", "DAVID", "SAM", "PRATTAY", "ANNA", "JING YI", "ADEN", "EMERSON", "RUSSELL", "JACOB", "WILLIAM", "NADA", "SAMANTHA", "IAN", "MARC", "ANJINI", "JEREMY", "LAUREN", "KEVIN", "RAVINDRA", "SADI", "EMILY", "GITAE", "MAY", "MAHIR", "VIVIAN", "GABRIEL", "BRIANNA", "JUN HONG", "JOSEPH", "MATTHEW", "JAMES", "THOMAS", "NICOLE", "Karen"],
    8:["ALEKSANDRA", "NAKIB", "AMEER", "HENRY", "DONALD", "YAT LONG", "SEBASTIAN", "DAVID", "YUKI", "SHAFIUL", "DANIEL", "SELENA", "JOSEPH", "SHINJI", "RYAN", "APRIL", "ERICA", "JIAN HONG", "VERIT", "JOSHUA", "WILSON", "AAHAN", "GORDON", "JUSTIN", "MAYA", "FAIYAZ", "SHREYA", "ERIC", "JEFFERY", "BRIAN", "KEVIN", "SAMSON", "BRIAN", "HARRY", "CORINA", "Wanying", "Kevin"]
         }
pd_list = [2, 7, 8]
pd = random.choice(pd_list)
name = random.choice(krewes[pd])

print(str(pd) + ' ' + name)