
# Toplulaştırma ve Gruplama (Aggregation & Grouping)
# Toplulaştırma: Bir veri yapısının içinde barınan değerleri toplu bir şekilde temsil etmek demektir.

# Toplulaştırma metodları:
# - count()
# - first()
# - last()
# - mean()
# - median()
# - min()
# - max()
# - std()
# - var()
# - sum()
# - pivot table
# pivot table hariç groupby ile kullanılabilir.

# Toplulaştırma ve gruplama birlikte kullanılır.
# Toplulaştırma bize özet istatistikler veren fonksiyonlardır.

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

# Yaşın ortalamasına erişmek için:
df["age"].mean()
# 29.69911764705882

# Cinsiyete göre yaşın ortalaması:
df.groupby("sex")["age"].mean()
# sex
# female    27.915709
# male      30.726645
# Name: age, dtype: float64

# Sadece ortalama değil toplamını da almak istiyorsak:
# Bu kullanım yukarıdakine göre daha doğrudur.
df.groupby("sex").agg({"age": "mean"})
#               age
# sex
# female  27.915709
# male    30.726645


df.groupby("sex").agg({"age": ["mean", "sum"]})
#               age
#              mean       sum
# sex
# female  27.915709   7286.00
# male    30.726645  13919.17

# Cinsiyete göre kırdıktan sonra gemiye biniş limanını ifade eden embark_town ile ilgili de frekans bilgisi istiyoruz.
# Neden pivot table fonksiyonuna ihtiyacımız var sorusunun yanıtı: Bize verdiği şey embark'ın frekansları değil
# cinsiyetin frekansı oldu. Yani anlıyorum ki groupby'a aldıktan sonra burada sayısal bir değişken girsek sanki daha
# mantıklı bir sonuç gelecekti.
df.groupby("sex").agg({"age": ["mean", "sum"],
                       "embark_town": "count"})
#               age           embark_town
#              mean       sum       count
# sex
# female  27.915709   7286.00         312
# male    30.726645  13919.17         577

# Sayısal değişken ile:
df.groupby("sex").agg({"age": ["mean", "sum"],
                       "survived": "mean"})
#               age            survived
#              mean       sum      mean
# sex
# female  27.915709   7286.00  0.742038
# male    30.726645  13919.17  0.188908

# Sadece cinsiyete göre değil diğer bazı kategorik değişkenlere göre de bir kırılım yapalım:
# kategorik değişkenleri liste şeklinde gönderdik, aggregation kısmındakileri ise sözlük şeklinde...
df.groupby(["sex", "embark_town"]).agg({"age": ["mean"],
                       "survived": "mean"})
#                           age  survived
#                          mean      mean
# sex    embark_town
# female Cherbourg    28.344262  0.876712
#        Queenstown   24.291667  0.750000
#        Southampton  27.771505  0.689655
# male   Cherbourg    32.998841  0.305263
#        Queenstown   30.937500  0.073171
#        Southampton  30.291440  0.174603

# class bilgisini de bir boyut olarak eklemek istiyoruz:
df.groupby(["sex", "embark_town", "class"]).agg({"age": ["mean"],
                       "survived": "mean"})
#                                  age  survived
#                                 mean      mean
# sex    embark_town class
# female Cherbourg   First   36.052632  0.976744
#                    Second  19.142857  1.000000
#                    Third   14.062500  0.652174
#        Queenstown  First   33.000000  1.000000
#                    Second  30.000000  1.000000
#                    Third   22.850000  0.727273
#        Southampton First   32.704545  0.958333
#                    Second  29.719697  0.910448
#                    Third   23.223684  0.375000
# male   Cherbourg   First   40.111111  0.404762
#                    Second  25.937500  0.200000
#                    Third   25.016800  0.232558
#        Queenstown  First   44.000000  0.000000
#                    Second  57.000000  0.000000
#                    Third   28.142857  0.076923
#        Southampton First   41.897188  0.354430
#                    Second  30.875889  0.154639
#                    Third   26.574766  0.128302

# DİKKAT: Şu anda 3 kırılımda gemiye binen yolcuların yaş ve hayatta kalma durumlarını değerlendirebiliyoruz.
# Cinsiyeti kadın olan Queenstown konumundan gemiye binen 3.sınıf yolcuların %72'si hayatta kalmış, erkeklerin
# Southhampton lokasyonundan gemiye binen 3.sınıf yolcuların %12'si ancak hayatta kalabilmiş. Daha kötü sonuçlar da var.
# DİKKAT:
# Queenstown  First   44.000000  0.000000
#             Second  57.000000  0.000000
# kısmında frekans bilgisi elimizde yok. Yani şu anlama geliyor hiç kimse olmayabilir veya bir kişi vardır o da hayatta
# kalamamıştır. Dolayısıyla ortalaması sıfır olmuştur.

# Frekans bilgilerini de getirelim: Bunu cinsiyet değişkeninin saydırılması ile yapabiliriz.
df.groupby(["sex", "embark_town", "class"]).agg({
    "age": ["mean"],
    "survived": "mean",
    "sex": "count"})
#                                  age  survived   sex
#                                 mean      mean count
# sex    embark_town class
# female Cherbourg   First   36.052632  0.976744    43
#                    Second  19.142857  1.000000     7
#                    Third   14.062500  0.652174    23
#        Queenstown  First   33.000000  1.000000     1
#                    Second  30.000000  1.000000     2
#                    Third   22.850000  0.727273    33
#        Southampton First   32.704545  0.958333    48
#                    Second  29.719697  0.910448    67
#                    Third   23.223684  0.375000    88
# male   Cherbourg   First   40.111111  0.404762    42
#                    Second  25.937500  0.200000    10
#                    Third   25.016800  0.232558    43
#        Queenstown  First   44.000000  0.000000     1
#                    Second  57.000000  0.000000     1
#                    Third   28.142857  0.076923    39
#        Southampton First   41.897188  0.354430    79
#                    Second  30.875889  0.154639    97
#                    Third   26.574766  0.128302   265

# Kadınların Cherburg lokasyonundan çıkan 1.sınıf yolcularının yaş ortalaması 36'dır, hayatta kalma oranı %97'dir ve bu
# grup tam 43 kişidir.
# Queenstown lokasyonunda 1. ve 2.sınıf birer yolcu vardır ve hayatta kalma yüzdeleri 0'dır.





