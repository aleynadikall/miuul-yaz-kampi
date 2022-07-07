# List & Dictionary Comprehensions Uygulamaları

# Uygulama-2

# İsminde "INS" olan değişkenlerin başına "FLAG_" diğerlerine "NO_FLAG_" eklemek istiyoruz.

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

df.columns = [col.upper() for col in df.columns]
df.columns

[col for col in df.columns if "INS" in col]
# ['INS_PREMIUM', 'INS_LOSSES']

# Orjinal bir kullanımdır bu kısma dikkat et.
["FLAG_" + col for col in df.columns if "INS" in col]
# ['FLAG_INS_PREMIUM', 'FLAG_INS_LOSSES']


["FLAG_" + col if "INS" in col else "NO_FLAG_" for col in df.columns]
# ['NO_FLAG_',
#  'NO_FLAG_',
#  'NO_FLAG_',
#  'NO_FLAG_',
#  'NO_FLAG_',
#  'FLAG_INS_PREMIUM',
#  'FLAG_INS_LOSSES',
#  'NO_FLAG_']


# Kalıcı hale getirelim:
df.columns = ["FLAG_" + col if "INS" in col else "NO_FLAG_" for col in df.columns]
df.columns
# Index(['TOTAL', 'SPEEDING', 'ALCOHOL', 'NOT_DISTRACTED', 'NO_PREVIOUS',
#        'INS_PREMIUM', 'INS_LOSSES', 'ABBREV'],
#       dtype='object')


