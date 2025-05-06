# To-Do list, yapılacak görevleri ekleyebildiğimiz, silebildiğimiz ya da güncelleyebildiğimiz bir
# yapılacaklar listesidir

import time

task = []
print("Kaç tane yapılacak görev eklemek istiyorsunuz: ", end = "")
num = input()

for i in range(int(num)):
    print("Eklenecek {}. görevi giriniz: ".format(i+1), end = "")
    task.append(input())

print("Eklediğiniz görevleriniz: ")
for j in range(len(task)):
    print("{}-) {}".format(j+1, task[j]))


def gorev_ekleme():
    print("Kaç tane yapılacak görev eklemek istiyorsunuz: ", end="")
    num2 = input()

    for k in range(int(num2)):
        print("Eklenecek {}. görevi giriniz: ".format(k + 1), end="")
        task.append(input())
def gorev_silme():
    delete = input("Silmek istediğiniz görev numarasını giriniz: ")
    if int(delete) == len(task):
        task.pop(int(delete) - 1)
    else:
        print("Hatalı tuşlama yaptınız....")
def cikis_yapma():
    print("Çıkış yapılıyor....")
    time.sleep(2)
def gorev_goruntuleme():
    print("Görevler; ")
    for x in range(len(task)):
        print("{}-) {}".format(x + 1, task[x]))
def gorev_guncelleme():
    update = input("Kaç numaralı görevi güncellemek istiyorsunuz: ")
    if int(update) == len(task):
        task[int(update) - 1] = input("Yeni görevi girebilirsinniz: ")
    else:
        print("Hatalı tuşlama yaptınız....")


while True:

    print("Görev eklemek için 1")
    print("Görev silmek için 2")
    print("Görevi güncellemek için 3")
    print("Görevlerinizi görüntülemek için 4")
    print("Çıkış yapmak için 'Q' tıklayınız")
    choose = input("Seçiminiz tuşlayınız: ")


    if choose == "1":
        gorev_ekleme()

    elif choose == "2":
        gorev_silme()

    elif choose == "q":
        cikis_yapma()
        break
    elif choose == "3":
        gorev_guncelleme()
    elif choose == "4":
        gorev_goruntuleme()
    else:
        print("Hatalı giriş yaptınız lütfen tekrar deneyiniz...")