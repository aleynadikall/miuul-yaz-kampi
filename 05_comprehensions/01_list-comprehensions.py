# Comprehensions
# Biden fazla satır ve kod ile yapılabilecek işlemleri kolayca istediğimiz çıktı veri yapısına göre tek bir satırda
# gerçekleştirme imkanı sağlayan yapılardır.

# List Comprehensions

salaries = [1000, 2000, 3000, 4000, 5000]


def new_salary(x):
    return x * 20 / 100 + x


for salary in salaries:
    print(new_salary(salary))


# 1200.0
# 2400.0
# 3600.0
# 4800.0
# 6000.0

null_list = []


# zam yapılmış bir maaşları bir listede saklamak istediğimizi düşünelim.
for salary in salaries:
    null_list.append(new_salary(salary))


null_list           # [1200.0, 2400.0, 3600.0, 4800.0, 6000.0]


for salary in salaries:
    if salary > 3000:
        null_list.append(new_salary(salary))
    else:
        null_list.append(new_salary(salary * 2))

null_list
# [2400.0,
#  4800.0,
#  7200.0,
#  4800.0,
#  6000.0]


# Eski yöntemle böyle yapabiliyorduk, peki bunu list comprehensions ile yapmak istersek nasıl yapacağız?

[new_salary(salary * 2) if salary < 3000 else new_salary(salary) for salary in salaries]
# [2400.0, 4800.0, 3600.0, 4800.0, 6000.0]

[salary * 2 for salary in salaries]
# [2000, 4000, 6000, 8000, 10000]


# Maaşı 3000'den olanları 2 ile çarpalım
[salary * 2 for salary in salaries if salary < 3000]
# [2000, 4000]

# Maaşı 3000'den büyük olanlara ne yapacağız?:
# DİKKAT: Eğer comprehensions içinde tek bir if kullanıyorsak yani else ile birlikte kullanmıyorsak bu durumda if sağ
# tarafa yazılır. Eğer else yapısı ile kullanacaksak for bloğu sağ tarafta kalır. if-else bölümü sağ tarafta kalır.
[salary * 2 if salary < 3000 else salary * 0 for salary in salaries]
# [2000, 4000, 0, 0, 0]

# Elimizdeki var olan fonksiyonu bu yapılar içerisinde kullanmak istiyoruz. Nasıl yapacağız?:
[new_salary(salary * 2) if salary < 3000 else salary * 0 for salary in salaries]
# [2400.0, 4800.0, 0, 0, 0]


# Nereye etki etmesini istiyorsak oraya yazabiliriz.
[new_salary(salary * 2) if salary < 3000 else new_salary(salary * 0.2) for salary in salaries]
# [2400.0, 4800.0, 720.0, 960.0, 1200.0]


students = ["John", "Mark", "Venessa", "Mariam"]
student_no = ["John", "Venessa"]

[student.lower() if student in student_no else student.upper() for student in students]
# ['john', 'MARK', 'venessa', 'MARIAM']

# not in ile de kullanabiliriz.
[student.upper() if student not in student_no else student.lower() for student in students]







