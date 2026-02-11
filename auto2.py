mark = list()
hp = list()
kg = list()

fm = open("autod_2025.txt", "r", encoding="utf8")
for rida in fm:
    rida = rida.strip()
    ajutine = rida.split()
    mark.append(ajutine[0])
    hp.append(int(ajutine[1]))
    kg.append(int(ajutine[2]))
fm.close()

def hp_kg_kohta(mark, hp, kg):
    for i in range(len(mark)):
        hp_kg = hp[i] / kg[i]
        print(mark[i], hp[i], "hp", kg[i], "kg", "Võimsus massi kohta:", round(hp_kg, 4), "hp/kg")

hp_kg_kohta(mark, hp, kg)