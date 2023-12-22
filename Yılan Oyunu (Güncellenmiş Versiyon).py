import time
import turtle
import random

hiz = 0.1

# Ekran Ayarları
pencere = turtle.Screen()
pencere.title('Yılan Oyunu')
pencere.bgcolor('lightgreen')
pencere.setup(width=916, height=148)
pencere.tracer(0)

# Yılanın Başı
kafa = turtle.Turtle()
kafa.speed(0)
kafa.shape("square")
kafa.color('black')
kafa.penup()
kafa.goto(0, 100)
kafa.direction = 'stop'

# Yemek
yemek = turtle.Turtle()
yemek.speed(0)
yemek.shape("circle")
yemek.color('red')
yemek.penup()
yemek.goto(0, 0)
yemek.shapesize(1.00, 1.00)

kuyruklar = []
puan = 0

# Skor Yazısı
yaz = turtle.Turtle()
yaz.speed(0)
yaz.shape("square")
yaz.color('black')
yaz.penup()
yaz.goto(0, 260)
yaz.hideturtle()
yaz.write('Score: {}'.format(puan), align='center', font=('Courier', 24, 'normal'))

# Yılanın Hareket Fonksiyonları
def move():
    if kafa.direction == 'up':
        y = kafa.ycor()
        kafa.sety(y + 20)
    if kafa.direction == 'down':
        y = kafa.ycor()
        kafa.sety(y - 20)
    if kafa.direction == 'right':
        x = kafa.xcor()
        kafa.setx(x + 20)
    if kafa.direction == 'left':
        x = kafa.xcor()
        kafa.setx(x - 20)


def goUp():
    if kafa.direction != 'down':
        kafa.direction = 'up'


def goDown():
    if kafa.direction != 'up':
        kafa.direction = 'down'


def goRight():
    if kafa.direction != 'left':
        kafa.direction = 'right'


def goLeft():
    if kafa.direction != 'right':
        kafa.direction = 'left'

# Tuş Kontrolleri
pencere.listen()
pencere.onkey(goUp, 'Up')
pencere.onkey(goDown, 'Down')
pencere.onkey(goRight, 'Right')
pencere.onkey(goLeft, 'Left')

# Ana Oyun Döngüsü
while True:
    pencere.update()

    if kafa.xcor() > 300 or kafa.xcor() < -300 or kafa.ycor() > 300 or kafa.ycor() < -300:
        yaz.clear()
        yaz.write('Game Over !', align='center', font=('Courier', 24, 'normal'))
        time.sleep(1)
        kafa.goto(0, 0)
        kafa.direction = 'stop'

        for kuyruk in kuyruklar:
            kuyruk.goto(1000, 1000)

        kuyruklar = []
        puan = 0
        yaz.clear()
        yaz.write('Score: {}'.format(puan), align='center', font=('Courier', 24, 'normal'))

    # Yemek Yendiğinde
    if kafa.distance(yemek) < 18:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        yemek.goto(x, y)

        puan = puan + 10
        yaz.clear()
        yaz.write('Score: {}'.format(puan), align='center', font=('Courier', 24, 'normal'))

        yeniKuyruk = turtle.Turtle()
        yeniKuyruk.speed(0)
        yeniKuyruk.shape('square')
        yeniKuyruk.color('white')
        yeniKuyruk.penup()
        kuyruklar.append(yeniKuyruk)

    for i in range(len(kuyruklar) - 1, 0, -1):
        x = kuyruklar[i - 1].xcor()
        y = kuyruklar[i - 1].ycor()
        kuyruklar[i].goto(x, y)

    if len(kuyruklar) > 0:
        x = kafa.xcor()
        y = kafa.ycor()
        kuyruklar[0].goto(x, y)

    move()

    for segment in kuyruklar:
        if segment.distance(kafa) < 20:
            time.sleep(1)
            kafa.goto(0, 0)
            kafa.direction = "stop"
            for segment in kuyruklar:
                segment.goto(1000, 1000)
            kuyruklar = []
            puan = 0
            yaz.clear()
            yaz.write('Score: {}'.format(puan), align='center', font=('Courier', 24, 'normal'))
            hiz = 0.1

    time.sleep(hiz)
