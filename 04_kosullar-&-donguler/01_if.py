# KOŞULLAR (CONDITIONS)
# Program yazımı esnasında akış kontrolü sağlayan ve programların belirli kurallara veya koşulara göre nasıl hareket
# etmesi gerektiğini biz kullanıcılar tarafından programlara bildirme imkanı sağlayan yapılardır. Şu koşul sağlanıyorsa
# bunu yap sağlanmıyorsa şunu yap şeklinde akışlar tasarlanmasını sağlar.


# True-False'u hatırlamakla başlayalım.
1 == 1      # True
1 == 2      # False


# if

if 1 == 1:
    print("something")

# Bu koşul True olarak döndüğünden ekrana something yazdırıldı.

if 1 == 2:
    print("something")

# False döndüğü için ekrana bir şey yazdırmadı. Ancak True dönmesi durumunda ekrana bir şeyler yazdıracaktır.

number = 11

if number == 10:
    print("number is 10")
# False döndüğünde ekrana bir şey yazdırılmadı. Bir sonuç gelmedi.


if number == 11:
    print("number is 11")
# number is 11

# Bu kısma kadar görüldüğü gibi birçok ayrı if yazdık. DRY prensibine ters düşmüş olduk. Bunu fonksiyon yazarak
# engeleyebiliriz.


def number_check(numberr):
    if numberr == 10:
        print("number is 10")


number_check(12)        # Sonuç üretmedi.
number_check(10)        # number is 10









