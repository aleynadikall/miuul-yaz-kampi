# Ön Tanımlı Argümanlar/Parametreler (Default Parameters/Arguments)

# Bölme işlemi yapmak üzere bir fonksiyon tanımlayalım:
def divide(a, b):
    print(a / b)


divide(1, 2)

# Varsayalım ki bu fonksiyonda çok fazla argüman var ya da bu fonksiyonun özelinde de düşünebiliriz, bir şekilde
# kullanıcı ile etkileşim sağlayacak bu fonksiyonu kullanıcı daha kolay bir şekilde kullanabilsin diye varsaydığımızı
# düşünelim. Bu durumda bazı argümanlarımıza ön tanımlı değerler ekleyerek kullanıcılar her argümanı girmemiş olsa dahi
# fonksiyonların çalışmasını sağlayabiliriz.


def bolme(a, b=3):
    print(a / b)


bolme(18)       # 6.0

