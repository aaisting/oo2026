#Joogid

#* Koosta klass Jook, millel on nimetus, liitri omahind ning erikaal. Koosta klass Joogipudel, millel on maht, pudelityyp, mass ning taara maksumus. Samuti sees olev Jook, mis võib ka puududa. Koosta Joogipudeli jaoks käsklus, mis leiaks Joogipudeli massi koos Joogiga (juhul kui see olemas), samuti käsklus sellise komplekti omahinna leidmiseks. Koosta tööks automaattestid.
#* Koosta klass Joogivaat, millel on ruumala ning sees oleva Joogi kogus liitrites. Koosta käsk etteantud Joogipudeli täitmiseks (juhul kui Jooki jagub). Koosta käsklus kogu Joogivaaditäie Joogi viimiseks Joogipudelitesse, tühjad pudelid tuleb käsule ette anda. Koosta töö kontrolliks automaattestid.
#* Koosta Joogipudelite Kasti jaoks klass. Väljadeks kastityyp, kastihind, kastimass ning pesade arv (mitu pudelit mahub). Loo käsklused kasti ja sinna kuuluvate pudelite ühise massi ja omahinna arvutamiseks. Loo käsklus Joogivaadist Kasti sisse pudelite viimiseks. Koosta automaattestid.

#Koosta klass Jook, millel on nimetus, liitri omahind ning erikaal.

import unittest





#___________________________________________________ esimene punkt_________________________________________________________



class Jook:
    def __init__(self, nimetus, liitri_omahind, erikaal):
        self.nimetus = nimetus
        self.liitri_omahind = liitri_omahind
        self.erikaal = erikaal

#Koosta klass Joogipudel, millel on maht, pudelityyp, mass ning taara maksumus, samuti sees olev Jook, mis võib ka puududa.
class Joogipudel:
    def __init__(self, maht, pudelityyp, mass, taara_maksumus, jook):
        self.maht = maht
        self.pudelityyp = pudelityyp
        self.mass = mass
        self.taara_maksumus = taara_maksumus
        self.jook = jook

 #Koosta Joogipudeli jaoks käsklus, mis leiaks Joogipudeli massi koos Joogiga (juhul kui see olemas)
    def kogumass(self):
        if self.jook is None:
            return self.mass

        joogi_mass = self.maht * self.jook.erikaal
        return self.mass + joogi_mass

#samuti käsklus sellise komplekti omahinna leidmiseks.
    def omahind(self):
        if self.jook is None:
            return self.taara_maksumus

        joogi_hind = self.maht * self.jook.liitri_omahind
        return self.taara_maksumus + joogi_hind

#Koosta tööks automaattestid.
class TestJoogipudel(unittest.TestCase):

    def setUp(self):
        self.vesi = Jook("Vesi", 1, 1.0)
        self.pudel = Joogipudel(
            maht=1.5,
            pudelityyp="odav",
            mass=0.05,
            taara_maksumus=0.10,
            jook=self.vesi
        )

    def test_kogumass_joogiga(self):
        print("---")
        self.assertEqual(self.pudel.kogumass(), 1.55)

    def test_omahind_joogiga(self):
        print("---")
        self.assertEqual(self.pudel.omahind(), 1.6)






#___________________________________________________ teine punkt_________________________________________________________

#* Koosta klass Joogivaat, millel on ruumala ning sees oleva Joogi kogus liitrites.
class Joogivaat:
    def __init__(self, ruumala, sees_oleva_Joogi_kogus, jook):
        self.ruumala = ruumala
        self.sees_oleva_Joogi_kogus = sees_oleva_Joogi_kogus
        self.jook = jook

#Koosta käsk etteantud Joogipudeli täitmiseks (juhul kui Jooki jagub).
    def Joogipudeli_taitmine(self, joogipudel):
        if self.sees_oleva_Joogi_kogus < joogipudel.maht:
            print("Jooki on vaadis liiiga vähe!!!")
            return False

        self.sees_oleva_Joogi_kogus -= joogipudel.maht
        joogipudel.jook = self.jook
        return True

