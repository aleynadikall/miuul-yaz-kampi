# Numpy Array Özellikleri (Attributes of Numpy Arrays)

import numpy as np

# ndim: boyut sayısı
# shape: boyut bilgisi
# size: toplam eleman sayısı
# dtype: array veri tipi

a = np.random.randint(10, size=5)       # a = np.random.randint(0, 10, size=5) ile aynı şeydir.


a           # array([7, 1, 3, 3, 7])
a.ndim      # 1
a.shape     # (5,)
a.size      # 5
a.dtype     # dtype('int32')




