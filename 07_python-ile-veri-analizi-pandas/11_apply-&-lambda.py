
# Apply ve Lambda
# apply: satır veya sütunlarda otomatik olarak fonksiyon çalıştırma imkanı sağlar. Yani bir DataFrame'e apply ile
# istediğimiz fonksiyonu uygulayabiliriz.
# lambda: bir fonksiyon tanımlama şeklidir. Tıpkı def gibi, fakat karkı kullan at fonksiyondur. Yani kod akışı esnasında
# bir kere kullanayım atayım dediğimiz noktalarda elimizin gittiği bir fonksiyondur.

import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()
#    survived  pclass     sex   age  sibsp  parch     fare embarked  class    who  adult_male deck  embark_town alive  alone
# 0         0       3    male  22.0      1      0   7.2500        S  Third    man        True  NaN  Southampton    no  False
# 1         1       1  female  38.0      1      0  71.2833        C  First  woman       False    C    Cherbourg   yes  False
# 2         1       3  female  26.0      0      0   7.9250        S  Third  woman       False  NaN  Southampton   yes   True
# 3         1       1  female  35.0      1      0  53.1000        S  First  woman       False    C  Southampton   yes  False
# 4         0       3    male  35.0      0      0   8.0500        S  Third    man        True  NaN  Southampton    no   True


df["age2"] = df["age"]*2

df["age3"] = df["age"]*5

# age2 ve age3 eklenmiş oldu
df.head()
#    survived  pclass     sex   age  sibsp  parch     fare embarked  class    who  adult_male deck  embark_town alive  alone  age2   age3
# 0         0       3    male  22.0      1      0   7.2500        S  Third    man        True  NaN  Southampton    no  False  44.0  110.0
# 1         1       1  female  38.0      1      0  71.2833        C  First  woman       False    C    Cherbourg   yes  False  76.0  190.0
# 2         1       3  female  26.0      0      0   7.9250        S  Third  woman       False  NaN  Southampton   yes   True  52.0  130.0
# 3         1       1  female  35.0      1      0  53.1000        S  First  woman       False    C  Southampton   yes  False  70.0  175.0
# 4         0       3    male  35.0      0      0   8.0500        S  Third    man        True  NaN  Southampton    no   True  70.0  175.0

# Aşağıdaki gibitek tek elimizle kodu yazmamız çok saçma olacaktır.

df["age"]/10.head()
# SyntaxError: invalid syntax

(df["age"]/10).head()
# 0    2.2
# 1    3.8
# 2    2.6
# 3    3.5
# 4    3.5
# Name: age, dtype: float64

(df["age2"]/10).head()
# 0    4.4
# 1    7.6
# 2    5.2
# 3    7.0
# 4    7.0
# Name: age2, dtype: float64

(df["age3"]/10).head()
# 0    11.0
# 1    19.0
# 2    13.0
# 3    17.5
# 4    17.5
# Name: age3, dtype: float64

# Tek tek elimizle yazmak yerine for döngüsü kullanalım:
for col in df.columns:
    if "age" in col:
        print(col)
# age
# age2
# age3
# Döngü çalışıyor mu diye kontrol ettik.

for col in df.columns:
    if "age" in col:
        print((df[col]/10).head())
# 0    2.2
# 1    3.8
# 2    2.6
# 3    3.5
# 4    3.5
# Name: age, dtype: float64
# 0    4.4
# 1    7.6
# 2    5.2
# 3    7.0
# 4    7.0
# Name: age2, dtype: float64
# 0    11.0
# 1    19.0
# 2    13.0
# 3    17.5
# 4    17.5
# Name: age3, dtype: float64

# Değişiklikleri kaydedelim:
for col in df.columns:
    if "age" in col:
        df[col] = df[col]/10

df.head()
#    survived  pclass     sex  age  sibsp  parch     fare embarked  class    who  adult_male deck  embark_town alive  alone  age2  age3
# 0         0       3    male  2.2      1      0   7.2500        S  Third    man        True  NaN  Southampton    no  False   4.4  11.0
# 1         1       1  female  3.8      1      0  71.2833        C  First  woman       False    C    Cherbourg   yes  False   7.6  19.0
# 2         1       3  female  2.6      0      0   7.9250        S  Third  woman       False  NaN  Southampton   yes   True   5.2  13.0
# 3         1       1  female  3.5      1      0  53.1000        S  First  woman       False    C  Southampton   yes  False   7.0  17.5
# 4         0       3    male  3.5      0      0   8.0500        S  Third    man        True  NaN  Southampton    no   True   7.0  17.5

# apply ve lambda kullanarak nasıl yaparız?:
df[["age", "age2", "age3"]].apply(lambda x: x/10).head()
#     age  age2  age3
# 0  0.22  0.44  1.10
# 1  0.38  0.76  1.90
# 2  0.26  0.52  1.30
# 3  0.35  0.70  1.75
# 4  0.35  0.70  1.75

# Daha programatik hali:
df.loc[:, df.columns.str.contains("age")].apply(lambda x: x/10).head()
#     age  age2  age3
# 0  0.22  0.44  1.10
# 1  0.38  0.76  1.90
# 2  0.26  0.52  1.30
# 3  0.35  0.70  1.75
# 4  0.35  0.70  1.75

# Daha karışık ve programatik hali: Standartlaştırma fonksiyonu / değerleri standartlaştıracak
df.loc[:, df.columns.str.contains("age")].apply(lambda x: (x - x.mean()) / x.std()).head()
#         age      age2      age3
# 0 -0.530005 -0.530005 -0.530005
# 1  0.571430  0.571430  0.571430
# 2 -0.254646 -0.254646 -0.254646
# 3  0.364911  0.364911  0.364911
# 4  0.364911  0.364911  0.364911

# normal def ile tanımlanmış bir fonksiyon ile de bunu yapabiliriz:
def standart_scaler(col_name):
    return (col_name - col_name.mean()) / col_name.std()

df.loc[:, df.columns.str.contains("age")].apply(standart_scaler).head()
#         age      age2      age3
# 0 -0.530005 -0.530005 -0.530005
# 1  0.571430  0.571430  0.571430
# 2 -0.254646 -0.254646 -0.254646
# 3  0.364911  0.364911  0.364911
# 4  0.364911  0.364911  0.364911

# Kaydetmek için:
# df.loc[:, ["age","age2","age3"]] = df.loc[:, df.columns.str.contains("age")].apply(standart_scaler)

# Otomatik kaydetmek için:
df.loc[:, df.columns.str.contains("age")] = df.loc[:, df.columns.str.contains("age")].apply(standart_scaler)

df.head()
#    survived  pclass     sex       age  sibsp  parch     fare embarked  class    who  adult_male deck  embark_town alive  alone      age2      age3
# 0         0       3    male -0.530005      1      0   7.2500        S  Third    man        True  NaN  Southampton    no  False -0.530005 -0.530005
# 1         1       1  female  0.571430      1      0  71.2833        C  First  woman       False    C    Cherbourg   yes  False  0.571430  0.571430
# 2         1       3  female -0.254646      0      0   7.9250        S  Third  woman       False  NaN  Southampton   yes   True -0.254646 -0.254646
# 3         1       1  female  0.364911      1      0  53.1000        S  First  woman       False    C  Southampton   yes  False  0.364911  0.364911
# 4         0       3    male  0.364911      0      0   8.0500        S  Third    man        True  NaN  Southampton    no   True  0.364911  0.364911





