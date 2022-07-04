# Demet (Tuple)

# Değiştirilemez, sıralıdır, kapsayıcıdır.

t = ("john", "mark", 1, 2)
t       # ('john', 'mark', 1, 2)

t[0]        # 'john'    Sıralı olduğundan dolayı erişilebilir.
t[0:3]      # ('john', 'mark', 1)   slice işlemi de yapılabilir.

t[0] = 99       # TypeError: 'tuple' object does not support item assignment

# Ancak bir yolu vardır. Listeye çevirip değiştirdik. Sonra tekrar tuple'a çevirdik.
t = list(t)
t[0] = 99
t = tuple(t)
type(t)
# tuple listenin zıttı kardeşidir.

