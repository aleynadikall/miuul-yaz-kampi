
# Birleştirme (Join) İşlemleri

import numpy as np
import pandas as pd
m = np.random.randint(1, 30, size=(5, 3))
df1 = pd.DataFrame(m, columns=["var1", "var2", "var3"])
df2 = df1 + 99

# alt alta birleştirmek için concat kullanırız, dataframe'leri de liste şeklinde yollarız.
pd.concat([df1, df2])
#    var1  var2  var3
# 0    12    19     6
# 1     9    29    27
# 2     1    21     6
# 3    20    10     9
# 4    25     9    25
# 0   111   118   105
# 1   108   128   126
# 2   100   120   105
# 3   119   109   108
# 4   124   108   124

pd.concat([df1, df2], ignore_index=True)
#    var1  var2  var3
# 0    12    19     6
# 1     9    29    27
# 2     1    21     6
# 3    20    10     9
# 4    25     9    25
# 5   111   118   105
# 6   108   128   126
# 7   100   120   105
# 8   119   109   108
# 9   124   108   124

# axis değerini 1 yaparsak yan yana birleştirme mümkün olur.

# Merge ile Birleştirme İşlemleri

# Çalışanlar ve hangi departmanda çalıştıkları bilgisi:
df1 = pd.DataFrame({'employees': ['john', 'dennis', 'mark', 'maria'],
                    'group': ['accounting', 'engineering', 'engineering', 'hr']})

# çalışanlar ve çalışmaya başlama tarihleri:
df2 = pd.DataFrame({'employees': ['mark', 'john', 'dennis', 'maria'],
                    'start_date': [2010, 2009, 2014, 2019]})

pd.merge(df1, df2)
# özellikle çalışanlara göre birleştirmesini ifade etmememize rağmen çalışanlara göre birleştirme yaptı.
#   employees        group  start_date
# 0      john   accounting        2009
# 1    dennis  engineering        2014
# 2      mark  engineering        2010
# 3     maria           hr        2019

# on ile neye göre birleştirme yapacağını söyleyebiliriz.
pd.merge(df1, df2, on="employees")
#   employees        group  start_date
# 0      john   accounting        2009
# 1    dennis  engineering        2014
# 2      mark  engineering        2010
# 3     maria           hr        2019

# Amaç: Her çalışanın müdürünün bilgisine erişmek istiyoruz.

df3 = pd.merge(df1, df2)
#   employees        group  start_date
# 0      john   accounting        2009
# 1    dennis  engineering        2014
# 2      mark  engineering        2010
# 3     maria           hr        2019

df4 = pd.DataFrame({'group': ['accounting', 'engineering', 'hr'],
                    'manager': ['Caner', 'Mustafa', 'Berkcan']})

pd.merge(df3, df4)
#   employees        group  start_date  manager
# 0      john   accounting        2009    Caner
# 1    dennis  engineering        2014  Mustafa
# 2      mark  engineering        2010  Mustafa
# 3     maria           hr        2019  Berkcan




