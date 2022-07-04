# Liste(list)
# Değiştirilebilir, sıralı (index işlemleri yapılabilir) ve kapsayıcı bir veri yapısıdır.

notes = [1, 2, 3, 4]
type(notes)

names = ["a", "b", "v", "d"]
not_nam = [1, 2, 3, "a", "b", True, [1, 2, 3]]  # 7 elemanlık bir listedir. Listenin bu durumu kapsayıcı olmasıyla
# ilişkilidir. Yani içinde birden fazla veri yapısını aynı anda bulundurabilir.

not_nam[0]
not_nam[5]
not_nam[6]  # listeye eriştik ama liste içindeki 2 numaralı elemana nasıl erişiriz.

# Bu şekilde:
not_nam[6][1]
type(not_nam)   # list
type(not_nam[6])    # list
type(not_nam[6][1])     # int
# Liste içindeki elemanlara eriştik bu durum listelerin sıralı olmasıyla ilgili bir durumdur. Yani index işlemleri
# yapılabilirdir.

notes[0] = 99   # Listeler değiştirilebilirdir.
# Listeler hem dlice işlemleri ile hem de index işlemleri ile erişilebilirdir. Bu sebeple kendine yaygın şekilde
# kullanım alanı bulmaktadır.

# Slice şeklinde elemanlara erişme:
not_nam[0:4]

# Liste Metodları (List Methods)

dir(notes)      # en yaygını appenddir.

# len: builtin python function, boyut bilgisi
len(notes)      # 4
len(not_nam)    # 7

# append: eleman ekler
notes       # [99, 2, 3, 4]
notes.append(100)
notes       # [99, 2, 3, 4, 100]

# pop: indexe göre siler
notes.pop(0)
notes       # [2, 3, 4, 100]

# insert: indexe ekler
notes.insert(2, 99)
notes       # [2, 3, 99, 4, 100]