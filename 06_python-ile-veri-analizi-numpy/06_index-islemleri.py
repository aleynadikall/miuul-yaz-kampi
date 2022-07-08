# Index Seçimi (Index Selection)

import numpy as np
a = np.random.randint(10, size=10)


# Slicing

a[0]        # 2

# Birden fazla seçim yapmak istersek:
a[0:5]      # array([2, 7, 4, 9, 0])

# İstediğimiz şekilde eleman değerlerini değiştirebiliriz:
a[0] = 999

m = np.random.randint(10, size=(3, 5))

m
# array([[4, 5, 8, 4, 8],
#        [8, 4, 0, 1, 1],
#        [9, 7, 9, 5, 9]])

m[0, 0]     # 4
# DİKKAT: Virgülden öncesi satırları sonrası ise sütunları ifade etmektedir.

m[2, 3]     # 5

m[2, 3] = 999
m
# array([[  4,   5,   8,   4,   8],
#        [  8,   4,   0,   1,   1],
#        [  9,   7,   9, 999,   9]])

# DİKKAT: Buraya inteeger bir değer yerine float bir değer eklemek isteseydik:
m[2, 3] = 2.9
m
# array([[4, 5, 8, 4, 8],
#        [8, 4, 0, 1, 1],
#        [9, 7, 9, 2, 9]])

# 2.9 yazmamıza rağmen 2 değeri eklendi çünkü numpy fixed type bir arraydir. numpy'ı hızlı kılan verimli veri saklama
# özelliğidir. numpy der ki üzerinde bin tane dahi değer tutsan bunların hepsi için ben tek bir tip bilgisi tutarım
# böylece verimli veri saklarım. Bu sebeple numpy'a değer girmek istediğimizde diğerleriyle uyumlu olmasına dikkat
# etmeliyiz.

# Tek boyutlularda şuradan şuraya git şeklinde yaptığımız slice işlemini burada da gerçekleştirebiliriz:
m[:, 0]     # tüm satırlar 0.sütun
# array([4, 8, 9])

m[1, :]     # 1.satır tüm sütunlar
# array([8, 4, 0, 1, 1])

# Hem satırlardan belli bir aralık hem sütunlardan belli bir aralık verebiliriz:
m[0:2, 0:3]
# array([[4, 5, 8],
#        [8, 4, 0]])





