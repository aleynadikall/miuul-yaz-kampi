# Yeniden Şekillendirme (Reshaping): Elimizdeki numpy array'inin boyutunu değiştirmek istediğimizde kullanırız.

import numpy as np

np.random.randint(1, 10, size=9)        # array([6, 1, 6, 3, 4, 3, 8, 7, 8])

# Bu array tek boyutludur, bunu iki veya üç boyutlu hale getirmek istiyoruz:

np.random.randint(1, 10, size=9).reshape(3, 3)
# array([[8, 3, 1],
#        [6, 3, 2],
#        [6, 5, 6]])

# DİKKAT: Bu işlemleri bir yere atayarak gerçeleştirmedik. Dolayısıyla kalıcı bir yerde tutulmuyor.

ar = np.random.randint(2, 24, size=12)
ar.reshape(4, 3)
# array([[17,  6,  5],
#        [10, 11, 10],
#        [14, 15,  4],
#        [ 8,  2, 11]])

np.random.randint(1, 10, size=10).reshape(3, 3)         # ValueError: cannot reshape array of size 10 into shape (3,3)


