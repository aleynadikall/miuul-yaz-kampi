# List & Dictionary Comprehensions Uygulamaları

# Uygulama-3

# Amaç key'i string, value'su aşağıdaki gibi bir liste olan sözlük oluşturmak:
# Sadece sayısal değişkenler için yapmak istiyoruz.

# Output
# {'total': ['mean', 'min', 'max', 'var'],
#  'speeding': ['mean', 'min', 'max', 'var'],
#  'alcohol': ['mean', 'min', 'max', 'var'],
#  'not_distracted': ['mean', 'min', 'max', 'var'],
#  'no_previous': ['mean', 'min', 'max', 'var'],
#  'ins_premium': ['mean', 'min', 'max', 'var'],
#  'ins_losses': ['mean', 'min', 'max', 'var']}


import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns
# Index(['total', 'speeding', 'alcohol', 'not_distracted', 'no_previous',
#        'ins_premium', 'ins_losses', 'abbrev'],
#       dtype='object')


# Sadece sayısal değişkenleri bu veri seti üzerinden nasıl seçeriz?


# O objecti yani kategorik değişkenleri ifade eder biz kategorik olmayan değişkenleri istiyoruz.
# Aşağıdaki ifade bize string tipleri değil numerik tipleri getirir.
num_cols = [col for col in df.columns if df[col].dtype != "O"]
num_cols
# ['total',
#  'speeding',
#  'alcohol',
#  'not_distracted',
#  'no_previous',
#  'ins_premium',
#  'ins_losses']

soz = {}
agg_list = ["mean", "min", "max", "sum"]

# DİKKAT: Çok orijinal bir kullanım gerçekleştireceğiz.

# Uzun Yol:
for col in num_cols:
    soz[col] = agg_list

# Yukarıdaki kodda num_cols'da geziyoruz, sözlüğün (soz) key değerine köşeli parantezler ile num_cols'tan gelen
# col(sütun) isimlerini girerken eşittir diyip bunların value bölümlerine sabit bir liste giriyoruz.


soz
# {'total': ['mean', 'min', 'max', 'sum'],
#  'speeding': ['mean', 'min', 'max', 'sum'],
#  'alcohol': ['mean', 'min', 'max', 'sum'],
#  'not_distracted': ['mean', 'min', 'max', 'sum'],
#  'no_previous': ['mean', 'min', 'max', 'sum'],
#  'ins_premium': ['mean', 'min', 'max', 'sum'],
#  'ins_losses': ['mean', 'min', 'max', 'sum']}

# Kısa Yol:
new_dict = {col: agg_list for col in num_cols}
new_dict

# Bu nerede işimize yarayabilir?


df[num_cols].head()
#    total  speeding  alcohol  ...  no_previous  ins_premium  ins_losses
# 0   18.8     7.332    5.640  ...       15.040       784.55      145.08
# 1   18.1     7.421    4.525  ...       17.014      1053.48      133.93
# 2   18.6     6.510    5.208  ...       17.856       899.47      110.35
# 3   22.4     4.032    5.824  ...       21.280       827.34      142.39
# 4   12.0     4.200    3.360  ...       10.680       878.41      165.63


df[num_cols].agg(new_dict)
#            total    speeding  ...   ins_premium   ins_losses
# mean   15.790196    4.998196  ...    886.957647   134.493137
# min     5.900000    1.792000  ...    641.960000    82.750000
# max    23.900000    9.450000  ...   1301.520000   194.780000
# sum   805.300000  254.908000  ...  45234.840000  6859.150000

# DİKKAT: agg() fonksiyonu bizim beklentilerimizi karşılayabilecek akıllı bir fonksiyondur. Eğer agg() fonksiyonuna bu
# şekilde bir sözlük gönderirsek ve agg() fonksiyonunu bu şekilde bir DataFrame'e uygularsak gönderdiğimiz sözlüğün
# içerisindeki değişkenler eğer buradaki DataFrame'de varsa, ki var, bu değişkenleri key bölümünden tutar value bölümüne
# girdiğimiz bütün fonksiyonları gidip bu değişkenleri otomatik olarak uugular.






