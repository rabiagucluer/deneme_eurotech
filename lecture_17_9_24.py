################################################
# VERI GÖRSELLESTIRME. MATPLOTLIB & SEABORN
################################################
import numpy as np
##############   MATPLOTLIB   ##################

#low level bir data visulation ve bunun atasidir
#grafik bicimlendirme konusunda diger kütüphanelerin kaynagi niteligindedir
#kategorik degisken: sütun grafigi ile gorsellestirilir. countplot-->seaborn,  matplotlib-->bar
#sayisal degisken: histogram ve boxplot. hist--> dagilim, boxplot--> ayrica aykiri degerleri de gosterir
#python veri gorsellestirme icin pekte uygun degildir. powerbi gibi bi araclari daha uygundur. veri tabanlarina entegra olmus uygulamar

###  Kategorik Degisken Görsellestirme  ###

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)# bu iki satir kod ciktilarin güyel gorunmesi icin düzenlemedir
pd.set_option('display.width',500)

df=sns.load_dataset("titanic")#veri yüklenip cagirildi
df.head()

df["sex"].value_counts().plot(kind = 'bar') #kategorik veride ilk akla gelen fonksiyon--> value_counts
plt.show(block=True)


###  Sayisal Degisken Görsellestirme  ###
plt.hist(df["age"]) #histogram grafigi
plt.show(block=True)

plt.boxplot(df["fare"]) #boxplot grafigi, genel dagilim disinda olan degerleri de isaretler ve gösterir.
plt.show(block=True)              #hangi araliklarda hangi gözlemlerin oldugunu,
                        #hem de veri setinin icindeki degiskenin kendi icindeki dagilim bilgisini,
                        #ve bu dagilimin ne kadar aykiri deger olabilecegini gösterir.

####### MATPLOTLIB Özellikleri  ########
# Farkli katmanlarda bir görsel, title, eksen bilgisi gibi farkli özellikleri göstererek ayni anda cesitli basliklarda calisma imkani saglar.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#### plot özelligi  ####
# veriyi görsellestirmek icin kullanilan fonksiyondur.

x = np.array ([1, 8])
y = np.array ([0, 100])

plt.plot(x, y) # eger görsellestirme kapatilmadan tekrar bir görsellestirme yapilirsa en son yapilan, kapatilmayan grafigin üzerine cizilir.
plt.show(block=True)

x = np.array ([2,4,6, 8,10])
y = np.array ([1,3,5,7,9])

plt.plot(x, y,'o') # o nokta nokta isaretler
plt.show(block=True)

#### marker ####
y=np.array ([13,45,69, 81,107])
plt.plot(y, marker= '*') # markera ne tanimlarsan o sekilde isaretler
plt.show(block=True)           # markers= ['o','v','s','D'...]


#### line ####
plt.plot(y, linestyle= "dashed", color="r") # linestyle=['solid', 'dashed', 'dashdot', 'dotted']
plt.show(block=True)                              # color=['b','g','r','c']

#### Multiple lines ####
x = np.array ([23, 18, 31, 10])
y = np.array ([13, 28, 11, 100])

plt.plot(x)

plt.title(" ")
plt.xlabel("")
plt.ylabel("")






sns.countplot(x=df["sex"],data = df)


x = np.array ([23, 18, 31, 10])
y = np.array ([23, 18, 31, 10])

#plot 2




##############   SEABORN   ##################
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

df=sns.load_dataset("tips")
df.head()

df["sex"].value_counts()
sns.countplot(x=df["sex"],data = df)


