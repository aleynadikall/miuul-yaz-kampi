# String (Karakter Dizisi) Metotlari

# Veri yapıları üzerinde çalışan bazı özel metotlar vardır. Bu metotlara dir() ile erişiriz.
dir(int)
dir(str)

# len: pythondaki gömülü fonksiyonlardandır. len fonksiyonu stringlere uygulanabilmektedir.
name = "john"
type(name)  # str
type(len)   # builtin_function_or_method
# len'in tipini öğrenmek istediğimizde ekranda fonksiyon veya method gibi bir bilgi döndü yani Python'ın da kafası karışık.

# len bir fonksiyondur bu ayrıma beraber güzelce varacağız.

len(name)   # 4
len("aleynadikal")  # 11
len("miuul")    # 5

# Kullanmış olduğumuz bir yapının metod mu yoksa fonksiyon mu olduğunu nasıl ayırt ederiz.
# DİKKAT: Eğer bir fonksiyon class yapısı içerisinde tanımlandıysa buna metod denir, eğer bir class yapısı içerisinde
# değilse fonksiyondur.
# Metod ve fonksiyon görevleri itibarı ile aynı şeylerdir. Çeşitli görevleri yerine getirirler. Farklılaştıkları nokta
# fonksiyonların bağımsız metodların classlar içerisinde tanımlanmış olmasıdır.

# upper() & lower() metodları: küçük-büyük dönüşümleri
"miuul".upper()
"MIUUL".lower()

type(upper)     # hatalı
type(upper())   # hatalı

# replace: Karakter değiştirme
hi = "Hello ai era"
hi.replace("l", "p")
hi

# split: böler
"Hello AI Era".split()  # boşluklara göre bölme işlemini gerçekleştirir.

# strip: kırpar
" ofofo".strip()
"ofofo".strip("o")

# capitalize: ilk harfi büyütür.
"foo".capitalize()
dir("foo")
"foo".startswith()  # TypeError: startswith() takes at least 1 argument (0 given)
"foo".startswith("f")

