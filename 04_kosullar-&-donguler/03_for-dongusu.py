# DÖNGÜLER (Loops)

# for loop

students = ["John", "Mark", "Venessa", "Mariam"]

# Her bir elemana erişmek istiyoruz:
students[0]
students[1]
students[2]

# Hepsine manual şekilde erişmeye çalışmak uzun zamanımızı alır bunun yerine for döngüsü kullanabiliriz.

for student in students:
    print(student)

# Ekran Çıktısı:
# John
# Mark
# Venessa
# Mariam


# Tüm harfleri büyük yazmak istiyoruz:
for student in students:
    print(student.upper())

# Ekran Çıktısı:
# JOHN
# MARK
# VENESSA
# MARIAM


salaries = [1000, 2000, 3000, 4000, 5000]

for salary in salaries:
    print(salary)

# Ekran Çıktısı:
# 1000
# 2000
# 3000
# 4000
# 5000


# Maaşlara %20 zam uygulayalım:
for salary in salaries:
    print(salary * 20 / 100 + salary)

# Ekran Çıktısı:
# 1200.0
# 2400.0
# 3600.0
# 4800.0
# 6000.0

# float olan maaşları iinteger olarak bastıralım.
for salary in salaries:
    print(int(salary * 20 / 100 + salary))

# Ekran Çıktısı:
# 1200
# 2400
# 3600
# 4800
# 6000

# DRY Prensibi: Kendini tekrar etme!


def new_salary(_salary, rate):
    return int(_salary * rate / 100 + _salary)


new_salary(1500, 10)        # 1650
new_salary(2000, 20)        # 2400

# Gayet hızlı şekilde for döngüsü kullanarak tüm maaşlara %10 zam yapabiliriz:
for salary in salaries:
    print(new_salary(salary, 10))

# Ekran Çıktısı
# 1100
# 2200
# 3300
# 4400
# 5500


for salary in salaries:
    if salary > 3000:
        print(new_salary(salary, 10))
    else:
        print(new_salary(salary, 20))

# Ekran Çıktısı:
# 1200
# 2400
# 3600
# 4400
# 5500







