# SANAL ORTAM (VIRTUAL ENVIRONMENT)
# Sanal Ortam Nedir?
# İzole çalışma ortamları oluşturmak için kullanılan araçlardır.
# Farklı çalışmalar için oluşabilecek farklı kütüphane ve versiyon ihtiyaçlarını çalışmalar birbirini etkilemeyecek
# şekilde oluşturma imkanı sağlar.

# Örnek vermek gerekirse bir proje oluşturmak istiyoruz;
# Elimizde python'ın 3.7 numpy'ın 1.16 ve pandas'ın 1.1 versiyonları var.
# Eşzamanlı olarak başka bir projede de çalışmak istiyoruz.
# Elimizde bu sefer python 2.7 numpy 1.14 ve pandas 0.14 versiyonları var.
# Yine başka bir proje için de python 3.8 numpy 1.20 ve pandas 0.19 versiyonları ile çalışılıyor.
# Bu proojeler için sanal ortamlar oluşturabiliriz.

# Başka bir örnek vermek gerekirse pygame kütüphanesi ile Python'da bir oyun yazmak istediğimizi düşünelim;
# Bu durumda pygame bize ython 3 serisi ile çalışamıyorum 2 ile çalışabiliyorum diyecektir.
# Biz de iyi de karşim bizim bütün uygulamalarımız 3 serisi ile çalışıyor senin için 2'ye dönecek halimiz yok ya deriz.
# Conda der ki merhaba.

# Yani kısaca conda ve benzeri araçlar bu durumda devreye girerek bize aynı anda birden fazla ortam oluşturma ve bunların
# bunların üzerinde çalışma imkanı sağlar.

# Conda dışındaki bazı sanal ortam araçları: venv, virtualenv, pipenv.