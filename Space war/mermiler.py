import turtle
import oyuncu
import math
import winsound

mermi = turtle.Turtle()
mermi.color("yellow")
mermi.shape("triangle")
mermi.penup()
mermi.speed(0)
mermi.setheading(90)
mermi.shapesize(0.5,0.5)
mermi.hideturtle()
mermiDurum = "hazir"

def mermiAtesle():
    global mermiDurum
    if mermiDurum == "hazir":
        mermiDurum = "ates"
        x = oyuncu.oyuncu.xcor()
        y = oyuncu.oyuncu.ycor() +  10
        mermi.setposition(x,y)
        mermi.showturtle()
        winsound.PlaySound("laser.wav", winsound.SND_ASYNC)


def dusmanaDegdimi(t1,t2):
    uzaklik = math.sqrt(math.pow(t1.xcor() - t2.xcor() , 2) + math.pow(t1.ycor() - t2.ycor() , 2))
    if uzaklik < 15:
        return True
    else:
        return False