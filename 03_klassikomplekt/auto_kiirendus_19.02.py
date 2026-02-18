class Auto:
    def __init__(self, nimi, hobujoud, kaal):
        self.nimi = nimi
        self.hobujoud = hobujoud
        self.kaal = kaal
        self.x = 0
        self.kiirus = 0


        joud = hobujoud * 40
        self.kiirendus = joud / kaal

    def uuenda(self, aeg):
        self.kiirus += self.kiirendus * aeg
        self.x += self.kiirus * aeg

    def kiirus_kmh(self):
        return self.kiirus * 3.6

    def positsioon(self):
        return self.nimi + ": asukoht=" + str(round(self.x,2)) + " m, kiirus=" + str(round(self.kiirus_kmh(),2)) + " km/h"


mark = list()
hp = list()
kg = list()

fm = open("autod_2025.txt", "r", encoding="utf8")

for rida in fm:
    andmed = rida.strip().split()
    mark.append(andmed[0])
    hp.append(int(andmed[1]))
    kg.append(int(andmed[2]))

fm.close()
autod = []

for i in range(len(mark)):
    auto = Auto(mark[i], hp[i], kg[i])
    autod.append(auto)

aeg = 1

print("asukoht ja kiirus igal sekundil 1–10 sekundit:")

for sekund in range(1, 11):
    for auto in autod:
        auto.uuenda(aeg)
    print(str(sekund) + " s")

    for auto in autod:
        print(auto.positsioon())
    print()

voitja = autod[0]

for auto in autod:
    if auto.x > voitja.x:
        voitja = auto

print("võitis:", voitja.nimi)

