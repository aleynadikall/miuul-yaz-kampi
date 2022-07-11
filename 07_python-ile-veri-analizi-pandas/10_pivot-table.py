
# Pivot table

# Pivot table groupby işlemlerine benzer şekilde veri setini kırılımlar açısından değerlendirmek ve ilgilendiğimiz özet
# istatistiği bu kırılımlar açısından grme imkanı sağlar.

import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()
#    survived  pclass     sex   age  sibsp  parch     fare embarked  class  \
# 0         0       3    male  22.0      1      0   7.2500        S  Third
# 1         1       1  female  38.0      1      0  71.2833        C  First
# 2         1       3  female  26.0      0      0   7.9250        S  Third
# 3         1       1  female  35.0      1      0  53.1000        S  First
# 4         0       3    male  35.0      0      0   8.0500        S  Third
#      who  adult_male deck  embark_town alive  alone
# 0    man        True  NaN  Southampton    no  False
# 1  woman       False    C    Cherbourg   yes  False
# 2  woman       False  NaN  Southampton   yes   True
# 3  woman       False    C  Southampton   yes  False
# 4    man        True  NaN  Southampton    no   True

# Pivot table der ki benim 1.argümanım values argümanı kesişimlerde neyi görmek istersen onu gir der, survived
# değişkenini görmek istiyorum diyorum. Indexte yani satırda hangi değişkeni görmek istiyorsun der, cinsiyet değişkenini
# görmek istiyorum. Peki sütunda hangi değişkeni görmek istiyorsun der, embark değişkenini görmek istiyorum:

df.pivot_table("survived", "sex", "embarked")
# embarked         C         Q         S
# sex
# female    0.876712  0.750000  0.689655
# male      0.305263  0.073171  0.174603

# survived değişkeninin ön tanımlı olarak ortalamasını alır dilersek değiştirebiliriz.
df.pivot_table("survived", "sex", "embarked", aggfunc="std")
# embarked         C         Q         S
# sex
# female    0.331042  0.439155  0.463778
# male      0.462962  0.263652  0.380058

# daha fazla boyut bilgisi de ekleyebiliriz. Liste olarak yollayabiliriz.
df.pivot_table("survived", "sex", ["embarked", "class"])
# embarked         C                      Q                          S  \
# class        First Second     Third First Second     Third     First
# sex
# female    0.976744    1.0  0.652174   1.0    1.0  0.727273  0.958333
# male      0.404762    0.2  0.232558   0.0    0.0  0.076923  0.354430
# embarked
# class       Second     Third
# sex
# female    0.910448  0.375000
# male      0.154639  0.128302

df.head()
#    survived  pclass     sex   age  sibsp  parch     fare embarked  class  \
# 0         0       3    male  22.0      1      0   7.2500        S  Third
# 1         1       1  female  38.0      1      0  71.2833        C  First
# 2         1       3  female  26.0      0      0   7.9250        S  Third
# 3         1       1  female  35.0      1      0  53.1000        S  First
# 4         0       3    male  35.0      0      0   8.0500        S  Third
#      who  adult_male deck  embark_town alive  alone
# 0    man        True  NaN  Southampton    no  False
# 1  woman       False    C    Cherbourg   yes  False
# 2  woman       False  NaN  Southampton   yes   True
# 3  woman       False    C  Southampton   yes  False
# 4    man        True  NaN  Southampton    no   True

