# Alternating Fonksiyonunun Enumerate ile Yazılması

# Çift indekslerdeki ve tek indekslerdeki stringleri büyütüp küçültme

def alternating_with_enumerate(string):
    new_string = ""
    for i, letter in enumerate(string):
        # enumerate kullanılmazsa len ve range kullanabiliriz ancak enumerate kullanımı daha kolay.
        if i % 2 == 0:
            new_string += letter.upper()
        else:
            new_string += letter.lower()
    print(new_string)


alternating_with_enumerate("hi my name is aleyna and i am learning python")
# Hi mY NaMe iS AlEyNa aNd i aM LeArNiNg pYtHoN





















