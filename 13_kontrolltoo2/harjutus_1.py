#   Esimene ülesanne:
#       koosta liides või abstraktne klass joone y-i väärtuste leidmiseks vastavalt x-i väärtusele.
#       Koosta automaattestid kontrollimaks, mitu punkti sirgel y=3x.
#       Koosta realiseeriv klass, millele antakse konstruktoris ettex-i kordaja. Kontrolli klassi eksemplari oskuste vastavalt testidele.
#   Teine ülesanne:
#       Loo teine realiseeriv klass, millele saab ette anda kordaja ja vabaliikme.
#       Kontrolli selle klassi tööd liidese kaudu testidega joontele y =3x ning y=3x+2.
#       Koosta funktsioon, mis saab parameetriks x-ide massiivi ning liidesele vastava y-koordinaate arvutava klassi ning tagab vastavate y-ite massiivi.
#       Kontrolli klasside ja funktsioonide tööd automaattestidega.
#   Kolmas ülesanne
#       Kuva parameetritele vastav joon ekraanile koos koordinaattelgedega.
#       Kasutaja saab  parameetreid muuta ning vastavalt muutub ka joonis


import unittest
from abc import ABC, abstractmethod
import turtle

# koosta liides või abstraktne klass joone y-i väärtuste leidmiseks vastavalt x-i väärtusele.
class AnnaVastus(ABC):

    @abstractmethod
    def get_y(self, x): # peab tagastama y x järgi
        pass


# koosta realiseeriv klass, millele antakse konstruktoris ette x-i kordaja.
class Y3X(AnnaVastus):

    def __init__(self, kordaja):
        self.kordaja = kordaja

    def get_y(self, x):
        return self.kordaja * x # y = a*x


# koosta automaattestid kontrollimaks, mitu punkti sirgel y = 3x.
class TestAnnaY(unittest.TestCase):

    def setUp(self):
        self.f = Y3X(3)

    def test_y1(self):
        self.assertEqual(self.f.get_y(1), 3)

    def test_y2(self):
        self.assertEqual(self.f.get_y(2), 6)

    def test_y3(self):
        self.assertEqual(self.f.get_y(3), 9)

    def test_y4(self):
        self.assertEqual(self.f.get_y(4), 12)

    def test_negatiivne_y3(self):
        self.assertEqual(self.f.get_y(-3), -9)







#       Loo teine realiseeriv klass, millele saab ette anda kordaja ja vabaliikme.
class KordajaJaVabaliige(AnnaVastus):

    def __init__(self, kordaja, vabaliige):
        self.kordaja = kordaja
        self.vabaliige = vabaliige

    def get_y(self, x):
        return self.kordaja * x + self.vabaliige


#       Koosta funktsioon, mis saab parameetriks x-ide massiivi ning liidesele vastava y-koordinaate arvutava klassi ning tagab vastavate y-ite massiivi.
def arvuta_y_massiiv(x_massiiv, funktsioon):
    return [funktsioon.get_y(x) for x in x_massiiv]


#       Kontrolli selle klassi tööd liidese kaudu testidega joontele y =3x ning y=3x+2.
#       Kontrolli klasside ja funktsioonide tööd automaattestidega.
class TestTeineY(unittest.TestCase):

    def test_y_3x(self):
        # y=3x+0
        f = KordajaJaVabaliige(3, 0)
        self.assertEqual(f.get_y(2), 6)

    def test_y_3x_plus_2(self):
        # y = 3x+2
        f = KordajaJaVabaliige(3, 2)
        self.assertEqual(f.get_y(2), 8)

    def test_massiiv_3x(self):
        f = KordajaJaVabaliige(3, 0)
        self.assertEqual(arvuta_y_massiiv([1, 2, 3], f),[3, 6, 9])

suite = unittest.TestLoader().loadTestsFromTestCase(TestAnnaY)
runner = unittest.TextTestRunner(verbosity=1)
result = runner.run(suite)

print(f"Teste: {result.testsRun}")





sc = turtle.Screen()
trtl = turtle.Turtle()
tousunurk = int(input("sisesta tõusunurk:"))
vabaliige = int(input("sisesta vabaliige:"))

# method to draw y-axis lines
def drawy(val):
    # line
    trtl.forward(300)

    # set position
    trtl.up()
    trtl.setpos(val, 300)
    trtl.down()

    # another line
    trtl.backward(300)

    # set position again
    trtl.up()
    trtl.setpos(val + 10, 0)
    trtl.down()


# method to draw y-axis lines
def drawx(val):
    # line
    trtl.forward(300)

    # set position
    trtl.up()
    trtl.setpos(300, val)
    trtl.down()

    # another line
    trtl.backward(300)

    # set position again
    trtl.up()
    trtl.setpos(0, val + 10)
    trtl.down()


# method to label the graph grid
def lab():
    # set position
    trtl.penup()
    trtl.setpos(155, 155)
    trtl.pendown()

    # write 0
    trtl.write(0, font=("Verdana", 12, "bold"))

    # set position again
    trtl.penup()
    trtl.setpos(290, 155)
    trtl.pendown()

    # write x
    trtl.write("x", font=("Verdana", 12, "bold"))

    # set position again
    trtl.penup()
    trtl.setpos(155, 290)
    trtl.pendown()

    # write y
    trtl.write("y", font=("Verdana", 12, "bold"))


# Main Section
# set screen
sc.setup(800, 800)

# set turtle features
trtl.speed(100)
trtl.left(90)
trtl.color('lightblue')

# y lines
for i in range(30):
    drawy(10 * (i + 1))

# set position for x lines
trtl.right(90)
trtl.up()
trtl.setpos(0, 0)
trtl.down()

# x lines
for i in range(30):
    drawx(10 * (i + 1))

# axis
trtl.color('green')

# set position for x axis
trtl.up()
trtl.setpos(0, 150)
trtl.down()

# x-axis
trtl.forward(300)

# set position for y axis
trtl.left(90)
trtl.up()
trtl.setpos(150, 0)
trtl.down()

# y-axis
trtl.forward(300)
trtl.right(180)
trtl.forward(150)

#siin alustab sirge skitseerimist
trtl.right(180)
trtl.forward(vabaliige)
trtl.left(tousunurk)
trtl.right(90)
trtl.forward(400)
trtl.right(180)
trtl.forward(800)



# labeling
lab()

# hide the turtle
trtl.hideturtle()

turtle.done()