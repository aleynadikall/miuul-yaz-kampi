# Ne zaman fonksiyon yazma ihtiyacımız olur?

# Diyelim ki bir belediyede işe girdik ve belediyenin çeşitli alanlarda kurmuş olduğu akıllı sokak lambaları var. Bu
# sokak lambalarından gelen bazı sinyaller/bilgiler olduğunu düşünelim. Bu bilgiler ısı, nem ve şarj durumu olsun.
# Diyelim ki bu akıllı sokak lambalarından gelen bilgileri kullanarak bazı hesaplamalar yapmak istiyoruz. Çıkan
# sonuçlara göre çeşitli aksiyonlar almak istiyoruz.

# warm, moisture, charge
(56 + 15) / 80      # 0.8875
(17 + 45) / 70      # 0.8857142857142857
(17 + 45) / 80      # 0.775

# Yukarıdaki işlemleri sınırlı olduğu sürece yapabiliriz ancak işlem yapamayacağımız miktarda değer olduğunda fonksiyon
# kullanmamız hem zamanımızdan tüketmeyecek hem de işimizi kolaylaştıracaktır.

# DRY prensibi: "Don't repeat yourself!"


def calculate(warm, moisture, charge):
    print((warm + moisture) / charge)


calculate(98, 12, 78)       # 1.4102564102564104

