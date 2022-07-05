# Docstring: Fonksiyonlarımıza herkesin anlayabileceği ortak bir dil ile bilgi notu ekleme yoludur. Örnek vermek
# gerekirse bir fonksiyon tanımlayalım, bu fonksiyonun görevi kendisine girilen iki sayıyı toplamak olsun. Fakat bunu
# ben biliyorum. Bu fonksiyonu tanımladığımda daha sonra bunu birisi kullanmak istediğinde bu argümanların ne işe
# yaradığını ya da genel itibari ile bu summer fonksiyonunun ne işe yaradığını bilmiyor olabilir. Bu şekilde eğer ortak
# bir dilde herkesin anlayabileceği formatta bu fonksiyonuma bir docstring bir bilgi notu ekleyebilirsem bu durumda bu
# fonksiyonu kim kullanmak isterse help yazarak bu fonksiyonu kolay bir şekilde kullanmaya başlayabilir. Şimdi bu
# fonksiyonumuza bir docstring ekleyelim.

def summer(arg1, arg2):
    """

    Parameters/Args
    ----------
    arg1: int, float
        # Bir boşluk bırakıp görevini gireriz.
    arg2 int, float

    Returns
    -------

    """
    print(arg1 + arg2)


# DİKKAT: Docstringin bölümlerini şimdi ele alacağız.
# İlk Bölümde fonksiyonun ne yaptığı bilgisi verilir.
# İkinci bölümde parameters dediği aynı zamanda argümanlar da diyebileceğimiz deişkenleri getirdi. Bu değişkenlerin
# tiplerini deyazabiliriz.

# Docstring oluşturmanın birden fazla yolu vardır. En yaygın kulanılan iki yol google ve numpy yoludur.

# Genel olarak docstringler 3 kısımdan oluşur. Bir fonksiyonun ne yaptığı iki argümanların ne yaptığı üç bunun
# çıktısının ne olacağı bölümleridir.

def sum_calculate(arg1, arg2):
    """
    Sum of two numbers

    Args:
        arg1: int, float
            Bu kısma bilgi girilebilir.
        arg2: int, float

    Returns:
        int, float

    Examples:
        Eklenebilir. (Opsiyonel)

    Notes:
        Eklenebilir. (Opsiyonel)
    """

    print(arg1 + arg2)

help(sum_calculate)
?sum_calculate

sum_calculate(1, 3)