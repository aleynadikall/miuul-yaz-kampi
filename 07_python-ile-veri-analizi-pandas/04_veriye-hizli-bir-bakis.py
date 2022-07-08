# Veriye Hızlı Bir Bakış (Quick Look at Data)

import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")

# Verinin ilk 5 gözlemine hızlı bir şekilde göz atmak için:
df.head()
#    survived  pclass     sex   age  ...  deck  embark_town  alive  alone
# 0         0       3    male  22.0  ...   NaN  Southampton     no  False
# 1         1       1  female  38.0  ...     C    Cherbourg    yes  False
# 2         1       3  female  26.0  ...   NaN  Southampton    yes   True
# 3         1       1  female  35.0  ...     C  Southampton    yes  False
# 4         0       3    male  35.0  ...   NaN  Southampton     no   True
# [5 rows x 15 columns]

# Verinin son 5 gözlemine hızlı bir şekilde göz atmak için:
df.tail()
#      survived  pclass     sex   age  ...  deck  embark_town  alive  alone
# 886         0       2    male  27.0  ...   NaN  Southampton     no   True
# 887         1       1  female  19.0  ...     B  Southampton    yes   True
# 888         0       3  female   NaN  ...   NaN  Southampton     no  False
# 889         1       1    male  26.0  ...     C    Cherbourg    yes   True
# 890         0       3    male  32.0  ...   NaN   Queenstown     no   True
# [5 rows x 15 columns]


# DataFarame'mimizin boyut bilgisini almak için:
df.shape
# (891, 15)


# Biraz daha detaylı bilgi için (Değişkenler, bu değişkenlerin tipleri bilgileri gibi):
df.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 891 entries, 0 to 890
# Data columns (total 15 columns):
#  #   Column       Non-Null Count  Dtype
# ---  ------       --------------  -----
#  0   survived     891 non-null    int64
#  1   pclass       891 non-null    int64
#  2   sex          891 non-null    object
#  3   age          714 non-null    float64
#  4   sibsp        891 non-null    int64
#  5   parch        891 non-null    int64
#  6   fare         891 non-null    float64
#  7   embarked     889 non-null    object
#  8   class        891 non-null    category
#  9   who          891 non-null    object
#  10  adult_male   891 non-null    bool
#  11  deck         203 non-null    category
#  12  embark_town  889 non-null    object
#  13  alive        891 non-null    object
#  14  alone        891 non-null    bool
# dtypes: bool(2), category(2), float64(2), int64(4), object(5)
# memory usage: 80.7+ KB


# Bu DataFrame'in değişkenlerinin isimlerine erişmek için:
df.columns
# Index(['survived', 'pclass', 'sex', 'age', 'sibsp', 'parch', 'fare',
#        'embarked', 'class', 'who', 'adult_male', 'deck', 'embark_town',
#        'alive', 'alone'],
#       dtype='object')


# Eğer index bilgisine erişmek istersek:
df.index
# RangeIndex(start=0, stop=891, step=1)


# Elimizdeki DataFrame'in eğer hızlı bir şekilde özet istatistiklerine erişmek istersek:
df.describe().T             # Transpozunu alarak daha okunaklı hale getirdik.
#           count       mean        std   min      25%      50%   75%       max
# survived  891.0   0.383838   0.486592  0.00   0.0000   0.0000   1.0    1.0000
# pclass    891.0   2.308642   0.836071  1.00   2.0000   3.0000   3.0    3.0000
# age       714.0  29.699118  14.526497  0.42  20.1250  28.0000  38.0   80.0000
# sibsp     891.0   0.523008   1.102743  0.00   0.0000   0.0000   1.0    8.0000
# parch     891.0   0.381594   0.806057  0.00   0.0000   0.0000   0.0    6.0000
# fare      891.0  32.204208  49.693429  0.00   7.9104  14.4542  31.0  512.3292


# Detaylarına girmeden sadece veri setinde herhangi bir eksiklik var mı araştırmak için:
df.isnull().values.any()
# True

df.isnull().values
# values kullandığımız için numpy array'e dönüştüğünü unutmayalım.

# array([[False, False, False, ..., False, False, False],
#        [False, False, False, ..., False, False, False],
#        [False, False, False, ..., False, False, False],
#        ...,
#        [False, False, False, ..., False, False, False],
#        [False, False, False, ..., False, False, False],
#        [False, False, False, ..., False, False, False]])


# Veri setindeki değişkenlerdeki eksiklik durumunun incelenmesi için:
df.isnull().sum()
# survived         0
# pclass           0
# sex              0
# age            177
# sibsp            0
# parch            0
# fare             0
# embarked         2
# class            0
# who              0
# adult_male       0
# deck           688
# embark_town      2
# alive            0
# alone            0
# dtype: int64

# DİKKAT: Elimizdeki True False array'ine sum veya mean atarsak true falseları sırasıylla 1 ve 0 olarak sayacaktır.


# Kategorik değişken içerisinde kaç tane sınıf olduğu ve bu sınıfların kaçar tane olduğu bilgisine erişmek için:

# Hatırlatma:
df["sex"].head()
# 0      male
# 1    female
# 2    female
# 3    female
# 4      male
# Name: sex, dtype: object

# Asıl amacımız:
df["sex"].value_counts()
# male      577
# female    314
# Name: sex, dtype: int64


