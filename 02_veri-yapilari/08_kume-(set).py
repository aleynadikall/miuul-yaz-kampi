# Küme (Set)
# Değiştirilebilir, sırasız ve eşsizdir, kapsayıcıdır.

# difference(): İki kümenin farkı
set1 = set([1, 3, 5])
set2 = {1, 2, 3}

# set1'de olup set2'de olmayan
set1.difference(set2)       # {5}
set1 - set2

# set2'de olup set1'de olmayan
set2.difference(set1)       # {2}
set2 - set1

# symmetric_difference(): İki kümede de birbirlerine gore olmayanların birleşimi
set1.symmetric_difference(set2)     # {2,5}
set2.symmetric_difference(set1)     # {2,5}

# intersection(): İki kümenin kesişimi
set1 = set([1, 3, 5])
set2 = set([1, 2, 3])
set1.intersection(set2)     # {1, 3}
set2.intersection(set1)     # {1, 3}

set1 & set2    # {1, 3}

# İki kümenin birleşimi: union()
set1.union(set2)        # {1, 2, 3, 5}
set2.union(set1)        # {1, 2, 3, 5}

# isdisjoint(): İki kümenin kesişimi boş mu?
set1 = set([7, 8, 9])
set2 = set([5, 6, 7, 8, 9, 10])

set1.isdisjoint(set2)       # False
set2.isdisjoint(set1)       # False

# issubset(): Bir küme diğer kümenin alt kümesi mi?

set1.issubset(set2)     # True
set2.issubset(set1)     # True


# issuperset(): kapsıyor mu?
set1.issuperset(set2)   # False
set2.issuperset(set1)   # True



