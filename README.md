# Lesson-Program-Project-with-Graph-Coloring
	Bu projemizde Python tabanlı framework olan Flask üzerinden arayüz tasarladık ve çizge renklendirme algoritması ile bir sınıf için ders programı oluşturduk.

	Bu projenin geliştirilme aşamasında python yazılım dili , HTML , CSS ,Bootstrap , MySQL gibi çeşitli teknolojileri kullandık.Arayüz oluşturmak için çeşitli algortimaların yazımı için Python yazılım dilinin Flask kütüphanesini kullandık.Arayüz düzenlemesi için HTML, CSS ve Bootstrap’i ; çeşitli veritabanı işlemleri için MYSQL kullandık.

#	ARAYÜZ TASARIMI

	ANA SAYFA: Projenin bu sayfasında templates klasörü içindeki index.html dosyasında kullanılan html, css kodları ile python sayfasında “/” endpointine giden bir sayfa tasarımı yapılmıştır.

![Ana Sayfa](https://github.com/AliEmirTuran/Lesson-Program-Project-with-Graph-Coloring/assets/89272211/976d78d1-832e-4355-b931-ed8a1631b0fd)

	DERSLER: Projemizin bu sayfasında templates klasörü içindeki lessons.html dosyasında kullanılan html , css kodları ile tasarım yapılmıştır. Python dosyasında tasarlanan “/lessons” endpoint’i ile bu sayfaya erişilmektedir.
 
	DERS PROGRAMI: Projemizin bu sayfasında isterlerde bulunan basit tablo tasarımını ve ders programı şablon oluşturmayı tasarladık.Proje detayındaki çizge renklendirme algoritmasını kullanmaya çalıştık.Sayfa tasarımında HTML ve CSS kullandık.Python sayfasında çeşitli fonksiyonlar ve değişkenler ile tablomuza render ettik.Bu sayfa “/program” endpoint’ini kullanmaktadır.
 
	ÖĞRETMENLER: Projemizin bu sayfasında veritabanımızda bulunan teachers tablosundaki verileri çeşitli sql sorguları ile teachers.html sayfasında oluşturulan tablolara yerleştirdik.Bu sayfaya “/teachers” endpointi ile ulaşılmaktadır.
 

	ÖĞRETMEN EKLE: Post işlemi ile veritabanına yazılan Insert sorgusu kullanılarak teachersadd.html sayfasında tasarlanan form yardımıyla öğretmen ekleme işlemi gerçekleşmektedir.

 

	Benzer işlemler ile kısıtlar ve kısıt ekleme sayfaları da oluşturulmuştur.
 

 
	VERİTABANI TASARIMI: MySQL üzerinde tasarladığımız ilişkisel veritabanında normalizasyon kurallarına dikkat ederek oluşturduğumuz tablolar ile çeşitli verileri tablolarımızda tuttuk.Veritabanının projeye entegrasyonu aşamasında PHPMYADMİN kullanılmıştır.

 
