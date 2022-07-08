# Veri Okuma (Reading Data)

import pandas as pd
data = open(r"C:\Users\aleyy\Desktop\miuul-yaz-kampi\07_python-ile-veri-analizi-pandas\datasets\advertising.csv")
data = pd.read_csv(data)
data.head()

#       TV  radio  newspaper  sales
# 1  230.1   37.8       69.2   22.1
# 2   44.5   39.3       45.1   10.4
# 3   17.2   45.9       69.3    9.3
# 4  151.5   41.3       58.5   18.5
# 5  180.8   10.8       58.4   12.9


# Vahit Hoca aşağıdaki şekilde yapıyor ancak bende bu çalışmadı bu yüzden yukarıdaki gibi yaptım:
# df = pd.read_csv("datasets/advertising.csv")
# df.head()

# Eğer farklı bir veri yapısı olursa (örneğin excel) ne yapmalıyız?:
# pd ifadesine ctrl'ye basarak tıklıyoruz, bir döküman (__init__.py) açıldı.
# CTRL + F diyoruz ve çıkan arama bölümüne read_ yazıyoruz. Herhangi bir google araması yapmadan kullanabileceğimiz
# birçok metod geldi.





