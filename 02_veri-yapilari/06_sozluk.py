# Sözlük (Dictionary)
# Sözlükler key-value çiftleri ile veri tutmayı sağlayan bir veri yapısıdır.
# Değiştirilebilir, sırasız (3.7 sürümünden sonra sıralı özelliği de kazanmıştır.) ve kapsayıcıdır.

dictionary = {"REG": "Regression",
              "LOG": "Logistic Regression",
              "CART": "Classification and Regression"}

# Peki bu key-value çifti ne anlama gelir? Örneğin dictionary içindeki bir tane elemanı seçmek istediğimizde REG keyini
# çağırırsak Regression valuesu gelir. Bu şekilde keyi bu olsun valuesu bu olsun denilerek çiftli yapılarda veri
# tutulabilir. REG ifadesi ile Regression ifadesi arasında pek bir fark şu anlık olmasa da value tarafına veri tipi
# liste olan bir yapı girersek işler farklı olabilir.

dictionary["REG"]       # 'Regression'

dictionary = {"REG": ["RMSE", 10],
              "LOG": ["MSE", 20],
              "CART": ["SSE", 30]}      # Kapsayıcı özelliği: Birden fazla veri tipini tutabildi.

dictionary["REG"]       # ['RMSE', 10]

dictionary = {"REG": 10,
              "LOG": 20,
              "CART": 30}
dictionary["REG"]       # 10

dictionary = {"REG": ["RMSE", 10],
              "LOG": ["MSE", 20],
              "CART": ["SSE", 30]}

# Sözlük içindeki 30 değerine erişmek istediğimizde ise: Sırasız ve Sıralı olmasıyla ilgilidir.
dictionary["CART"][1]       # 30
dictionary["LOG"][0]        # 'MSE'

# Key Sorgulama

"REG" in dictionary     # True

# Key'e Göre Value'ya Erişmek
dictionary.get("REG")       # ['RMSE', 10]

# Değiştirilebilirlik Özelliği:
dictionary["REG"] = ["YSA", 10]
dictionary      # {'REG': ['YSA', 10], 'LOG': ['MSE', 20], 'CART': ['SSE', 30]}

# Tüm Key'lere Erişmek
dictionary.keys()

# Tüm Value'lere Erişmek
dictionary.values()

#Tüm çiftleri Tuple Halinde Listeye Çevirme
dictionary.items()

# Key-Value Değerini Güncellemek
dictionary.update({"REG": 11})
dictionary      # {'REG': 11, 'LOG': ['MSE', 20], 'CART': ['SSE', 30]}

# Yeni Key-Value Eklemek
dictionary.update({"RF": 10})
dictionary      # {'REG': 11, 'LOG': ['MSE', 20], 'CART': ['SSE', 30], 'RF': 10}









