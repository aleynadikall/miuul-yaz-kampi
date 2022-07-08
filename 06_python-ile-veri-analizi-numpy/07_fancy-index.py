# Fancy Index

import numpy as np

v = np.arange(0, 30, 3)
v[1]        # 3
v[4]        # 12

# Bu şekilde indeksleri tek tek gözlemleyebiliyoruz. Diyelim ki elimizde birden fazla index var tek tek yazmaktan daha
# kolay bi yol olmalı, bunu gerçekleştirmenin yolu fancy indextir. Fancy index bir numpy array'ine bir liste
# girdiğimizde fantastik bir seçim işlemi sağlar.

catch = [1, 2, 3]
v[catch]        # array([3, 6, 9])

