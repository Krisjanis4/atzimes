import json
vardnica = {}

pievienot=input("ja vēlaties vēl ievadīt atzīmes, rakstiet yes")
while pievienot == "yes":
    prieksmets=input("ievadi priekšmetu")
    # Pārbaudi vai atzīmju vārdnīcā jau ir šāda atslēga (priekšmets)
    # Ja nav, izveido jaunu masīvu
    # atzimes[prieksmets]=[]
    if prieksmets not in vardnica:
        vardnica[prieksmets]=[]

    atzime=input("ievadi atzīmi")
    # Pārbaudi vai ir diapazonā no 1 - 10, vai nv
    # 0 = nv
    # Un pie izvades -
    # if atzime = 0: print("nv")
    vardnica[prieksmets].append(atzime)
    pievienot=input("ja vēlaties vēl ievadīt atzīmes, rakstiet yes")

    print(vardnica)

'''
atzimes={}
atzimes["prieksmets 1"]=[5,6,7]
prieksmeta_nos = "prieksmets 1"
atzimes[prieksmeta_nos]
print(atzimes[prieksmeta_nos][1])
'''

for x in vardnica:
    for y in vardnica[x]:
        print(x,"atzīme ir", y)

        #fails=json.dumps((x,"atzīme ir", y))
