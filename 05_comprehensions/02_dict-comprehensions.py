# Dict Comprehensions

dictionary = {'a': 1,
              'b': 2,
              'c': 3,
              'd': 4}


# Sözlüğün keys değerlerine erişmek istersek:
dictionary.keys()
# dict_keys(['a', 'b', 'c', 'd'])


# Sözlüğün values değerlerine erişmek istersek:
dictionary.values()
# dict_values([1, 2, 3, 4])


# Eğer item çiftlerine liste formunda ama her bir elemanı tuple olarak ifade edilmiş şekilde ulaşmak istersek:
dictionary.items()
# dict_items([('a', 1), ('b', 2), ('c', 3), ('d', 4)])


# Bu sözlük içerisindeki her bir value'nun karesini almak istiyoruz. Nasıl yapabiliriz?:
{k: v ** 2 for (k, v) in dictionary.items()}
# DİKKAT: Buradan çıkan eleman çiftlerinin key değerleri sabit olacak, value değerlerinin karesini olacak.
# {'a': 1, 'b': 4, 'c': 9, 'd': 16}


# key değerlerini değiştirmek istersek:
{k.upper(): v for (k, v) in dictionary.items()}
# {'A': 1, 'B': 2, 'C': 3, 'D': 4}


# İkisine aynı anda da etki edebiliriz:
{k.upper(): v ** 2 for (k, v) in dictionary.items()}
# {'A': 1, 'B': 4, 'C': 9, 'D': 16}





