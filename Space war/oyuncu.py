import turtle

turtle.register_shape("oyuncu.gif")
oyuncu = turtle.Turtle()
oyuncu.color("blue")
oyuncu.shape("oyuncu.gif")
oyuncu.penup()
oyuncu.speed(0)
oyuncu.setposition(0,-250)
oyuncu.setheading(90)

#hareket
oyuncuHiz = 10

def solaHareket():
    x = oyuncu.xcor()
    x -= oyuncuHiz
    if x < -280:
        x = 280
    oyuncu.setx(x)

def sagaHareket():
    x = oyuncu.xcor()
    x += oyuncuHiz
    if x > 280:
        x = 280
    oyuncu.setx(x)