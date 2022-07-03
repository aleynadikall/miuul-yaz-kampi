# Paket Yönetimi (Package Management)

# Package Management Nedir?
# Paket/modül/kütüphane yönetimi
# Python programını bilgisayarımıza indirip kullanmaya başladığımızda python ile beraber gelen bazı metodlar, fonksiyonlar
# ve modüller vardır. Bunun dışında bazı kaynaklardan da indirilebilecek olan paketler/modüller/kütüphsneler vardır.
# Dış dünyada bu paket/modül/kütüphanelerin indirilmesi kurulması ve python çalışmalarına dahil edilmesi ve bu kütüphanelerin
# bağımlılıklarının yönetilmesi bir iştir. Bu işi yönetenler de package management araçlarıdır. Bunlara bazen paket bazen
# kütüphane bazen modül dendiğini göreceğiz. Neredeyse aynı şeylerdir. Ufak farklılıkları vardır.

# Paket Yönetim Araçları: pip(requirements.txt), pipenv(Pipfile), conda(environment.yaml)
# DİKKAT: conda hem sanal ortam yöneticisi hem de paket yöneticisi olarak kullanılabilmektedir. Yani conda ile hem sanal
# ortam oluşturabiliriz hem de paket indirme paket güncelleme paket silme paket versiyon güncellemeleri yapmak gibi paketleri
# ilgilendiren işlemler de yapabiliriz.
# DİKKAT: Bu tür araçların bizim için sağladığı aslında iki önemli nokta vardır.
# 1- Python dışındaki paketleri indirme kurma vb. işlevler yerine getirmektedirler.
# 2- Bağımlılık yönetimi (dependence management)yapmalarıdır. Yani örneğin bir numpy programını bilgisayarımıza kurduğumuzda
# aslında arka tarafta numpy'ın bağımlı olduğu birçok kütüphane ve versiyon vardır. Bu kütüphaneleri otomatik olarak kurarlar.

# Peki Sanal Ortamlar ile Paket Yönetim Araçları Arasındaki İlişki Nedir?
# Önceden bahsetmiş olduğumuz sanal ortam araçlarından olan venv ve virtualenv psket yönetimi aracı olarak pip'i kullanır.
# conda ve pipenv hem sanal ortam yönetcisi hem de paket yöneticisidirler.
# Sanal ortam oluşturma işimiz ve bunu idare eden bazı araçlarımız var, aynı zamanda paket yönetim araçları var.
# SONUÇ: conda package management ve virtual environment yönetimi için kullanılabilir. pip sadece paket yönetimi için kullanılabilir.
# CONDA > PIP