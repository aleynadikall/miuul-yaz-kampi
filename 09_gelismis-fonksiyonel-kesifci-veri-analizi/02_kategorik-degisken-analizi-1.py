
# 2. Kategorik Değişken Analizi (Analysis of Categorical Variables)
# DİKKAT: Bu bölüm oldukça önemlidir. Bize programatik bir şekilde kategorik deişkenleri yapmak için gerekli olan bazı
# bilgileri edinicez. Öyle ki veri analtiği veri bilimi makine öğrenmesi gibi süreçlerde geliştirmeler yaparken göz
# yordamıyla değil de programatik olarak bazı tanımlamarı yapabiliyor ve takip edebiliyor olmamız lazım. Bu şu anlama
# gelir, örneğin biz burada bir kategorik değişkeni analiz edelim diye düşündüğümüzde hemen görüyoruz cinsiyet değişkeni
# embark değişkeni gibi değişkenler var. Tamam bunu göz yordamıyla gördük. Peki soru şu: Burada 1500 tane değişken
# olsaydı yine bu şekilde göz yordamıyla bu değişkenleri yakalayabiliyor olacak mıydık? Tabii ki olamayacaktık.
# Dolayısıyla tek birdeğişkeni analiz etmek istiyorsak, örneğin value_counts'u kullanıp bunu analiz edebiliriz. Fakat
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


# Çok fazla olduklarında bunları yukarıdaki şekilde yakalayamayacağımız aşikardır.

# Öyle bir şey yapmalıyız ki bu veri setinin içerisinden otomatik bir şekilde bize bütün olası kategorik değişkenleri
# seçsin. Bunu birkaç aşamada yapacağız. Öncelikle tip bilgisine göre seçeceğiz, daha sonra tip konusunda bizi atlatmış
# başka tipte gözüken ama aslında kategorik olan sinsirellaları da yakalayacağız. Bu iki durumu örneklendirelim.
cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]

num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int", "float"]]

cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ["category", "object"]]

cat_cols = cat_cols + num_but_cat

cat_cols = [col for col in cat_cols if col not in cat_but_car]

df[cat_cols].nunique()

[col for col in df.columns if col not in cat_cols]


df["survived"].value_counts()
100 * df["survived"].value_counts() / len(df)


def cat_summary(dataframe, col_name):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##########################################")


cat_summary(df, "sex")

for col in cat_cols:
    cat_summary(df, col)


def cat_summary(dataframe, col_name, plot=False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##########################################")

    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show(block=True)

cat_summary(df, "sex", plot=True)

for col in cat_cols:
    if df[col].dtypes == "bool":
        print("sdfsdfsdfsdfsdfsd")
    else:
        cat_summary(df, col, plot=True)


df["adult_male"].astype(int)


for col in cat_cols:
    if df[col].dtypes == "bool":
        df[col] = df[col].astype(int)
        cat_summary(df, col, plot=True)

    else:
        cat_summary(df, col, plot=True)




def cat_summary(dataframe, col_name, plot=False):

    if dataframe[col_name].dtypes == "bool":
        dataframe[col_name] = dataframe[col_name].astype(int)

        print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                            "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
        print("##########################################")

        if plot:
            sns.countplot(x=dataframe[col_name], data=dataframe)
            plt.show(block=True)
    else:
        print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                            "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
        print("##########################################")

        if plot:
            sns.countplot(x=dataframe[col_name], data=dataframe)
            plt.show(block=True)

cat_summary(df, "adult_male", plot=True)





def cat_summary(dataframe, col_name):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##########################################")

cat_summary(df, "sex")