# Pandas'ta Seçim İşlemleri (Selection in Pandas)

import pandas as pd
import seaborn as sns
df = sns.load_dataset("titanic")
df.head()
#    survived  pclass     sex   age  ...  deck  embark_town  alive  alone
# 0         0       3    male  22.0  ...   NaN  Southampton     no  False
# 1         1       1  female  38.0  ...     C    Cherbourg    yes  False
# 2         1       3  female  26.0  ...   NaN  Southampton    yes   True
# 3         1       1  female  35.0  ...     C  Southampton    yes  False
# 4         0       3    male  35.0  ...   NaN  Southampton     no   True
# [5 rows x 15 columns]


# Dış özellikler dediğimiz indekslerden başlayalım:
df.index
# RangeIndex(start=0, stop=891, step=1)

# Slice işlemi yapmak istersek:
df[0:13]
#     survived  pclass     sex   age  ...  deck  embark_town  alive  alone
# 0          0       3    male  22.0  ...   NaN  Southampton     no  False
# 1          1       1  female  38.0  ...     C    Cherbourg    yes  False
# 2          1       3  female  26.0  ...   NaN  Southampton    yes   True
# 3          1       1  female  35.0  ...     C  Southampton    yes  False
# 4          0       3    male  35.0  ...   NaN  Southampton     no   True
# 5          0       3    male   NaN  ...   NaN   Queenstown     no   True
# 6          0       1    male  54.0  ...     E  Southampton     no   True
# 7          0       3    male   2.0  ...   NaN  Southampton     no  False
# 8          1       3  female  27.0  ...   NaN  Southampton    yes  False
# 9          1       2  female  14.0  ...   NaN    Cherbourg    yes  False
# 10         1       3  female   4.0  ...     G  Southampton    yes  False
# 11         1       1  female  58.0  ...     C  Southampton    yes   True
# 12         0       3    male  20.0  ...   NaN  Southampton     no   True
# [13 rows x 15 columns]


# Indexlerde silme işlemi de gerçekleştirebiliriz:
df.drop(0, axis=0).head()
# Silme işlemi satır içinse axis = 0, sütun içinse axis = 1
# Gözlemlemek adına head atıyoruz.
# Atama yapılmadığı için kalıcı değişiklik yapılmadı.

#    survived  pclass     sex   age  ...  deck  embark_town  alive  alone
# 1         1       1  female  38.0  ...     C    Cherbourg    yes  False
# 2         1       3  female  26.0  ...   NaN  Southampton    yes   True
# 3         1       1  female  35.0  ...     C  Southampton    yes  False
# 4         0       3    male  35.0  ...   NaN  Southampton     no   True
# 5         0       3    male   NaN  ...   NaN   Queenstown     no   True
# [5 rows x 15 columns]


# Eğer burada birden fazla index gönderip buna göre silme işlemi yapmak istersek:
delete_indexes = [1, 3, 5, 7]
df.drop(delete_indexes, axis=0).head(10)
#     survived  pclass     sex   age  ...  deck  embark_town  alive  alone
# 0          0       3    male  22.0  ...   NaN  Southampton     no  False
# 2          1       3  female  26.0  ...   NaN  Southampton    yes   True
# 4          0       3    male  35.0  ...   NaN  Southampton     no   True
# 6          0       1    male  54.0  ...     E  Southampton     no   True
# 8          1       3  female  27.0  ...   NaN  Southampton    yes  False
# 9          1       2  female  14.0  ...   NaN    Cherbourg    yes  False
# 10         1       3  female   4.0  ...     G  Southampton    yes  False
# 11         1       1  female  58.0  ...     C  Southampton    yes   True
# 12         0       3    male  20.0  ...   NaN  Southampton     no   True
# 13         0       3    male  39.0  ...   NaN  Southampton     no  False
# [10 rows x 15 columns]

# Yukarıdaki işlem kalıcı değildir, kalıcı yapmak için 2 yol vardır:
# YOL- 1: Atama yaparak: df = df.drop(delete_indexes, axis=0)
# YOL - 2: Inplace argümanı ile atama yapmadan: df.drop(delete_indexes, axis=0, inplace=True)
# DİKKAT: Inplace argumanı çok yaygın bir şekilde kullanılan birçok metodda metod uygulandığında bir değişiklik
# yapıldığında bu değişikliğin kalıcı olması gerektiği bilgisini veren bir argümandır.

# DİKKAT: Birçok senaryoda elimizdeki dataFrame'lerin indexini değişkene ya da değişkeni indexe çevirme ihtiyacı
# olmaktadır. Şimdi bu ihtiyaçları bir değerlendirelim:

# Değişkeni Indexe Çevirmek

# Yaş değişkenini indexe indexteki değeri de bir değişken olarak değişkenler arasına almak isteyelim:

