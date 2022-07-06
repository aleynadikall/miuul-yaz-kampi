# Fonksiyon içerisinden fonksiyon çağırmak

# Diyelim ki daha önce tanımladığımız birkaç tane fonksiyon var ya da biz tanımlamasak da zaten var olan fonksiyonlar
# olduğunu düşünelim. Fonksiyon tanımlama sırasında bu fonksiyonları çağırabiliyoruz. Bu konuda fonksiyonların statement
# bölümünü biraz daha ele almış olacağız.


def calculation(warm, moisture, charge):
    return (warm + moisture) / charge


calculation(98, 12, 12) * 10    # 91.666666666666...


def calculate(warm, moisture, charge):
    return int((warm + moisture) / charge)
    # float değil de integer tipinde bir değer üretmesi için yukarıdaki şekilde yazmalıyız.


calculate(98, 12, 12) * 10      # 90


def standardization(a, p):
    return a * 10 / 100 * p * p


standardization(45, 1)      # 4.5


# DİKKAT: Eğer bir fonksiyon tanımlıyorsak ve bu fonksiyonun içerisinde başka fonksiyonlar yer alacaksa (çağrılacaksa),
# çağırmış olduğumuz fonksiyonların argümanlarını da eğer bu tanımladığımız ana fonksiyondan biçimlendirmek istersek bu
# durumda ana fonksiyonu tanımlarken fonksiyonun misafir edileceği fonksiyonların argümanlarını da girmemiz
# gerekmektedir.


def all_calculation(warm, moisture, charge, p):
    a = calculate(warm, moisture, charge)
    b = standardization(a, p)
    print(b * 10)


all_calculation(98, 12, 12, 5)      # 225.0


def all_calculate(warm, moisture, charge, a, p):
    print(calculate(warm, moisture, charge))
    b = standardization(a, p)
    print(b * 10)


all_calculate(1, 3, 5, 19, 12)      # 2735.9999999999995





