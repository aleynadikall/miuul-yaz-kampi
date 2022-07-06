# Zip

students = ["John", "Mark", "Venessa", "Mariam"]

departments = ["mathematics", "statistics", "physics", "astronomy"]

ages = [23, 30, 26, 22]

# Buradaki 3 farklı listenin elemanlarını eşlemek istiyoruz. zip bize bu birbirinden farklı şekilde olan listeleri bir
# arada değerlendirme imkanı sağlar.

#genel çıktının liste tipinde olmasını istediğimiz için list fonksiyonunu kullanırız.
list(zip(students, departments, ages))
# [('John', 'mathematics', 23), ('Mark', 'statistics', 30), ('Venessa', 'physics', 26), ('Mariam', 'astronomy', 22)]







