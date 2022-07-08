# Matematiksel İşlemler (Mathematical Operations)

import numpy as np
v = np.array([1, 2, 3, 4, 5])

v / 5           # array([0.2, 0.4, 0.6, 0.8, 1. ])
v * 5 / 10      # array([0.5, 1. , 1.5, 2. , 2.5])

v ** 2          # array([ 1,  4,  9, 16, 25])

v - 1           # array([0, 1, 2, 3, 4])


# Bu işlemleri operatörler aracılığıyla gerçekleştirdiğimiz gibi metodlar aracılığıyla da gerçekleştirebiliriz:

# Çıkarma İşlemi:
np.subtract(v, 1)           # array([0, 1, 2, 3, 4])

# Toplama İşlemi:
np.add(v, 1)                # array([2, 3, 4, 5, 6])

# Numpy Array Ortalaması:
np.mean(v)                  # 3.0

# Tüm Elemanların Toplamı:
np.sum(v)                   # 15

np.min(v)                   # 1

np.max(v)                   # 5

# Varyansı:
np.var(v)                   # 2.0

# DİKKAT: Hiçbir elemanın atamasını yapmadık sadece sonuçları gözlemliyoruz. Kalıcı hale getirmek için tekrar atama
# şarttır.

# Basit işlemleri gerçekleştirdiğimiz gibi bazı ileri seviye işlemleri (türev, integral) de gerçekleştirebiliriz:
# Ya da iki bilinmeyenli denklem çözmede de kullanabiliriz:

# Numpy ile İki Bilinmeyenli Denklem Çözme:

# 5 * x0 + x1 = 12
# x0 + 3 * x1 = 10

a = np.array([[5, 1], [1, 3]])          # katsayılar bir array'de olmalı
b = np.array([12, 10])                  # sonuçlar bir array'de olmalı

np.linalg.solve(a, b)                   # array([1.85714286, 2.71428571])







