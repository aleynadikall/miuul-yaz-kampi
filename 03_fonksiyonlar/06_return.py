# Return: Fonksiyon çıktılarını girdi olarak kullanmak için kullanılan bir yapıdır.


def calculate(warm, moisture, charge):
    print((warm + moisture) / charge)


calculate(98, 12, 78) * 10      # TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'

type(calculate(98, 12, 78))     # NoneType

# Peki fonksiyonu print olmadan yazsak ne olur?


def calc(warm, moisture, charge):
    (warm + moisture) / charge


calc(98, 12, 78) * 10       # TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'
type(calc(98, 12, 78))      # NoneType


def calculation(warm, moisture, charge):
    return (warm + moisture) / charge

# Kod akışı esnasında return görüldükten sonra bir kod varsa bu çalışmaz.


calculation(98, 12, 78) * 10        # 14.102564102564104

# Bu sonucu bir değişkene atayabiliriz.
a = calculation(98, 12, 78) * 10


def clctn(warm, moisture, charge):
    warm = warm * 2
    moisture = moisture * 2
    charge = charge * 2
    output = (warm + moisture) / charge
    return warm, moisture, charge, output
    # Birden fazla çıktı almak istiyorsak return'ü yukarıdaki şekilde yazmalıyız.

clctn(98, 12, 78)           # (196, 24, 156, 1.4102564102564104)
type(clctn(98, 12, 78))     # tuple

warm, moisture, charge, output = clctn(98, 12, 78)
# Bu şekilde sırayla değerleri birer değişkene atayabiliriz.



