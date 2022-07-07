# List & Dictionary Comprehensions Uygulamaları

# Uygulama-1

# Bir Veri Setindeki Değişken İsimlerini Değiştirmek

# before:
# ['total', 'speeding', 'alcohol', 'not_distracted', 'no_previous', 'ins_premium', 'ins_losses', 'abbrev']

# after:
# ['TOTAL', 'SPEEDING', 'ALCOHOL', 'NOT_DISTRACTED', 'NO_PREVIOUS', 'INS_PREMIUM', 'INS_LOSSES', 'ABBREV']


import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

# Ekran Çıktısı:
# Index(['total', 'speeding', 'alcohol', 'not_distracted', 'no_previous',
#        'ins_premium', 'ins_losses', 'abbrev'],
#       dtype='object')


for col in df.columns:
    print(col)

# total
# speeding
# alcohol
# not_distracted
# no_previous
# ins_premium
# ins_losses
# abbrev

for col in df.columns:
    print(col.upper())

# TOTAL
# SPEEDING
# ALCOHOL
# NOT_DISTRACTED
# NO_PREVIOUS
# INS_PREMIUM
# INS_LOSSES
# ABBREV

# Amacımız buydu ancak bunu kalıcı şekilde dataframe'e yansıtmamız gerekiyor.

A = []

for col in df.columns:
    A.append(col.upper())

A
# ['TOTAL',
#  'SPEEDING',
#  'ALCOHOL',
#  'NOT_DISTRACTED',
#  'NO_PREVIOUS',
#  'INS_PREMIUM',
#  'INS_LOSSES',
#  'ABBREV']

# Liste formatında kalıcı şekilde değiştirmiş olduk. (Aşağıdaki atamayı yapmalıyız ki kalıcı değişiklik olabilsin.)

df.columns = A
df.columns
# Index(['TOTAL', 'SPEEDING', 'ALCOHOL', 'NOT_DISTRACTED', 'NO_PREVIOUS',
#        'INS_PREMIUM', 'INS_LOSSES', 'ABBREV'],
#       dtype='object')


# Bunu list comprehensions ile yapalım:

df = sns.load_dataset("car_crashes")

df.columns = [col.upper() for col in df.columns]
df.columns
# Index(['TOTAL', 'SPEEDING', 'ALCOHOL', 'NOT_DISTRACTED', 'NO_PREVIOUS',
#        'INS_PREMIUM', 'INS_LOSSES', 'ABBREV'],
#       dtype='object')




