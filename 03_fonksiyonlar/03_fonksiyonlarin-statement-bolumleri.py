# Fonksiyonların Statement/Body Bölümü

# def function_name(parameters/arguments):
#     statements (function body)

# Bir fonksiyon parametresiz/argümansız da olabilir.


# 3 tane string değeri peş peşe yazdıracak ancak herhangi bir argüman taşımayacak fonksiyonu yazalım:
def say_hi():
    print("Merhaba")
    print("Hi")
    print("Hello")

say_hi()        # fonksiyona herhangi bir parametre girmedik. Ama çağırdığımızda fonksiyon içerisinde ne varsa ekrana
# yazdırdı.


def say_hello(string):
    print(string)
    print("Hi")
    print("Hello")


say_hello()     # TypeError: say_hello() missing 1 required positional argument: 'string'

say_hello("miuul")


# Girilen iki sayıyı çarpan, bunu önce bir nesnede tutan ve sonucu ekrana yazdıran fonksiyonu yazalım:

def multiplication(a, b):
    c = a * b
    print(c)

multiplication(347, 52)

# Girilen iki değeri birbiriile çarptıktan sonra sonucu bir liste içerisinde saklayacak fonksiyonu yazalım:

# Global scope'tur.
list_store = []

# Bir listeye eleman eklememizi sağlayan metod append'di, şimdi bunu kullanalım.
def add_element(a, b):
    # Aşağısı local scope'tur.
    c = a * b
    list_store.append(c)    # Listenin değiştirilebilir özelliğini unutmayalım!
    print(list_store)       # listenin son halini görmek için


add_element(1, 8)       # [8]
add_element(5, 7)       # [8, 35]
add_element(4, 3)       # [8, 35, 12]

# DİKKAT: Kullandığımız bası metodlar yeniden atama işlemi yapmaya gerek kalmaksızın ilgili veri yapısında kalıcı bir
# değişiklik meydana getirebilir. append metodu o metodlardan birisidir. Bundan dolayı list_store = list_store.append(c)
# gibi bir atama yapmadık.




