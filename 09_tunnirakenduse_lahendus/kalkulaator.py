import unittest

class Kalkulaator:

    def vajutus(self, nupp):
        if self.sisu == "0":
            self.sisu = nupp

    def ekraan(self):
        return self.sisu

    def puhasta(self):
        self.sisu = "0"
        return self.sisu

    def miinus(self):
        if self.sisu[0] == "-":
            self.sisu = self.sisu[1:]
        else:
            self.sisu = "-" + self.sisu

    def liida(self):
        self.temp = self.sisu
        self.Liida = True
        self.sisu = "0"

    def lahuta(self):
        self.temp1 = self.sisu
        self.Lahuta = True
        self.sisu = "0"

    def korruta(self):
        self.temp2 = self.sisu
        self.Korruta = True
        self.sisu = "0"

    def jaga(self):
        self.temp3 = self.sisu
        self.Jaga = True
        self.sisu = "0"

    def summa(self):
        if self.Liida == True:
            self.sisu = str(int(self.temp) + int(self.sisu))
            self.Liida = False

        elif self.Lahuta == True:
            self.sisu = str(int(self.temp1) - int(self.sisu))
            self.Lahuta = False

        elif self.Korruta == True:
            self.sisu = str(int(self.temp2) * int(self.sisu))
            self.Korruta = False

        elif self.Jaga == True:
            self.sisu = str(int(self.temp3) / int(self.sisu))
            self.Jaga = False


class TestKalkulaator(unittest.TestCase):
    k = Kalkulaator()

    #     def test_algus(self):
    #         self.assertEqual(self.k.ekraan(), "0")
    #
    #     def test_vajutus_1(self):
    #         self.k.vajutus("1")
    #         self.assertEqual(self.k.ekraan(), "1")
    #
    #     def test_vajutus_2(self):
    #         self.k.puhasta()
    #         self.k.vajutus("1")
    #         self.k.vajutus("2")
    #         self.assertEqual(self.k.ekraan(), "12")

    def test_liida(self):
        self.k.puhasta()
        self.k.vajutus("5")
        self.k.liida()
        self.k.vajutus("2")
        self.k.summa()
        self.assertEqual(self.k.ekraan(), "7")

    def test_korruta(self):
        self.k.puhasta()
        self.k.vajutus("9")
        self.k.korruta()
        self.k.vajutus("4")
        self.k.summa()
        self.assertEqual(self.k.ekraan(), "36")

    def test_jaga(self):
        self.k.puhasta()
        self.k.vajutus("9")
        self.k.jaga()
        self.k.vajutus("3")
        self.k.summa()
        self.assertEqual(self.k.ekraan(), "3.0")

    def test_miinus(self):
        self.k.puhasta()
        self.k.vajutus("10")
        self.k.miinus()
        self.assertEqual(self.k.ekraan(), "-10")


suite = unittest.TestLoader().loadTestsFromTestCase(TestKalkulaator)
runner = unittest.TextTestRunner(verbosity=1)
result = runner.run(suite)
print(f'Teste: {result.testsRun}')
