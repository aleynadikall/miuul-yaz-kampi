# break & continue & while

salaries = [1000, 2000, 3000, 4000, 5000]

for salary in salaries:
    if salary == 3000:
        break
    print(salary)

# Ekran Çıktısı:
# 1000
# 2000

for salary in salaries:
    if salary == 3000:
        continue
    print(salary)

# Ekran Çıktısı:
# 1000
# 2000
# 4000
# 5000

# while
number = 1
while number < 5:
    print(number)
    number += 1

# Ekran Çıktısı:
# 1
# 2
# 3
# 4









