import math
def arvutus_teine_punkt():
    arvud = [400, 4, 7, 3]
    arvud_kokku = 1

    for i in arvud:
        arvud_kokku = arvud_kokku * i

    pikkus=len(arvud)
    juur = arvud_kokku ** (1 / pikkus)

    print("juur on:",juur)
arvutus_teine_punkt()

