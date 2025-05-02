# To-Do list, yapılacak görevleri ekleyebildiğimiz, silebildiğimiz ta da güncelleyebildiğimiz bir
# yapılacaklar listesidir

task = []
print("Kaç tane yapılacak görev eklemek istiyorsunuz: ", end = "")
num = input()

for i in range(int(num)):
    print("Eklenecek {}. görevi giriniz: ".format(i+1), end = "")
    task.append(input())

print("Eklediğiniz görevleriniz: ")
for j in range(len(task)):
    print("{}-) {}".format(j+1, task[j]))


print("Görev eklemek için 1")
print("Görev silmek için 2")
print("Görevi güncellemek için 3' e tıklayınız")
choose = input("Seçiminiz tuşlayınız: ")

if choose == "1":
    print("Kaç tane yapılacak görev eklemek istiyorsunuz: ", end="")
    num2 = input()

    for k in range(int(num2)):
        print("Eklenecek {}. görevi giriniz: ".format(k + 1), end="")
        task.append(input())
elif choose == "2":
    print("Görevler; ")
    for x in range(len(task)):
        print("{}-) {}".format(x + 1, task[x]))

    delete = input("Silmek istediğiniz görev numarasını giriniz: ")
    task.pop(int(delete)-1)
else:
    for x in range(len(task)):
        print("{}-) {}".format(x + 1, task[x]))
    update = input("Kaç numaralı görevi güncellemek istiyorsunuz: ")
    task[int(update)-1] = input("Yeni görevi girebilirsinniz: ")
#Daha bitmedi fonksiyon biçimine çevrilcek ve eksikler veya eklencekler olabilir