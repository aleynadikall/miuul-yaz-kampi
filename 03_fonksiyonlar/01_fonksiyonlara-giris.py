# FONKSİYONLAR, KOŞULLAR (Conditions), DÖNGÜLER (Loops), COMPREHENSIONS

# Fonksiyon Okuryazarlığı
# Önce print() fonksiyonunu ile alalım. print'in görevi içine yazdığımız ifadeye ekrana yazdırmaktı.

print('a')
# Peki print'in bu görevini nasıl değerlendirebiliriz. Nasıl anlayabiliriz? Ne yapmaktadır, nasıl yapmaktadır şeklinde
# nasıl bulabiliriz?

?print      # Hakkında bilgi almak istediğimizde böyle yapıyoruz. Ancak bunu console'dan yapmamız daha sağlıklı olur
# çünkü bu şekilde daha temiz bir çalışma ortamı sağlamış oluruz.

# DİKKAT: Parametre ifadesi de argüman ifadesi de doğrudur. Fakat bunun tam karşılığı şudur: Parametre fonksiyon
# tanımlanması esnasında ifade edilen değişkenlerdir. Argüman ise bu fonksiyonlar çağrıldığında bu parametre değerlerine
# karşılık girilen değerlerdir. Fakat yaygın kullanımı bunların hepsine argüman deme eğilimi yönündedir. Dolayısıyla biz
# de argüman diyerek ifade etmiş olacağız.

# Argümanlar bir özellik belirtebileceği gibi fonksiyonun genel amacını biçimlendirmek üzere kullanılan alt görevcilerdir.
# Bunu bir örnekle pekiştirelim hemen: Normalde print fonksiyonunun görevi nedir, ekrana bir şeyler yazdırmaktır. sep
# argümanı ile iki değer arasına string koyarak ayırmamıza yardımcı olur.

print("a", "b")     # sep argümanının default değeri zaten boşluk olduğundan ekrana a ve b yi boşluklu (a b) yazdırdı.
print("a", "b", sep = "__")     # a__b

help(print)     # aynı şekilde fonksiyon hakkında bize bilgi verir.

# Fonksiyon Tanımlama
# Girilen sayıyı iki ile çarpan fonksiyon:

# - Ey Python! Ben geliyorum, fonksiyon tanımlayacağım.
# + Hoş geldin. Gel, buyur. Fonksiyona bir isim vermek ister misin?
# - Elbette, isimsiz fonksiyon mu olur?

def calculate(x):
    print(x * 2)
# Tanımladığımız fonksiyon sağ tarafta özel değişkenler içerisinde yer alır.

calculate(10)

# İki argümanlı, iki parametreli fonksiyon tanumlayalım:
def summer(x, y):
    print(x + y)


summer(3, 7)
# Bazı durumlarda sıralamanın önemi vardır. Bu nedenle şunu yapmamız doğru olur.
summer(x = 8, y = 7)

