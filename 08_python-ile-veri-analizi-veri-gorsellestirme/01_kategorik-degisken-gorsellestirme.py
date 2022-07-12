
# VERİ GÖRSELLEŞTİRME: MATPLOTLIB & SEABORN

# MATPLOTLIB: Python'daki veri görselleştirme araçlarının atasıdır. low level bir veri görselleştirme aracıdır.
# Seaborn'a kıyasla daha fazla çabayla veri görselleştirme yapmak gerekmektedir. Özlellikle grafik biçimlendirme
# noktalarında diğer kütüphaneye mathplot library'nin katkısı vardır.
# DİKKAT: Veri görselleştirme konusu derya denizdir fakat yine gkontrollü bir açılmayla ihtiyaçlarımızı görebileceğimiz
# şekilde bu veri görselleştirme araçlarına hakim olmak önemlidir. Burada genellikle veri görselleştirme ile karşı
# karşıya kalan kullanıcıların içinden çıkamadığı bir durum vardır: Hangi değişkeni hangi veriyi nasıl görselleştiririm?
# Eğer elimizde kategorik bir değişken varsa bunu sütun grafikle görselleştiririz. Bunu da seaborn içerisindeki
# countplot veya matplot içerisindeki barplot ile gerçekleştirebiliriz. Elimizdeki değişken sayısal bir değişkense bu
# durumda histogram ve boxplot kullanılabilir.
# DİKKAT: Python verş görselleştirme için en uygun yer midir?
# Değildir. Veri tabanına bağlı olan bir görselleştirme aracı ya da bir iş zekası aracı bunun için daha uygundur.
# powerbi, tablo, clickview gibi bazı araçlar, yani bunların da yaygın özelliği veritabanı üzerine kurulu olmasıdır.
# Veri tabanıyla direkt konuşabiliyor olmasıdır. Dolayısıyla bu araçlar veriye daha yakın kaynaklarda
# konumlandırılabileceğinden dolayı veri görselleştirme asıl işinin olması gereken yer bi araçlarıdır.


# KISACA:
# Kategorik değişken: sütun grafik. countplot bar
# Sayısal değişken: hist, boxplot


#############################################
# Kategorik Değişken Görselleştirme
#############################################
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)             # alt alta değil de yan yana yazılsın diye
df = sns.load_dataset("titanic")
df.head()
#   survived  pclass     sex   age  sibsp  parch     fare embarked  class    who  adult_male deck  embark_town alive  alone
# 0         0       3    male  22.0      1      0   7.2500        S  Third    man        True  NaN  Southampton    no  False
# 1         1       1  female  38.0      1      0  71.2833        C  First  woman       False    C    Cherbourg   yes  False
# 2         1       3  female  26.0      0      0   7.9250        S  Third  woman       False  NaN  Southampton   yes   True
# 3         1       1  female  35.0      1      0  53.1000        S  First  woman       False    C  Southampton   yes  False
# 4         0       3    male  35.0      0      0   8.0500        S  Third    man        True  NaN  Southampton    no   True


df['sex'].value_counts().plot(kind='bar')
plt.show()
![](../../Screenshot_1.png)