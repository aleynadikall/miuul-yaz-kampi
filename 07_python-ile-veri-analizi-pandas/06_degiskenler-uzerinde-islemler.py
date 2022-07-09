# Değişkenler Üzerinde İşlemler

import pandas as pd
import seaborn as sns

# Çıktılardaki veri setindeki üç noktalardan kurtulmak için yapılan ayar
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

# Bir DataFrame'de herhangi bir değişkenin varlığını sorgulamak için:
"age" in df
# True

# Seçim işleminin 2 yolu vardı:
df["age"].head()
# 0    22.0
# 1    38.0
# 2    26.0
# 3    35.0
# 4    35.0
# Name: age, dtype: float64

df.age.head()
# 0    22.0
# 1    38.0
# 2    26.0
# 3    35.0
# 4    35.0
# Name: age, dtype: float64

# DİKKAT:
df["age"].head()
type(df["age"].head())
# pandas.core.series.Series

df[["age"]].head()
type(df[["age"]].head())
# pandas.core.frame.DataFrame

# Bir DataFrame içerisinden birden fazla deişken seçmek istersek:
df[["age", "alive"]]
#       age alive
# 0    22.0    no
# 1    38.0   yes
# 2    26.0   yes
# 3    35.0   yes
# 4    35.0    no
# ..    ...   ...
# 886  27.0    no
# 887  19.0   yes
# 888   NaN    no
# 889  26.0   yes
# 890  32.0    no
# [891 rows x 2 columns]


# Liste ile değişken isimlerini gönderebiliriz:
col_names = ["age", "adult_male", "alive"]
df[col_names]
#       age  adult_male alive
# 0    22.0        True    no
# 1    38.0       False   yes
# 2    26.0       False   yes
# 3    35.0       False   yes
# 4    35.0        True    no
# ..    ...         ...   ...
# 886  27.0        True    no
# 887  19.0       False   yes
# 888   NaN       False    no
# 889  26.0        True   yes
# 890  32.0        True    no
# [891 rows x 3 columns]

# DataFrame'e yeni bir değişken ekleme:
df["age2"] = df["age"]**2
df.head()
#    survived  pclass     sex   age  ...  alive  alone    age2      age3
# 0         0       3    male  22.0  ...     no  False   484.0  0.045455
# 1         1       1  female  38.0  ...    yes  False  1444.0  0.026316
# 2         1       3  female  26.0  ...    yes   True   676.0  0.038462
# 3         1       1  female  35.0  ...    yes  False  1225.0  0.028571
# 4         0       3    male  35.0  ...     no   True  1225.0  0.028571
# [5 rows x 17 columns]

df["age3"] = df["age"] / df["age2"]
df.head()
#    survived  pclass     sex   age  ...  alive  alone    age2      age3
# 0         0       3    male  22.0  ...     no  False   484.0  0.045455
# 1         1       1  female  38.0  ...    yes  False  1444.0  0.026316
# 2         1       3  female  26.0  ...    yes   True   676.0  0.038462
# 3         1       1  female  35.0  ...    yes  False  1225.0  0.028571
# 4         0       3    male  35.0  ...     no   True  1225.0  0.028571
# [5 rows x 17 columns]


# Bir değişkeni silmek istersek:
df.drop("age3", axis=1).head()
#    survived  pclass     sex   age  sibsp  ...  deck  embark_town alive  alone    age2
# 0         0       3    male  22.0      1  ...   NaN  Southampton    no  False   484.0
# 1         1       1  female  38.0      1  ...     C    Cherbourg   yes  False  1444.0
# 2         1       3  female  26.0      0  ...   NaN  Southampton   yes   True   676.0
# 3         1       1  female  35.0      1  ...     C  Southampton   yes  False  1225.0
# 4         0       3    male  35.0      0  ...   NaN  Southampton    no   True  1225.0
# [5 rows x 16 columns]

# Birden fazla sütun silmek istiyorsak:
df.drop(col_names, axis=1).head()
#    survived  pclass     sex  sibsp  ...  embark_town  alone    age2      age3
# 0         0       3    male      1  ...  Southampton  False   484.0  0.045455
# 1         1       1  female      1  ...    Cherbourg  False  1444.0  0.026316
# 2         1       3  female      0  ...  Southampton   True   676.0  0.038462
# 3         1       1  female      1  ...  Southampton  False  1225.0  0.028571
# 4         0       3    male      0  ...  Southampton   True  1225.0  0.028571
# [5 rows x 14 columns]

# DİKKAT:
# Diyelim ki veri setinde belirli bir string ifadeyi barındıran değişkenleri silmek istiyoruz:
df.loc[:, df.columns.str.contains("age")].head()
#     age    age2      age3
# 0  22.0   484.0  0.045455
# 1  38.0  1444.0  0.026316
# 2  26.0   676.0  0.038462
# 3  35.0  1225.0  0.028571
# 4  35.0  1225.0  0.028571

# Değildir demenin yolu başa ~ eklemektir.
df.loc[:, ~df.columns.str.contains("age")].head()
#    survived  pclass     sex  sibsp  ...  deck  embark_town alive  alone
# 0         0       3    male      1  ...   NaN  Southampton    no  False
# 1         1       1  female      1  ...     C    Cherbourg   yes  False
# 2         1       3  female      0  ...   NaN  Southampton   yes   True
# 3         1       1  female      1  ...     C  Southampton   yes  False
# 4         0       3    male      0  ...   NaN  Southampton    no   True
# [5 rows x 14 columns]

# contains metodu stringlere uygulanan bir metoddur. Bize der ki bana bir string ifade ver ben benden önceki stringde
# bu var mı yok mu bunu arayayım.

