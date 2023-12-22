import turtle
import random

turtle.register_shape("dusman.gif")

dusmanSayisi = 30
dusmanlarListe = []

for i in range(dusmanSayisi):
    dusmanlarListe.append(turtle.Turtle())

dusmanX = -200
dusmanY = 250
dusmanNo = 0

for dusman in dusmanlarListe:
    dusman.color("red")
    dusman.shape("dusman.gif")
    dusman.penup()
    dusman.speed(0)
    x = dusmanX + (50 * dusmanNo)
    y = dusmanY
    dusman.setposition(x, y)
    dusmanNo +=1
    if dusmanNo ==10:
        dusmanY -=50
        dusmanNo = 0

