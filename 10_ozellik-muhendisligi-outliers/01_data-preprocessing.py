# FEATURE ENGINEERING & DATA PRE-PROCESSING (Özellik Mühendisliği ve Veri Ön İşleme)

# Veri bilimi alanı birçok farklı uygulamayı da barındırmaktadır. Bu uygulamaların da hemen hemen hepsinde ufak
# istisnalar olsa da verinin önemi oldukça yüksektir. Eğer kötü veri varsa buradan iyi sonuçların çıkması çok
# beklenmeyecek bir durumdur. Dolayısıyla nasıl bir çalışma gerçekleştiriliyorsa gerçekleştirilsin, verinin iyi olması
# gerekmektedir. Bununla beraber özellik mühendisliği değişken mühendisliği kapsamında ham veriden çıkarılabilecek
# birçok olası yeni özellik de söz konusu olacağından sadece iyi veri ile ilgilenmiyoruz. Aslında potansiyel veri ile
# de ilgileniyoruz.

# Bu bölümde neler inceleyeceğiz?
# Outliers (Aykırı Değerler)
# Missing Values (Eksik Değerler)
# Encoding
# Feature Scaling (Özellik Ölçeklendirme)
# Feature Extraction (Özellik Çıkarımı)
# Feature Interactions (Özellik Etkileşimleri)
# En-to-End Application (Uçtan Uca Uygulama)

# Özellik mühendisliği kavramıyla ilgili bir değerlendirme yapalım:
# DİKKAT: Uygulamalı makine öğrenmesi temel olarak değişken mühendisliğidir.
# Applied machine learning is basically feature engineering - Andrew Ng
# Bizim için makine öğrenmesi araçları önemli ancak makine öğrenmesi araçlarını etkili kullanmamızın yolu da değişken
# mühendisliğini iyi anlamaktır. Veriden değişkenler üretmek ve bu değişkenler üzerinde çalışabilmeyi iyi anlamaktır.
# Dolayısıyla bu çerçevede uygulamalı makne öğrenmesinin nasıl feature engiinering ile ilişkili olduğunu birlikte
# gözlemleme imkanı bulacağız.

# Peki özellik mühendisliğinin tanımı nedir?
# Özellikler üzerinde gerçekleştirilen çalışmalardır. Ham veriden değişken üretmektir.

# Veri Ön İşleme: Çalışmalar öncesi verinin uygun hale getirilmesi sürecidir.Peki bunun özellik mühendisliği ile ne
# farkı vardır? Şöyle düşünülebilir, özellik mühendisliği veri ön işleme sürecinin alt başlıklarından birisidir. Yani
# büyük resim veri ön işleme, hazırlığı basamağı vardır. Bunun altında ön işleme işlemleri, bunun da altında özellik
# çıkarımı işlemleri vb. işlemler vardır.

# DİKKAT: Sadece makine öğrenmesi için veri ön işlemesi veya özellik mühendisliği gerekmez. Birçok farklı veri bilimi
# uygulaması kapsamında da bize bu basamaklar gerekiyor olacaktır. Dolayısıyla aslında bu kısımlara çok ciddi hakimiyet
# sağlanması durumunda veri bilimi, derin öğrenme ve makine öğrenmesi kapsamındaki birçok ihtiyacımızı çok rahat bir
# şekilde anlayabiliyor ve çözebiliyor olacağız.






