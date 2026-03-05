class PalgaKalkulaator:
    def __init__(self, esimese_aasta_palk):
        self.palgad = [esimese_aasta_palk]
        self.koefitsiendid = []

    def lisa_aasta_koefitsiendiga(self, koefitsent):
        viimane_palk = self.palgad[-1]
        uus_palk = viimane_palk * koefitsent
        self.koefitsiendid.append(koefitsent)
        self.palgad.append(uus_palk)

    def lisa_mitu_aastat_koefitsentidega(self, koefitsiendid):
        for koefitsent_2 in koefitsiendid:
            self.lisa_aasta_koefitsiendiga(koefitsent_2)

    def lisa_aasta_palk(self, palk):
        viimane_palk = self.palgad[-1]
        koefitsent = palk / viimane_palk
        self.koefitsiendid.append(koefitsent)
        self.palgad.append(palk)

    def palkade_ajalugu(self):
        ajalugu = []

        for i in range(len(self.palgad)):
            aasta = i + 1
            palk = self.palgad[i]
            palk_ümmardatud = round(palk, 2)
            rida = f"Aasta {aasta}: {palk_ümmardatud}"
            ajalugu.append(rida)

        ajalugu.append("Koefitsiendid:")
        for i in range(len(self.koefitsiendid)):
            aasta = i + 2
            koef = self.koefitsiendid[i]
            koef_ümmardatud = round(koef, 3)
            rida = f"Aasta {aasta}: {koef_ümmardatud}"
            ajalugu.append(rida)
        return ajalugu

    def arvutus_geomeetriline_keskmine(self):
        if not self.koefitsiendid:
            print("Koefitsiente pole arvutamiseks.")
            return None

        arvud = self.koefitsiendid
        arvud_kokku = 1

        for i in arvud:
            arvud_kokku *= i

        pikkus = len(arvud)
        juur = arvud_kokku ** (1 / pikkus)

        print("Geomeetriline keskmine on:",juur,)
        return juur

    def palkade_geomeetriline_kasv(self):
        geokeskmine = self.arvutus_geomeetriline_keskmine()
        palkade_geokeskmine = [round(self.palgad[0], 2)]
        palk = self.palgad[0]
        print("\nPalkade geomeetriline kasv:")
        print(f"Aasta {round(palk, 2)}")

        for i in range(len(self.koefitsiendid)):
            palk *= geokeskmine
            palk_ümmardatud = round(palk, 2)
            palkade_geokeskmine.append(palk_ümmardatud)
            print(f"Aasta:  {palk_ümmardatud}")

        return palkade_geokeskmine

kalkulaator = PalgaKalkulaator(2500)
kalkulaator.lisa_mitu_aastat_koefitsentidega([0.68, 1.1, 1.05, 1.18, 1.78])
kalkulaator.palkade_geomeetriline_kasv()

for rida in kalkulaator.palkade_ajalugu():
    print(rida)

kalkulaator.arvutus_geomeetriline_keskmine()
kasv = kalkulaator.palkade_geomeetriline_kasv()
