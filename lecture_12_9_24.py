from statsmodels.tsa.stattools import breakvar_heteroskedasticity_test

my_dict={"adı": "Rabia",
         "soyadı":"Köme",
         "sehir":"Gaziantep",
         "yas": 27
}

var=list(my_dict.keys())

#hata aldığında dikkat etmen gereken hata tipine ayrı, hata açıklamasına ayrı bakmak
#hatalarda bi syntax(yazım hataları) vardır bi de diğer hatalar vardır. önce syntax gelir sonra diğer hatalar gelir

my_dict.get("ülke","Not Found")

for key,value in my_dict.items():
    if value==27:
        print(key)

#loop control statements: break, continue

for k,v in my_dict.items():
    if k=='sehir':
        continue
    print(k,v)

#builtin functions
list(range(10,20,3))

list(enumerate(my_list))

for i in enumerate(my_list):
    print(i)

my_int=[1,2,3]
list(zip(my_list,my_int))

#fonksiyonu tanımlarken kullanılan değişken parametredir (place holder:yer kaplayan)
def merhaba (name):
    #print("Hello world!",name)
    print(f"Hello World {name}") #fstring

#argument ise fonksiyonu çağırırken gönderidiğimiz değişkendir. (actual=gerçek)
merhaba("Engin")

def defination(name,age):
    print(f"{name} {age} yaşındadır.")

#positional argumant, yani verilen sıra ile değer gönderme
defination("Faruk",42)

#eğer keyword olarak tanımlarsak yazılan sıranın bir önemi olmadan tanır

def defination_1(name:str,age:int):
    assert type(age)==int, "age has to be integer!"
    print(f"{name} {age} yaşındadır.")

defination_1("Faruk", "42") #hata verir assertion error verir


def  add(a,b):
    c=a+b
    #return None : return yazılmadığında otomatik eklenir arka planda
    return c


add(16,13)*2


