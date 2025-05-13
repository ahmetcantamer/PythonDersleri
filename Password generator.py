#Parola oluşturucu örneğinde kullanıcıdan bir parola uzunluk alıcaz ve bu parolanın içinde büyük ve küçük harfler, sayılar ve semboller içericek

import random

def password_generator():
        sifre = ""
        while True:
                print("Oluşturmak istediğiniz parolanızın uzunluğunu giriniz: ", end="")
                try:
                        pass_len = int(input())
                        break
                except:
                        print("Lütfen sayı formatında bir değer giriniz...")

        if pass_len >= 12:
                statment = "Şifre uzunluğu iyi"
        elif 7 <= pass_len < 12:
                statment = "Orta güvenlikte şifre uzunluğu"
        else:
                statment = "Güvensiz şifre uzunluğu"


        words = ["qwertyuıopğüasdfghjklşizxcvbnmöç", "QWERTYUIOPĞÜASDFGHJKLŞİZXCVBNMÖÇ", "0123456789", ".,!'^+%&/()=?_£#${[]}\|*-"]

        for i in range(pass_len):

                sifre += random.choice(words[i%4])

        return statment, sifre

statment, sifre = password_generator()
print("Şifreniz: {} ve {}".format(sifre, statment))