# Numpy

# Numerical Python'ın kısaltılmışıdır.
# Bilimsel hesaplamalar için kullanılır.
# Array'ler, çok boyutlu array'ler ve matrisler üzerinde yüksek performanslı çalışma imkanı sağlar.
# Temelleri 1995 yılında atılmıştır.

# NEDEN NUMPY? : kısaca sabit tipte veri tutarak daha hızlı işlem yaptırması diyebiliriz.

# Doğal veri yapılarından olan listelerden farkı verimli veri saklama ve vektörel operasyonlardır.
# Numpy'ın listelerden farklılaştığı iki nokta verimli veri saklama ve yüksek seviyeden işlemlerdir (vektörel işlemler).
# Numpy içerisinde bir veri tutarken bunu fiktip adını verdiği sabitlenmiş tipte tutarak listelere kıyasla çok daha
# hızlı bir şekilde işlem yapma imkanı sağlar. Örneğin bir listenin içerisinde 5 eleman varsa hepsi aynı tipteyse
# listeler her bir elemanın tip, boyut ve diğer bazı meta bilgilerini ayrı ayrı tutarken numpy der ki ben sabit bir
# tipte veri tutarım (örneğin integer olur.), bunun içerisinde sadece integer veri yapısı olduğundan dolayı değil 5 tane
# 5000 tane bile eleman olsa her birisi için ayrı ayrı bir tip ya da boyut ya da meta bilgileri tutmayacak olduğundan
# dolayı verimli veri saklama imkanı sağlayarak hızlı bir şekilde arrayler üzerinde çalışma imkanı sağlar.
# Bir diğer özelliği örneğin döngü yazmaya gerek olmadan array seviyesinde çok basit işlemlerle normalde daha çok çaba
# gerektiren işlemleri gerçekleştirme imkanı sağlar.

import numpy as np

a = [1, 2, 3, 4]
b = [2, 3, 4, 5]

# Amaç: Listedeki elemanları sırasıyla birbiri ile çarpmak istiyoruz.

# Şu ana kadar öğrendiklerimizle (klasik python yolu) şu şekilde yapılabilir:
ab = []

for i in range(0, len(a)):
    ab.append(a[i] * b[i])

ab      # [2, 6, 12, 20]


# Numpy ile yapmanın yolu:

# Önce listeleri numpy arrayine dönüştürüyoruz.
a = np.array([1, 2, 3, 4])
b = np.array([2, 3, 4, 5])

# Sonra da çarpma işlemi gerçekleştiriyoruz.
a * b       # array([ 2,  6, 12, 20])








