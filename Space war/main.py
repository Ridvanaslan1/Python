import ekran
import cerceve
import oyuncu
import turtle
import dusmanlar
import mermiler
import random
import skorlar
import winsound

dusmanHiz = .2
mermiHiz = 5
vurulanSayi = 0
ekran.ekr.tracer(0)


ekran.ekr.listen()
ekran.ekr.onkeypress(oyuncu.solaHareket,"Left")
ekran.ekr.onkeypress(oyuncu.sagaHareket,"Right")
ekran.ekr.onkeypress(mermiler.mermiAtesle,"space")

while True:
    ekran.ekr.update()
    for dusman in dusmanlar.dusmanlarListe:
        x = dusman.xcor()
        x +=dusmanHiz
        dusman.setx(x)

        if dusman.xcor() > 280:
            for d in dusmanlar.dusmanlarListe:
                y = d.ycor()
                y -= 40
                d.sety(y)
            dusmanHiz *= -1

        if dusman.xcor() < -280:
            for d in dusmanlar.dusmanlarListe:
                y = d.ycor()
                y -= 40
                d.sety(y)
            dusmanHiz *= -1
        #vuruş kontrol
        if mermiler.dusmanaDegdimi(mermiler.mermi, dusman):
            mermiler.mermi.hideturtle()
            mermiler.mermiDurum = "hazir"
            mermiler.mermi.setposition(0, -400)
            dusman.setposition(0, 1000000000000)
            winsound.PlaySound("patlama.wav", winsound.SND_ASYNC)
            vurulanSayi +=1
            if vurulanSayi == dusmanlar.dusmanSayisi:
                winsound.PlaySound("alkis.wav", winsound.SND_ASYNC)
                oyuncu.oyuncu.hideturtle()
                ekran.ekr.bgpic("bitti.png")
            #skor
            skorlar.skor += 10
            skorlar.skorCiz.clear()
            skorMetin = "Skor: %s" % skorlar.skor
            skorlar.skorCiz.write(skorMetin, False, align="left", font=("Arial", 21, "normal"))

        if mermiler.dusmanaDegdimi(oyuncu.oyuncu,dusman):
            winsound.PlaySound("patlama.wav", winsound.SND_ASYNC)
            oyuncu.oyuncu.hideturtle()
            dusman.hideturtle()
            print("Oyun Bitti")
            break


    # mermi
    if mermiler.mermiDurum == "ates":
        y = mermiler.mermi.ycor()
        y += mermiHiz
        mermiler.mermi.sety(y)

    if mermiler.mermi.ycor() > 275:
        mermiler.mermi.hideturtle()
        mermiler.mermiDurum = "hazir"






