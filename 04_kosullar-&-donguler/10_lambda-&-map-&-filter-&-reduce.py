# lambda, map, filter, reduce

# Python'ın fonksiyonel programlama yönüne hitap eden vektör seviyesinde işlemler yapma yönüne hitap eden bazı
# araçlardır.

# lambda: bir kullan at fonksiyonudur.
# daha önce bir fonksiyon tanımlamak istediğimizde bunu şu şekilde tanımlıyorduk:
def summer(a, b):
    return a + b


summer(1, 3) * 9  # 36

new_sum = lambda a, b: a + b
# Kullan at fonksiyonu olduğundan değişkenler kısmında lambdayı göremeyiz.

new_sum(4, 5)  # 9

# map: bizi döngü yazmaktan kurtarır.

salaries = [1000, 2000, 3000, 4000, 5000]


def new_Salary(x):
    return x * 20 / 100 + x


new_Salary(5000)  # 6000.0

for salary in salaries:
    print(new_Salary(salary))

# Ekran Çıktısı:
# 1200.0
# 2400.0
# 3600.0
# 4800.0
# 6000.0

list(map(new_Salary, salaries))  # [1200.0, 2400.0, 3600.0, 4800.0, 6000.0]

# lambda ve map ilişkisi:
list(map(lambda x: x * 20 / 100 + x, salaries))  # [1200.0, 2400.0, 3600.0, 4800.0, 6000.0]

list(map(lambda x: x ** 2, salaries))  # [1000000, 4000000, 9000000, 16000000, 25000000]

# filter: adı üstünde olduğu gibi filtreleme işlemleri için kullanılır.

list_store = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(filter(lambda x: x % 2 == 0, list_store))  # [2, 4, 6, 8, 10]

# reduce: indirgemek demektir.

from functools import reduce
list_store = [1, 2, 3, 4]
reduce(lambda a, b: a + b, list_store)        # 10

# Çalışacağın zaman lambda ve map'e yoğunluk verebilirsin çünkü filter ve reduce çok sık kullanılmaz.





