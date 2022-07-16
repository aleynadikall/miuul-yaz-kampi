
# 2. Kategorik Değişken Analizi (Analysis of Categorical Variables)

# DİKKAT: Bu bölüm oldukça önemlidir. Bize programatik bir şekilde kategorik deişkenleri yapmak için gerekli olan bazı
# bilgileri edinicez. Öyle ki veri analtiği veri bilimi makine öğrenmesi gibi süreçlerde geliştirmeler yaparken göz
# yordamıyla değil de programatik olarak bazı tanımlamarı yapabiliyor ve takip edebiliyor olmamız lazım. Bu şu anlama
# gelir, örneğin biz burada bir kategorik değişkeni analiz edelim diye düşündüğümüzde hemen görüyoruz cinsiyet değişkeni
# embark değişkeni gibi değişkenler var. Tamam bunu göz yordamıyla gördük. Peki soru şu: Burada 1500 tane değişken
# olsaydı yine bu şekilde göz yordamıyla bu değişkenleri yakalayabiliyor olacak mıydık? Tabii ki olamayacaktık.
# Dolayısıyla tek bir değişkeni analiz etmek istiyorsak, örneğin value_counts'u kullanıp bunu analiz edebiliriz. Fakat
# burada çok fazla sayıda değişken olduğunda bunları tek tek gidip yakalayamıyor olacağız. İşte bu bölümde programatik
# (fonksiyonel) bir şekilde (bu bölümleri gelişmiş olarak adlandırmamızın sebebi budur) genellenebilirlik kaygısıyla
# değişken tiplerini yakalamayı ve bunların özelinde analiz yapacak bir fonksiyon yazma işlemini gerçekleştirmiş
# olacağız.


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
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

# Tek bir değişkeni analiz etmek istediğimizde value_counts metodunu kullanarak sınıf sayılarına erişebiliriz:
df["survived"].value_counts()
# 0    549
# 1    342
# Name: survived, dtype: int64

# Bir başka değişkenin unique değerlerine erişmek istersek:
df["sex"].unique()
# array(['male', 'female'], dtype=object)

# Toplamda kaç tane eşsiz değer var bilgisine erişmek için:
df["class"].nunique()
# 3


# Çok fazla değişken olduğunda bunları yukarıdaki şekilde yakalayamayacağımız aşikardır.

# Öyle bir şey yapmalıyız ki bu veri setinin içerisinden otomatik bir şekilde bize bütün olası kategorik değişkenleri
# seçsin. Bunu birkaç aşamada yapacağız. Öncelikle tip bilgisine göre seçeceğiz, daha sonra tip konusunda bizi atlatmış
# başka tipte gözüken ama aslında kategorik olan sinsirellaları da yakalayacağız. Bu iki durumu örneklendirelim.

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


# Birincisi tip bilgisi:

# 10  adult_male   891 non-null    bool
#  11  deck         203 non-null    category
#  12  embark_town  889 non-null    object
# bool object aslında kategorik değişkendir. bool True(1) False(0)'lardan oluşur.

# 7   embarked     889 non-null    object
# embarked objecttir, 3 sınıfı vardır ancak kategoriktir. Dolayısıyla bizim için tip bilgisinden hareketle kategorik
# olan değişkenler 3 tanedir: bool, category ve object.

# List comprehension yapısı ile cat_cols adında bir liste oluşturalım:
cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]
cat_cols
# ['sex',
#  'embarked',
#  'class',
#  'who',
#  'adult_male',
#  'deck',
#  'embark_town',
#  'alive',
#  'alone']

df["sex"].dtypes
# dtype('O')

# Yukarıdaki ifadeyi stringe çevirelim:
str(df["sex"].dtypes)
# 'object'

# Bu object içinde midir diyelim:
str(df["sex"].dtypes) in ["object"]
# True

# Tekrar örneklendirelim:
df["alone"].dtypes                          # dtype('bool')
str(df["alone"].dtypes)                     # 'bool'
str(df["alone"].dtypes) in ["bool"]         # True


# gelelim sinsirellalara mesela survived değişkeninin tipi int olmasına rağmen kategorik değişkendir. 2 sınıftan
# oluşmuştur. Ancak sınıfları 0 ve 1 den oluştuğu için bunu ayırt etmek kolay olmamıştır.

# Eşsiz sınıf sayısına bakarak bir değerlendirme yapalım. Sınırlandırılabilir ise kategoriktir, sayısal değildir.
# 10'dan küçük eşsiz sınıf sayısına sahip değişken varsa bu bizim için numerik görünümlü ama kategorik olan bir
# değişkendir yorumunu yapabiliriz.

num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int64", "float64"]]
num_but_cat
# ['survived', 'pclass', 'sibsp', 'parch']


# Diyelim ki çalıştığımız veri setinde yine object ve kategorik tipte olan değişkenler var ama bu sefer bu
# değişkenlerden birisinin sınıf sayısı çok fazla olabilir. Mesela burade name bir isim değişkeni olsaydı yolcuların
# isimleri olsaydı muhtemelen 891 tane, isim soyisimden dolayı, unique isim olacaktı bu kategorik değişken değildir.
# Bunlara cardinality'si yüksek değişkenler denir. Bu şu anlama gelir: Ölçülemeyecek kadar, ölçüm değeri taşımayacak
# kadar açıklanabilirlik taşımayacak kadar fazla sınıfı vardır anlamına gelir. Bir kategorik değişkenin 50 sınıfı
# olması çok büyük ihtimalle onun bir bilgi, anlam taşımadığı anlamına gelir. Öyle bir şey yapmalıyız ki programatik
# olarak da bu veri setindeki kategorik tipte olduğu halde kategorik olmayan değişkenleri de yakalayabiliyor olmalıyız:

