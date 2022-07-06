# UYGULAMA: Mülakat Sorusu: ALTERNATING

# Amaç: Aşağıdaki şekilde string değiştiren fonksiyon yazmak istiyoruz.

# before: "hi my name is john and i am learning python"
# after: "Hi mY NaMe iS JoHn aNd i a M LeArNiNg pYtHoN"

range(len("miuul"))     # range bize iki değer arasında sayı üretme şansı sağlar. Yani 0'dan 5'e kadar.
range(0, 5)

for i in range(0, 5):
    print(i)

# Ekran Çıktısı:
# 0
# 1
# 2
# 3
# 4

for i in range(len("miuul")):
    print(i)

# Ekran Çıktısı:
# 0
# 1
# 2
# 3
# 4

"miuul"[1].upper()      # I


def alternating(string):
    new_string = ""
    # girilen string'in indekslerinde gez.
    for string_index in range(len(string)):
        # index çift ise büyük harfe çevir.
        if string_index % 2 == 0:
            new_string += string[string_index].upper()
        # index tek ise küçük harfe çevir.
        else:
            new_string += string[string_index].lower()
    print(new_string)


alternating("hi my name is john and i am learning python")












