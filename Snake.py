import turtle
import time
import random

delay = 0.1

# Puanları
score = 0
high_score = 0

# Ekran ayarları
wn = turtle.Screen()
wn.title("Yılan Oyunu")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

# Yılan başı
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# Yemek
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# Skor yazısı
pen = turtle.Turtle()
pen.speed(0)
pen.shape("circle")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Puan: 0   En Yüksek Puan: 0", align="center", font=("Courier", 24, "normal"))

# Yılan hareket fonksiyonları
def go_up():
    if head.direction != "Down":
        head.direction = "Up"

def go_down():
    if head.direction != "Up":
        head.direction = "Down"

def go_left():
    if head.direction != "Right":
        head.direction = "Left"

def go_right():
    if head.direction != "Left":
        head.direction = "Right"

def move():
    if head.direction == "Up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "Down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "Left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "Right":
        x = head.xcor()
        head.setx(x + 20)

# Tuş kontrolleri
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Ana oyun döngüsü
while True:
    wn.update()

    # Sınırlar kontrolü
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"

        # Segmentleri temizle
        for segment in segments:
            segment.goto(1000, 1000)

        segments.clear()

        # Skoru sıfırla
        score = 0

        # Gecikmeyi sıfırla
        delay = 0.1

        pen.clear()
        pen.write("Puan: {}   En Yüksek Puan: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Yemek yendiğinde
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Yeni segment oluştur
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Gecikmeyi azalt
        delay -= 0.001

        # Skoru artır
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Puan: {}   En Yüksek Puan: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Segmentlerin hareketi
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Yılanın kendine çarpması kontrolü
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "Stop"

            for segment in segments:
                segment.goto(1000, 1000)

            segments.clear()

            score = 0
            delay = 0.1

            pen.clear()
            pen.write("Puan: {}   En Yüksek Puan: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

turtle.mainloop()

