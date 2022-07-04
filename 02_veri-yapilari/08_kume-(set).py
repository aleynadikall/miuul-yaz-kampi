# Küme (Set)
# Değiştirilebilir, sırasız ve eşsizdir, kapsayıcıdır.

# difference(): İki kümenin farkı
set1 = set([1, 3, 5])
set2 = {1, 2, 3}

# set1'de olup set2'de olmayan
set1.difference(set2)       # {5}

# set2'de olup set1'de olmayan
set2.difference(set1)       # {2}

# symmetric_difference(): İki kümede de birbirlerine

