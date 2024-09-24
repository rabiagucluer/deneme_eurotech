#1-100 arasinda sayi tahmini. Sayiyi buldurmak icin fonksiyon yonlendirsin

def guess_number(x):
    tahmin = 0
    #num=None
    #while num!=x
    #break i de silmek lazim.
    #ama bu yöntem pek tercih edilmez
    while True:
        num = int(input("Sayi giriniz:"))
        tahmin += 1
        if x > num:
            print("Sayi daha büyüktür")
        elif x < num:
            print("Sayi daha kücüktür")
        else:
            print(f"Tebrikler bildiniz. Tahmin Sayisiniz:{tahmin}")
            break

guess_number(45)

sayinin_karesi = lambda x: x*x
#kullan at fonk., atamaya gerek yok
sayinin_karesi(12)

my_list=[1,5,3,8,12]

sonuc=map(lambda x: x*x)

sonuc=list(map(sayinin_karesi, my_list))

my_list2=["Isim","Yas","Sehir"]
my_dict={"Isim":"Rabia",
         "Sehir": "Ankara"}

#exception handling
try:
    for i in my_list2:
        print(my_dict[i])
except:
    print("Hata Aldim.")
#try da hata alininca except e gecilir

for i in my_list2:
    try:
        print(my_dict[i])
    except:
        print(f"Hata Aldim.Bu item '{i}' yok. ")

