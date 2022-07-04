# DATA STRUCTURES
# Veri yapıları programlama dünyasında önemli bir yere sahiptir. Diğer birçok yapı gibi bir programlama büyük resminin
# küçük alt parçalarındandır. Bu tip küçük parçalar bir araya gelerek programları oluşturur. Veri yapıları programlama
# sürecindeki en küçük yapıtaşlarındandır. Kullanıcıolarak bizlerin bilgisayarlara anlatmak istediği durumları temsil
# eden farklı tiplerde bize veri tutma imkanı sağlayan yapılardır.

# Bu bölümde ele alınacak bazı konular:
# - Veri yapılarına giriş ve hızlı özet
# - Sayılar (Numbers): int, float, complex
# - Karakter Dizileri (strings): str
# - Boolean (TRUE-FALSE): bool
# - Liste (List)
# - Sözlük (Dictionary)
# - Demet (Tuple)
# - Set

###################################################
# Veri Yapılarına Giriş ve Hızlı Özet
###################################################

# Sayılar: integer
x = 46
type(x)

# Sayılar: float
x = 10.3
type(x)

# Sayılar: complex
x = 2j + 1
type(x)

# String
x = "Hello ai era"
type(x)

# Boolean
True
False

# True False'lar birprogram akışı için en önemli veri yapılarından birisidir. Program ancak belirli koşullara göre
# ilerlemek istediğinde bu true false mantıksal operatörlerine göre durumlar gözlemleyip buna göre ilerleyebilecektir.
type(True)
type(False)
5 == 4 # Eşit midir diye sorar. False döner
1 == 1 # True döner
type(3 == 2) # bool döner


# Liste
# En sık kullanacak olduğumuz hemen hemen bütün işlemlerde yanımızda götürmemiz gereken veri yapılarındandır.
x = ["btc", "eth", "xrp"]
type(x)

# Sözlük
x = {"name": "Peter", "Age": 36}
type(x)

# DİKKAT : Sözlük içerisindeki 2 eleman virgül ile ayrılmıştır. Gnelde eleman ayırma işlemi vrigül ile gerçekleştirilir.
# Sözlük yapısı -> Key: Value şeklindeki çiftlerden oluşur.

# Tuple
x = ("python", "ml", "ds")
type(x)

# Set
x = {"python", "ml", "ds"}
type(x)

# NOT: Bu görmüş olduğumuz liste set tuple sözlük veri yapıları aynı zamanda python collections (python arrays) olarak
# geçmektedir.