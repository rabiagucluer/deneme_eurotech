a=[1,2,3,9,8,45,5]
b=[8,2,3,56,45,5,10]
c=a-b #
d= (a-b)+(b-a) #

b=set(b)
a=set(a)


a.intersection(b)

a.symmetric_difference(b)

dict_2={'key1':1, 'key2':2}

dict_2["key2"] # key2 yi bastırma
new_dict_2=list(dict_2.values())[1]  # list yöntemi ile bastırma

dict_2.get("key4") # eğer bu key yoksa hata vermesin diye olup olmadığına bakıp alma
dict_2.get("key4","Not Found")  # bu key varsa bana ver yoksa not found yazdır

dict_2={'key1':1,'key2':2, 'key3':3, 'key4':3, 'key5':3}
dict_2.values()
dict_2.keys()
dict_2.items()

for k in dict_2.items():
    #print(k)  # elemanları tupple olarak atar ve bastırır
    if k[1]==3:  #burdaki köşeli parantes list olduğundan değil indexleme olduğundan kullandık.ilk index anlamında
        print(k[0])

my_list=[('key1', 1),('key2',2), ('key3',3), ('key4',3), ('key5',3)]
for key,value in my_list:
    #print(k)
    print(key, value)

for key,value in dict_2.items():
    if value==3 :
        print(value)

#items yaptığımızda dict artık bir tuple şeklinde key value değer çiftleri halinde anlıyor

#unpack error da dict teki verileri ayırma işlemi oluyor ve hata veriyor
for key in dict_2.items():
    #print(dict_2[key])
    if dict_2[2]==3:
        print(key)

for value in dict_2.values():
    #print(dict_2[key])
    if value==3:
        print(dict_2[key])
###unhashable type error konusuna bak!
key
type(key)