# Ölçülebilir olmayan değişkenlerin bulunması:
cat_but_cardinal = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ["category", "object"]]
cat_but_cardinal
# []
# Yani yok ancak başka bir senaryoda olabilir, bunu göz önünde bulundurmalıyız.

# Toparlayalım:
cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ["category", "object"]]

cat_cols = cat_cols + num_but_cat

cat_cols = [col for col in cat_cols if col not in cat_but_car]

# Bu seçtiğimiz değişkenleri ilgili dataframe içerisinden seçmek istersek:
df[cat_cols]
#         sex embarked   class    who  adult_male deck  embark_town alive  alone  survived  pclass  sibsp  parch
# 0      male        S   Third    man        True  NaN  Southampton    no  False         0       3      1      0
# 1    female        C   First  woman       False    C    Cherbourg   yes  False         1       1      1      0
# 2    female        S   Third  woman       False  NaN  Southampton   yes   True         1       3      0      0
# 3    female        S   First  woman       False    C  Southampton   yes  False         1       1      1      0
# 4      male        S   Third    man        True  NaN  Southampton    no   True         0       3      0      0
# ..      ...      ...     ...    ...         ...  ...          ...   ...    ...       ...     ...    ...    ...
# 886    male        S  Second    man        True  NaN  Southampton    no   True         0       2      0      0
# 887  female        S   First  woman       False    B  Southampton   yes   True         1       1      0      0
# 888  female        S   Third  woman       False  NaN  Southampton    no  False         0       3      1      2
# 889    male        C   First    man        True    C    Cherbourg   yes   True         1       1      0      0
# 890    male        Q   Third    man        True  NaN   Queenstown    no   True         0       3      0      0
# [891 rows x 13 columns]
# Şu an yukarıdakiler kategorik değişkendir.

# Seçtiğimiz değişkenlerin eşsiz sınıf sayısına bakıp bu işlemleri doğrulayalım:
df[cat_cols].nunique()
# sex            2
# embarked       3
# class          3
# who            3
# adult_male     2
# deck           7
# embark_town    3
# alive          2
# alone          2
# survived       2
# pclass         3
# sibsp          7
# parch          7
# dtype: int64

# Sayısal olanlara ne olduğu sorusuna cevap almak için:
[col for col in df.columns if col not in cat_cols]
# ['age', 'fare']
# Baştan sadece numerikleri seçip dışında kalanlara göre işlem yapsaydık?
# Hayır, hepsini ayrı ayrı farklı senaryolara göre seçebiliyor olmak durumundayız.

# Şimdi bunlara bir fonksiyon yazalım:

# Bu fonksiyonun ne yapacağını kenarda bir hesaplayalım:
df["survived"].value_counts()
100 * df["survived"].value_counts() / len(df)
# 0    61.616162
# 1    38.383838
# Name: survived, dtype: float64


def cat_summary(dataframe, col_name):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##########################################")


cat_summary(df, "sex")
#         sex      Ratio
# male    577  64.758698
# female  314  35.241302
# ##########################################

# Her birisi için ayrı ayrı yapamayız, bu yüzden for ile işimizi kolaylaştıralım:
for col in cat_cols:
    cat_summary(df, col)
#         sex      Ratio
# male    577  64.758698
# female  314  35.241302
# ##########################################
#    embarked      Ratio
# S       644  72.278339
# C       168  18.855219
# Q        77   8.641975
# ##########################################
#         class      Ratio
# Third     491  55.106622
# First     216  24.242424
# Second    184  20.650954
# ##########################################
#        who      Ratio
# man    537  60.269360
# woman  271  30.415264
# child   83   9.315376
# ##########################################
#        adult_male     Ratio
# True          537  60.26936
# False         354  39.73064
# ##########################################
#    deck     Ratio
# C    59  6.621773
# B    47  5.274972
# D    33  3.703704
# E    32  3.591470
# A    15  1.683502
# F    13  1.459035
# G     4  0.448934
# ##########################################
#              embark_town      Ratio
# Southampton          644  72.278339
# Cherbourg            168  18.855219
# Queenstown            77   8.641975
# ##########################################
#      alive      Ratio
# no     549  61.616162
# yes    342  38.383838
# ##########################################
#        alone     Ratio
# True     537  60.26936
# False    354  39.73064
# ##########################################
#    survived      Ratio
# 0       549  61.616162
# 1       342  38.383838
# ##########################################
#    pclass      Ratio
# 3     491  55.106622
# 1     216  24.242424
# 2     184  20.650954
# ##########################################
#    sibsp      Ratio
# 0    608  68.237935
# 1    209  23.456790
# 2     28   3.142536
# 4     18   2.020202
# 3     16   1.795735
# 8      7   0.785634
# 5      5   0.561167
# ##########################################
#    parch      Ratio
# 0    678  76.094276
# 1    118  13.243547
# 2     80   8.978676
# 3      5   0.561167
# 5      5   0.561167
# 4      4   0.448934
# 6      1   0.112233
# ##########################################








