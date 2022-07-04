# Karakter Dizileri (Strings)

print("John")

# Print olmadan da bu ifadeleri çalıştırabiliriz.
"John"   # yazmamız bunun için yeterlidir.

# DİKKAT: Bir program veya fonksiyon yazıyorsak bu program veya fonksiyonun içerisindeki bir noktada ekrana bir bilgi
# paylaşmak istiyorsak ancak bu durumda print kullanmamız gerekir. Etkileşimden yararlanmak istediğimizde ise ipython'ın
# bize sağladığı bu etkileşimden yararlanırken daha genel olarak aslında print yazmadan kullanıyor olacağız. Fakat
# fonksiyonlar ys da döngülere geçtiğimizde ekranda bir bilgi paylaşmak istediğimizde bu durumlarda printi sık bir şekilde
# kullanacağız.

# Atama ile de bu işlemi yapabiliriz:
name = "John"
name

# Çok Satırlı Karakter Dizileri 3 tırnak içerisinde yazılır.
""" Veri Yapıları: Hızlı Özet,
Sayılar (Numbers): int, float, complex,
Karakter Dizileri (strings): str,
List, Dictionary, Tuple, Set,
Boolean (TRUE-FALSE): bool"""

# İstiyorsak bunu bir değişken içerisinde tutabilir ve bu değişken üzerinde de çalışabiliriz:
long_str = """ Veri Yapıları: Hızlı Özet, Sayılar (Numbers): int, float, complex, Karakter Dizileri (strings): str,List, 
Dictionary, Tuple, Set,Boolean (TRUE-FALSE): bool """
long_str

# Karakter Dizilerinde Eleman Seçme İşlemleri
name
name[0]
name[3]

# Karakter Dizilerinde Slice İşlemi
name
name[0:2]
long_str[0:10]

# String İçerisinde Karakter/karakter dizisi Sorgulamak
long_str
"veri" in long_str   # False dedi
"Veri" in long_str   # True döndü
"bool" in long_str
"V" in long_str