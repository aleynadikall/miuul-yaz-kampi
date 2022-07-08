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

df["age"].head()
df.age.head()

df["age"].head()
type(df["age"].head())


df[["age"]].head()
type(df[["age"]].head())

df[["age", "alive"]]

col_names = ["age", "adult_male", "alive"]
df[col_names]

df["age2"] = df["age"]**2
df["age3"] = df["age"] / df["age2"]

df.drop("age3", axis=1).head()

df.drop(col_names, axis=1).head()

df.loc[:, ~df.columns.str.contains("age")].head()