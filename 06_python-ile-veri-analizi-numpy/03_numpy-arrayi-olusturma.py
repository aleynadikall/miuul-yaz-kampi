# Numpy Array'i Oluşturmak ( Creating Numpy Array)

# Numpy Array'leri diğer adıyla ndarray nesneleri python'da kullanılan diğer bazı veri yapıları gibi bir veri yapısıdır.
# Numpy işlemlerini yapabilmek için öncelikle bir numpy array'ine ihtiyaç vardır.
# Genelde bu numpy array'leri sıfırdan oluşturulmaz. Çalışmamız esnasındaki bazı veri yapılarından dönüştürülerek elde
# edilir.

import numpy as np

# Bir liste üzerinden numpy array oluşturalım:
np.array([1, 2, 3, 4, 5])
type(np.array([1, 2, 3, 4, 5]))         # numpy.ndarray

# girdiğimiz sayı adedince 0 oluşturur:
np.zeros(10, dtype=int)         # array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

# integerlardan oluşan belli aralıkta array oluşturur:
np.random.randint(0, 10, size=10)       # 0 ile 10 arasında rastgele 10 tane seçim
# array([5, 5, 7, 2, 2, 2, 6, 2, 2, 3])

# Belirli bir istatistiksel dağılıma göre sayı üretmek istersek:
np.random.normal(10, 4, (3, 4))       # Ortalaması 10, standart sapması 4 olan 3'e 4'lük bir array oluştur.
# array([[ 6.80498726,  5.77186124,  6.25189272,  9.45858415],
#        [16.10283596,  8.51395898, 13.82815873, 11.91057431],
#        [ 7.43184433, 13.83759722, -1.32239249,  7.27276869]])













