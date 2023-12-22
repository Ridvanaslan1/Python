import turtle

cer = turtle.Turtle()
cer.speed(0)
cer.color("white")
cer.penup()
cer.setposition(-300,-300)
cer.pendown()
cer.pensize(3)
for sayi in range(4):
    cer.fd(600)
    cer.lt(90)
cer.hideturtle()