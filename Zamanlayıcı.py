import time

while True:
    try:
        minute = int(input("Geri sayımı başlatmak için dakika giriniz: "))
        second = int(input("Saniye giriniz: "))
        break


    except ValueError:
        print("Lütfen geçerli bir sayı giriniz")


while 1:
    print("{} : {:02}".format(minute, second))  # {:02} kısmı saniyeyi iki basamaklı göstermek için yazıldı

    if minute == 0 and second == 0:
        break
    if second == 0:
        minute -= 1
        second = 60

    second -= 1
    time.sleep(1)  # 1 saniye gecikme oluşturmak için yazıldı