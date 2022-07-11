
# iloc & loc

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


# iloc: integer based selection
df.iloc[0:3]
#    survived  pclass     sex   age  sibsp  parch     fare embarked  class  \
# 0         0       3    male  22.0      1      0   7.2500        S  Third
# 1         1       1  female  38.0      1      0  71.2833        C  First
# 2         1       3  female  26.0      0      0   7.9250        S  Third
#      who  adult_male deck  embark_town alive  alone
# 0    man        True  NaN  Southampton    no  False
# 1  woman       False    C    Cherbourg   yes  False
# 2  woman       False  NaN  Southampton   yes   True


df.iloc[0, 0]       # 0

# loc: label based selection : Mutlak olarak isimlendirmenin kendisini seçer.
df.loc[0:3]
#    survived  pclass     sex   age  sibsp  parch     fare embarked  class  \
# 0         0       3    male  22.0      1      0   7.2500        S  Third
# 1         1       1  female  38.0      1      0  71.2833        C  First
# 2         1       3  female  26.0      0      0   7.9250        S  Third
# 3         1       1  female  35.0      1      0  53.1000        S  First
#      who  adult_male deck  embark_town alive  alone
# 0    man        True  NaN  Southampton    no  False
# 1  woman       False    C    Cherbourg   yes  False
# 2  woman       False  NaN  Southampton   yes   True
# 3  woman       False    C  Southampton   yes  False

df.iloc[0:3, 0:3]
#    survived  pclass     sex
# 0         0       3    male
# 1         1       1  female
# 2         1       3  female

df.iloc[0:3, "age"]
# ValueError: Location based indexing can only have [integer, integer slice (START point is INCLUDED, END point is
# EXCLUDED), listlike of integers, boolean array] types

df.loc[0:3, "age"]
# 0    22.0
# 1    38.0
# 2    26.0
# 3    35.0
# Name: age, dtype: float64

# Fancy Index
col_names = ["age", "embarked", "alive"]
df.loc[0:3, col_names]
#     age embarked alive
# 0  22.0        S    no
# 1  38.0        C   yes
# 2  26.0        S   yes
# 3  35.0        S   yes
