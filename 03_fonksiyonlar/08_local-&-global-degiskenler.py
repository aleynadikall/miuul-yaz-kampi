# Lokal & Global Değişkenler (Local & Global Variables)

list_store = [1, 2]
type(list_store)        # list

# Amacı kendisine girilen iki sayıyı çarpmak ve list_store eklemek olan fonksiyonu yazalım.


def add_element(a, b):
    c = a * b       # c local etki alanında burası dışında bir yerde kullanamayız. c Local etki alanından global etki
    # alanını etkiler.
    list_store.append(c)
    print(list_store)


add_element(1, 9)       # [1, 2, 9]






