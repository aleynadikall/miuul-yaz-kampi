#  UYGULAMA: Mülakat Sorusu: DICTIONARY COMPREHENSIONS

# Amaç: Çift sayıların karesi alınarak bir sözlüğe eklenmek istenmektedir.
# Yani tek değerlere dokunmayacağız.
# Key'ler orjinal değerler value'lar ise değiştirilmiş değerler olacak.


# 0'dan 10'a kadar sayıları oluşturalım:
numbers = range(10)

new_dict = {}


for n in numbers:
    if n % 2 == 0:
        new_dict[n] = n ** 2

new_dict        # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}


new_dict = {}

new_dict = {n: n ** 2 for n in numbers if n % 2 == 0}
new_dict
# {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}