# Ben hem cinsiyet kırılımı istiyorum, hem gemiye binilen lokasyon istiyorum, ya da yaşlara göre bir kırılım istiyorum.
# Fakat sıkıntı şu ki veri setindeki yaş değişkeni sayısal bir değişken. Öyle bir şey yapmak istiyoruz ki çocukların da
# gençler ya da daha olgun kişilerle karşılaştırıldığında hayatta kalma durumlarını analiz edelim.
# Öyle bir işlem yapmalıyız ki bir boyuta yaş değişkenini de ekleyebilelim. Bunu yapmanın yolu da yaş sayısal
# değişkenini kategorik değişkene çevirmektir.
# cut ve qcut fonksiyonları elimizdeki sayısal değişkenleri kategorik değişkene çevirmek için en yaygın kullanılan iki
# ayrı fonksiyondur. Genelde sayısal değişkeni hangi kategorilere bölmek istediğimizi biliyorsak bu durumda cut
# fonksiyonu, eğer elimizdeki sayısal değişkeni tanımıyorsak ve çeyreklik değerlere göre bölünsün istiyorsak qcut
# kullanırız. Örneğin yaş değişkenini kategorik değişkene çevirmek istediğimizde yaş değişkeni adındaki değişkeni
# tanıdığımızdan deriz ki 0 ile 10 arasına çocuk de 10 ile 18 arasına genç de gibi şeyler diyebiliyoruz. Dolayısıyla bu
# sayısal değişkenin kategorik değişkene çevirirken çevirecek olduğumuz sınıfları tanımlayabiliyoruz. Tanımlayamazsak
# qcut fonksiyonunu kullanmamız gerekir ki qcut fonksiyonu otomatik olarak değerkeri küçükten büyüğe sıralar ve yüzdelik
# çeyrek değerlerine göre bunları gruplara böler.
df["new_age"] = pd.cut(df["age"], [0, 10, 18, 25, 40, 90])

df.head()
#    survived  pclass     sex   age  sibsp  parch     fare embarked  class  \
# 0         0       3    male  22.0      1      0   7.2500        S  Third
# 1         1       1  female  38.0      1      0  71.2833        C  First
# 2         1       3  female  26.0      0      0   7.9250        S  Third
# 3         1       1  female  35.0      1      0  53.1000        S  First
# 4         0       3    male  35.0      0      0   8.0500        S  Third
#      who  adult_male deck  embark_town alive  alone   new_age
# 0    man        True  NaN  Southampton    no  False  (18, 25]
# 1  woman       False    C    Cherbourg   yes  False  (25, 40]
# 2  woman       False  NaN  Southampton   yes   True  (25, 40]
# 3  woman       False    C  Southampton   yes  False  (25, 40]
# 4    man        True  NaN  Southampton    no   True  (25, 40]

# Yaş kırılımında da hayatta kalmaları inceleyebilir miyiz sorusunun cevabını araştıralım:
df.pivot_table("survived", "sex", "new_age")
# new_age   (0, 10]  (10, 18]  (18, 25]  (25, 40]  (40, 90]
# sex
# female   0.612903  0.729730  0.759259  0.802198  0.770833
# male     0.575758  0.131579  0.120370  0.220930  0.176471

df.pivot_table("survived", "sex", ["new_age", "class"])
# new_age (0, 10]                   (10, 18]                   (18, 25]  \
# class     First Second     Third     First Second     Third     First
# sex
# female      0.0    1.0  0.500000  1.000000    1.0  0.523810  0.941176
# male        1.0    1.0  0.363636  0.666667    0.0  0.103448  0.333333
# new_age                      (25, 40]                      (40, 90]            \
# class      Second     Third     First    Second     Third     First    Second
# sex
# female   0.933333  0.500000  1.000000  0.906250  0.464286  0.961538  0.846154
# male     0.047619  0.115385  0.513514  0.071429  0.172043  0.280000  0.095238
# new_age
# class       Third
# sex
# female   0.111111
# male     0.064516

# Yukarıdaki çıktı çok karışık oldu bu nedenle bir ayar yapalım:
pd.set_option('display.width', 500)
# new_age   (0, 10]  (10, 18]  (18, 25]  (25, 40]  (40, 90]
# sex
# female   0.612903  0.729730  0.759259  0.802198  0.770833
# male     0.575758  0.131579  0.120370  0.220930  0.176471