# Değişkeni seçelim:
df["age"].head()    # 1.YOL
df.age.head()       # 2.YOL
# 0    22.0
# 1    38.0
# 2    26.0
# 3    35.0
# 4    35.0
# Name: age, dtype: float64

# Yaş değişkenini indexe atayalım:
df.index = df["age"]
df.index
# Float64Index([22.0, 38.0, 26.0, 35.0, 35.0,  nan, 54.0,  2.0, 27.0, 14.0,
#               ...
#               33.0, 22.0, 28.0, 25.0, 39.0, 27.0, 19.0,  nan, 26.0, 32.0],
#              dtype='float64', name='age', length=891)

# Şimdi de değişken kısmındaki yaş sütununu artık değişkenlerde yaşa ihtiyaç olmadığından silelim:
df.drop("age", axis=1).head()
# Silinme sütunda olacağından axis = 1 yazdık.

#       survived  pclass     sex  sibsp  ...  deck  embark_town alive  alone
# age                                    ...
# 22.0         0       3    male      1  ...   NaN  Southampton    no  False
# 38.0         1       1  female      1  ...     C    Cherbourg   yes  False
# 26.0         1       3  female      0  ...   NaN  Southampton   yes   True
# 35.0         1       1  female      1  ...     C  Southampton   yes  False
# 35.0         0       3    male      0  ...   NaN  Southampton    no   True
# [5 rows x 14 columns]

# Bu değişikliği kalıcı şekilde yapmak için:
df.drop("age", axis=1, inplace=True)
df.head()
#       survived  pclass     sex  sibsp  ...  deck  embark_town alive  alone
# age                                    ...
# 22.0         0       3    male      1  ...   NaN  Southampton    no  False
# 38.0         1       1  female      1  ...     C    Cherbourg   yes  False
# 26.0         1       3  female      0  ...   NaN  Southampton   yes   True
# 35.0         1       1  female      1  ...     C  Southampton   yes  False
# 35.0         0       3    male      0  ...   NaN  Southampton    no   True
# [5 rows x 14 columns]


# Indexi Değişkene Çevirmek

# YOL - 1

# Indexi seçelim:
df.index
# Float64Index([22.0, 38.0, 26.0, 35.0, 35.0,  nan, 54.0,  2.0, 27.0, 14.0,
#               ...
#               33.0, 22.0, 28.0, 25.0, 39.0, 27.0, 19.0,  nan, 26.0, 32.0],
#              dtype='float64', name='age', length=891)

# DİKKAT:
# Eğer köşeli parantez içine girecek olduğumuz string ifade bu DataFrame'de varsa bu durumda bu değişken seçilir, eğer
# girmiş olduğumuz ifade DataFrame içerisinde yoksa bu durumda yeni değişken eklendiği anlaşılır.

df["age"]           # Silindiği için KeyError: 'age' hatası aldık. Bu yüzden yeni değişken eklemiş olacağız.
df["age"] = df.index

df.head()
#       survived  pclass     sex  sibsp  ...  embark_town  alive  alone   age
# age                                    ...
# 22.0         0       3    male      1  ...  Southampton     no  False  22.0
# 38.0         1       1  female      1  ...    Cherbourg    yes  False  38.0
# 26.0         1       3  female      0  ...  Southampton    yes   True  26.0
# 35.0         1       1  female      1  ...  Southampton    yes  False  35.0
# 35.0         0       3    male      0  ...  Southampton     no   True  35.0
# [5 rows x 15 columns]


# YOL - 2

# 2.yolu görebilmek için tekrar silelim:
df.drop("age", axis=1, inplace=True)

# Kısaca bir resetleme işlemi yapmaktır:
df.reset_index().head()
#     age  survived  pclass     sex  ...  deck  embark_town  alive  alone
# 0  22.0         0       3    male  ...   NaN  Southampton     no  False
# 1  38.0         1       1  female  ...     C    Cherbourg    yes  False
# 2  26.0         1       3  female  ...   NaN  Southampton    yes   True
# 3  35.0         1       1  female  ...     C  Southampton    yes  False
# 4  35.0         0       3    male  ...   NaN  Southampton     no   True
# [5 rows x 15 columns]

# Kalıcı hale getirelim:
df = df.reset_index()
df.head()
#     age  survived  pclass     sex  ...  deck  embark_town  alive  alone
# 0  22.0         0       3    male  ...   NaN  Southampton     no  False
# 1  38.0         1       1  female  ...     C    Cherbourg    yes  False
# 2  26.0         1       3  female  ...   NaN  Southampton    yes   True
# 3  35.0         1       1  female  ...     C  Southampton    yes  False
# 4  35.0         0       3    male  ...   NaN  Southampton     no   True
# [5 rows x 15 columns]