#Koosta käsklus kogu Joogivaaditäie Joogi viimiseks Joogipudelitesse, tühjad pudelid tuleb käsule ette anda.
    def Joogipudelite_taitmine(self, joogipudelid):
        taitud_pudelid = []

        for pudel in joogipudelid:
            if self.Joogipudeli_taitmine(pudel):
                taitud_pudelid.append(pudel)
            else:
                break

        return taitud_pudelid


#Koosta töö kontrolliks automaattestid.
class TestJoogivaat(unittest.TestCase):

    def setUp(self):
        self.limps = Jook("Limonaad", 2, 1.0)
        self.vaat = Joogivaat(100, 10, self.limps)

    def test_pudeli_taitmine(self):
        pudel = Joogipudel(1, "plastik", 0.1, 0.2, None)

        tulemus = self.vaat.Joogipudeli_taitmine(pudel)

        self.assertTrue(tulemus)
        self.assertEqual(self.vaat.sees_oleva_Joogi_kogus, 9)
        self.assertEqual(pudel.jook, self.limps)

    def test_mitu_pudelit(self):
        pudelid = [
            Joogipudel(1, "plastik", 0.1, 0.1, None),
            Joogipudel(1, "plastik", 0.1, 0.1, None),
            Joogipudel(1, "plastik", 0.1, 0.1, None)
        ]

        taitud = self.vaat.Joogipudelite_taitmine(pudelid)

        self.assertEqual(len(taitud), 3)
        self.assertEqual(self.vaat.sees_oleva_Joogi_kogus, 7)





#___________________________________________________ kolmas punkt _________________________________________________________


#* Koosta Joogipudelite Kasti jaoks klass. Väljadeks kastityyp, kastihind, kastimass ning pesade arv (mitu pudelit mahub). Loo käsklused kasti ja sinna kuuluvate pudelite ühise massi ja omahinna arvutamiseks. Loo käsklus Joogivaadist Kasti sisse pudelite viimiseks. Koosta automaattestid.

class Joogipudelite_Kast:
    def __init__(self, kastityyp, kastihind, kastimass, pesade_arv):
        self.kastityyp = kastityyp
        self.kastihind = kastihind
        self.kastimass = kastimass
        self.pesade_arv = pesade_arv
        self.pudelid = []

#Loo käsklused kasti ja sinna kuuluvate pudelite ühise massi ja omahinna arvutamiseks.

    def arvuta_yhine_mass(self):
        kogumass = self.kastimass

        for pudel in self.pudelid:
            kogumass += pudel.kogumass()

        return kogumass

    def arvuta_omahind(self):
        koguhind = self.kastihind

        for pudel in self.pudelid:
            koguhind += pudel.omahind()

        return koguhind


#Loo käsklus Joogivaadist Kasti sisse pudelite viimiseks.
    def vii_kasti(self, joogivaat, pudelid):

        for pudel in pudelid:

            if len(self.pudelid) >= self.pesade_arv:
                break

            if joogivaat.Joogipudeli_taitmine(pudel):
                self.pudelid.append(pudel)


# Koosta automaattestid.

class TestJoogipudeliteKast(unittest.TestCase):

    def setUp(self):
        self.vesi = Jook("Vesi", 1, 1.0)

        self.vaat = Joogivaat(100, 20, self.vesi)

        self.kast = Joogipudelite_Kast(
            "õllekast",
            5,
            1,
            6
        )

    def test_kasti_taitmine(self):

        pudelid = []

        for i in range(6):
            pudelid.append(
                Joogipudel(
                    1,
                    "plastik",
                    0.1,
                    0.2,
                    None
                )
            )

        self.kast.vii_kasti(self.vaat, pudelid)

        self.assertEqual(len(self.kast.pudelid), 6)

    def test_yhine_mass(self):

        pudel = Joogipudel(
            1,
            "plastik",
            0.1,
            0.2,
            self.vesi
        )

        self.kast.pudelid.append(pudel)

        self.assertEqual(self.kast.arvuta_yhine_mass(), 2.1)

    def test_omahind(self):

        pudel = Joogipudel(
            1,
            "plastik",
            0.1,
            0.2,
            self.vesi
        )

        self.kast.pudelid.append(pudel)

        self.assertEqual(self.kast.arvuta_omahind(), 6.2)