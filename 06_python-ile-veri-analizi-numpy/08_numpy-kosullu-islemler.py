# Numpy'da Koşullu İşlemler (Conditions on NumPy)

import numpy as np
v = np.array([1, 2, 3, 4, 5])


# Amaç: Bu array içerisindeki 3'ten küçük olan değerlere erişmek.

# Klasik yol: Döngü ile...

ab = []
for i in v:
    if i < 3:
        ab.append(i)

ab      # [1, 2]


# numpy ile:

v < 3           # array([ True,  True, False, False, False])

# Bu şekilde True olarak gördüklerini seçecek False olarak gördüklerini seçmeyecek:
v[v < 3]        # array([1, 2])

v[v > 3]        # array([4, 5])
v[v != 3]       # array([1, 2, 4, 5])
v[v == 4]       # array([4])
v[v >= 4]       # array([4, 5])

