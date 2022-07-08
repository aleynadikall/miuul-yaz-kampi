# Pandas Serileri (Pandas Series)

# Pandas serileri ve pandas dataframeleri en yaygın kullanılan veri yapılarıdır.
# Pandas serileri tek boyutlu ve index bilgileri barındıran bir veri tipidir.
# Pandas dataframe'i ise çok boyutlu ve index bilgisi barındıran bir diğer veri tipidir.

import pandas as pd

# Series bir metoddur ve der ki bana bir liste veya farklı tipte bir veri ver ki ben bunu pandas serisine çevireyim.
pd.Series([10, 77, 12, 4, 5])
# 0    10
# 1    77
# 2    12
# 3     4
# 4     5
# dtype: int64

# Veri yapısını atama işlemi ile kaydedelim:
s = pd.Series([10, 77, 12, 4, 5])

# DİKKAT: Veri yapıları bizim için şu açıdan önemlidir: Bir veri yapısının liste mi tuple mı set mi pandas serisi mi
# pandas dataframe mi yoksa numpy array'i mi olduğunu bilmek fonksiyonların bizden beklediği ihtiyaçları daha doğru bir
# şekilde yerine getirme imkanı sağlar ya da karşılaşabileceğimiz bazı problemleri daha iyi çözme imkanı sağlar.
# Örneğin kullanacak olduğumuz bir fonksiyon bizden bir dataframe beklerken biz ona bir pandas serisi gönderdiğimizde
# hata verecektir ve alana yeni başlıyorsak bu hatayı anlamak veya araştırmak bizi biraz zorlayacaktır. Dolayısıyla veri
# yapılarını iyi bilirsek çıktılarda en azından hata alınan durumlarda hızlı bir şekilde hatayı anlayabilmemize katkısı
# olur. Diğer yandan fonksiyonların ihtiyaç ve beklentilerini daha doğru şekilde yerine getirmiş oluruz.


type(s)         # pandas.core.series.Series

# Index bilgisine erişmek için:
s.index         # RangeIndex(start=0, stop=5, step=1)

# İçerisindeki verinin tip bilgisi için:
s.dtype         # dtype('int64')

# İçinde barınan eleman sayısı için:
s.size          # 5

# Boyut bilgisine erişmek için:
s.ndim          # 1

# Bu serinin içindeki değerlerin kendilerine erişmek için:
s.values        # array([10, 77, 12,  4,  5], dtype=int64)

# DİKKAT: Yine veri yapısı farkındalığına ilişkin bir değerlendirme yapalım: Yukarıda gözlemleneceği üzere bir çıktı
# geldi ama acaba bu çıktının tipi nedir?
type(s.values)
# numpy.ndarray ifadesi döner. Bir pandas serisinin sonuna values ifadesini girdiğimizde ve değerlerine erişmek
# istediğimizde bu durumda zaten index bilgisi ile ilgilenmiyorum demiş olduğumuzdan dolayı bize bunu bir numpy array'i
# olarak döndürdü. Dolayısıyla bunun farkında olduğumuzda hata alma ihtimalimizi azaltırız.

# Seri içindeki ilk 5 gözlemi getirmek için:
s.head()
# 0    10
# 1    77
# 2    12
# 3     4
# 4     5
# dtype: int64

s.head(3)
# 0    10
# 1    77
# 2    12
# dtype: int64

# Sondan 3 gözlemi görmek için:
s.tail(3)
# 2    12
# 3     4
# 4     5
# dtype: int64



