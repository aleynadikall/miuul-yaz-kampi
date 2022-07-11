
# Koşullu Seçim (Conditional Selection)

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

# df[koşul]
df[df["age"] > 50].head()
#     survived  pclass     sex   age  sibsp  parch     fare embarked   class  \
# 6          0       1    male  54.0      0      0  51.8625        S   First
# 11         1       1  female  58.0      0      0  26.5500        S   First
# 15         1       2  female  55.0      0      0  16.0000        S  Second
# 33         0       2    male  66.0      0      0  10.5000        S  Second
# 54         0       1    male  65.0      0      1  61.9792        C   First
#       who  adult_male deck  embark_town alive  alone
# 6     man        True    E  Southampton    no   True
# 11  woman       False    C  Southampton   yes   True
# 15  woman       False  NaN  Southampton   yes   True
# 33    man        True  NaN  Southampton    no   True
# 54    man        True    B    Cherbourg    no  False

# Yaşı 50'den küçük olan kaç kişi var sorusunun cevabını bulalım: count ile saydırıyoruz.
df[df["age"] > 50].count()
# survived       64
# pclass         64
# sex            64
# age            64
# sibsp          64
# parch          64
# fare           64
# embarked       63
# class          64
# who            64
# adult_male     64
# deck           33
# embark_town    63
# alive          64
# alone          64
# dtype: int64

# Yukarıdaki çıktıda bir gariplik var, bazı yerlerde sayılar değişmiş. Bunun sebebi sonuçtan herhangi bir değişken
# seçilmediği için bütün hepsine ekrana yazdırdı. Dolayısıyla bunun sonuna gelir ilgilendiğimiz değişkeni yazarsak
# sonuca ulaşmış olacağız:
df[df["age"] > 50]["age"].count()
# 64

# Yaşı 50'den büyük olan kişilerin buradaki değişkenlerden birisindeki değerini merak ediyoruz, bunu nasıl
# gerçekleştireceğiz?
df.loc[df["age"] > 50, ["age", "class"]].head()
#      age   class
# 6   54.0   First
# 11  58.0   First
# 15  55.0  Second
# 33  66.0  Second
# 54  65.0   First

# Yaşı 50'den büyük olan erkekleri seçmek istiyoruz:
# DİKKAT:
df.loc[df["age"] > 50 df["sex"] == "male", ["age", "class"]].head()
# SyntaxError: invalid syntax

# & operatörünü unutma!
df.loc[df["age"] > 50 & df["sex"] == "male", ["age", "class"]].head()
# TypeError: Cannot perform 'rand_' with a dtyped [object] array and scalar of type [bool]
# DİKKAT: Birden fazla koşul giriliyorsa bu durumda bu birden fazla koşulların parantez içerisine alınması gerekmektedir.

# Doğrusu:
df.loc[(df["age"] > 50) & (df["sex"] == "male"), ["age", "class"]].head()
#      age   class
# 6   54.0   First
# 33  66.0  Second
# 54  65.0   First
# 94  59.0   Third
# 96  71.0   First


df.loc[(df["age"] > 50) & (df["sex"] == "male")
       & (df["embark_town"] == "Cherbourg"),
       ["age", "class", "embark_town"]].head()

#       age  class embark_town
# 54   65.0  First   Cherbourg
# 96   71.0  First   Cherbourg
# 155  51.0  First   Cherbourg
# 174  56.0  First   Cherbourg
# 487  58.0  First   Cherbourg

df["embark_town"].value_counts()
# Southampton    644
# Cherbourg      168
# Queenstown      77
# Name: embark_town, dtype: int64


# & = ve
# | = ya da
df_new = df.loc[(df["age"] > 50) & (df["sex"] == "male")
       & ((df["embark_town"] == "Cherbourg") | (df["embark_town"] == "Southampton")),
       ["age", "class", "embark_town"]]

df_new["embark_town"].value_counts()
# Southampton    35
# Cherbourg       9
# Name: embark_town, dtype: int64