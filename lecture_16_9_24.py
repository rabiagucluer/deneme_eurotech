x=None
print(x)
print(type(x))

#pair programming?

def sum(a,b):
    return a+b

sum(7,8)

#function assigned to a variable
#fonksiyonu baska bir degiskene atandi
#x=sum
#x(5,10)

x=sum(7,58)
#modularity: bazi veri tiplerin kendine has methodlari vardir. bu modularity calisma sistemine ornektir

#return
def sum(a,b):
    return a+b
    print("Hello World") #return fonksiyonun exitidir. o nedenle returndan sonra yazilan satirlar calismaz yani dead code´dur

sum(5,23)

def my_function(int1):
    if int1 > 0:
        return"pozitif"
    elif int1 < 0:
        return "negatiftir"
    else:
        return "sayi sifirdir"

my_function(-2)

def my_function(int1):
    if int1 > 0:
        return"pozitif"
    elif int1 < 0:
        return "negatiftir"
    return "sayi sifirdir" #bu da calisir cünkü else mantigindadir en son yazilan return.


def my_function(int1):
    if int1 > 0:
        output="pozitif"
    elif int1 < 0:
        output= "negatiftir"
    else:
        output= "sayi sifirdir"
    return output

my_function(5-8)

#fonksiyonda sadece bir deger döndürmene gerek yok. birden fazla deger döndürebilirsin

def sum_and_subst(x,y):
    return x+y , x-y

t,c=sum_and_subst(10,11) #tupple da toplanan return sonuclarini burda unpack ettik
#fonksiyonlara daha cok atomik islemler yaptirilir. bu da hatalari kolay bulmak icindir
