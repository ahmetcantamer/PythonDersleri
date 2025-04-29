import random
degerler = ["taş",
            "kağıt",
            "makas"]


while 1:  #Sonsuz döngüye sokar 1 = True demek
    bil_secim = random.choice(degerler)  # degerler arasından rastgele seçim yapar
    print("1- Taş")
    print("2- Kağıt")
    print("3- Makas")
    print("Taş-kağıt-makas oyununa başlamak için lütfen üstteki sayılardan seçim yapınız(çıkmak için Q' ya basınız): ", end="")  # end ifadesi aşağı satıra inmemesini sağlıyor
    secim = input()

    if secim in ["1", "2", "3", "q"]:   #secim == "1" or secim == "2" or secim == "3" or secim == "q":
        if secim == "q":
            print("Çıkış yapılıyor...")
            break

        if bil_secim == "taş" and secim == "2":
            print("Bilgisayaraın seçimi: {}".format("taş"))
            print("Tebrikler Kazandınız")
        elif bil_secim == "kağıt" and secim == "3":
            print("Bilgisayarın seçimi: {}".format("kağıt"))
            print("Tebrikler Kazandınız")
        elif bil_secim == "makas" and secim == "1":
            print("Bilgisayarın seçimi: {}".format("makas"))
            print("Tebrikler Kazandınız")
        elif (bil_secim == "taş" and secim == "1") or (bil_secim == "kağıt" and secim == "2") or (bil_secim == "makas" and secim == "3"):
            print("Bigisayarın seçimi: {}".format(bil_secim))
            print("Berabere kaldınız")

        else:
            print("Bilgisayarın seçimi: {}".format(bil_secim))
            print("Üzgünüm, kaybettiniz tekrar deneyiniz")
    else:
        print("Hatalı giriş yaptınız lütfen tekrar deneyiniz")