import turtle

# Grafik penceresini oluştur
window = turtle.Screen()
window.bgcolor("white")

# Turtle nesnesini oluştur
t = turtle.Turtle()
t.shape("turtle")
t.color("black")
t.speed(0)  # En yüksek hız

# Görsel ve çizgi kalınlığını büyütme
t.shapesize(2, 2, 2)  # Genişlik, uzunluk ve kalınlığı 2 katına çıkar
t.width(3)  # Çizgi kalınlığını 3 birim yap

# 360 derece dönme fonksiyonu
def rotate_360():
    for _ in range(360):
        t.forward(1)
        t.right(1)

# Döngü içinde dönme işlemini çağır
while True:
    rotate_360()
