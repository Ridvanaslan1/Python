print("VİCUT KİTLE ENDEKSİNİ HESAPLAYAN PROGRAM")

kilo=int(input("KİLONUZU GİRİNİZ"))
boy=float(input("BOYUNUZU GİRİNİZ"))

sonuc=kilo/(boy**2)
round(sonuc)
if sonuc<20:
    print("ZAYIFSINIZ")
elif sonuc>21 and sonuc<30:
    print(sonuc, "NORMAL KİLODASINIZ")
else:
    print(sonuc, "KİLONUZA DİKKAT ETMELİSİNİZ")
