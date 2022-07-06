# Enumerate: Otomatik Counter/Indexer ile for loop
# Bir iteratif nesne(liste gibi) içinde gezip elemanlarına işlem uygularken aynı zamanda o elemanların index bilgilerini
# de takip etmek istediğimizde hayat kurtaran bir yapıdır ve genelde derinlemesine bir projenin içerisinde bu problemle
# karşılaşıp nasıl çözülebileceği bile anlaşılamadan uzun zamanlar harcanmasına sebep olabilecek bir problemdir.


students = ["John", "Mark", "Venessa", "Mariam"]

for student in students:
    print(student)

# Ekran Çıktısı:
# John
# Mark
# Venessa
# Mariam

for index, student in enumerate(students):
    print(index, student)

# Ekran Çıktısı:
# 0 John
# 1 Mark
# 2 Venessa
# 3 Mariam

# Index 0'dan başlar ancak değiştirmek istersek değiştirebiliriz:
for index, student in enumerate(students, 1):
    print(index, student)

# Ekran Çıktısı:
# 1 John
# 2 Mark
# 3 Venessa
# 4 Mariam

A = []
B = []

for index, student in enumerate(students):
    if index % 2 == 0:
        A.append(student)
    else:
        B.append(student)

A       # ['John', 'Venessa']
B       # ['Mark', 'Mariam']


