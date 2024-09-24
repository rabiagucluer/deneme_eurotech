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





