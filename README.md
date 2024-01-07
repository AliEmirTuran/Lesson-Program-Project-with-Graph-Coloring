# Lesson-Program-Project-with-Graph-Coloring
	Bu projemizde Python tabanlı framework olan Flask üzerinden arayüz tasarladık ve çizge renklendirme algoritması ile bir sınıf için ders programı oluşturduk.

	Bu projenin geliştirilme aşamasında python yazılım dili , HTML , CSS ,Bootstrap , MySQL gibi çeşitli teknolojileri kullandık.Arayüz oluşturmak için çeşitli algortimaların yazımı için Python yazılım dilinin Flask kütüphanesini kullandık.Arayüz düzenlemesi için HTML, CSS ve Bootstrap’i ; çeşitli veritabanı işlemleri için MYSQL kullandık.

#	ARAYÜZ TASARIMI

	ANA SAYFA: Projenin bu sayfasında templates klasörü içindeki index.html dosyasında kullanılan html, css kodları ile python sayfasında “/” endpointine giden bir sayfa tasarımı yapılmıştır.

![Ana Sayfa](https://github.com/AliEmirTuran/Lesson-Program-Project-with-Graph-Coloring/assets/89272211/976d78d1-832e-4355-b931-ed8a1631b0fd)

	DERSLER: Projemizin bu sayfasında templates klasörü içindeki lessons.html dosyasında kullanılan html , css kodları ile tasarım yapılmıştır. Python dosyasında tasarlanan “/lessons” endpoint’i ile bu sayfaya erişilmektedir.

![Dersler](https://github.com/AliEmirTuran/Lesson-Program-Project-with-Graph-Coloring/assets/89272211/8ef7f29c-e82a-47a4-9e1e-8b0e1a811d0e)
 
	DERS PROGRAMI: Projemizin bu sayfasında isterlerde bulunan basit tablo tasarımını ve ders programı şablon oluşturmayı tasarladık.Proje detayındaki çizge renklendirme algoritmasını kullanmaya çalıştık.Sayfa tasarımında HTML ve CSS kullandık.Python sayfasında çeşitli fonksiyonlar ve değişkenler ile tablomuza render ettik.Bu sayfa “/program” endpoint’ini kullanmaktadır.

![Ders Programı](https://github.com/AliEmirTuran/Lesson-Program-Project-with-Graph-Coloring/assets/89272211/42afc14d-73bb-47fc-aa48-8f30a81f4328)
 
	ÖĞRETMENLER: Projemizin bu sayfasında veritabanımızda bulunan teachers tablosundaki verileri çeşitli sql sorguları ile teachers.html sayfasında oluşturulan tablolara yerleştirdik.Bu sayfaya “/teachers” endpointi ile ulaşılmaktadır.

 ![Öğretmenler](https://github.com/AliEmirTuran/Lesson-Program-Project-with-Graph-Coloring/assets/89272211/c7bcbb14-79aa-435b-9907-5621f9bd4e7d)

	ÖĞRETMEN EKLE: Post işlemi ile veritabanına yazılan Insert sorgusu kullanılarak teachersadd.html sayfasında tasarlanan form yardımıyla öğretmen ekleme işlemi gerçekleşmektedir.

 ![Öğretmen Ekleme](https://github.com/AliEmirTuran/Lesson-Program-Project-with-Graph-Coloring/assets/89272211/68d3e035-9bcf-48ba-88a6-6d0ee9d077ba)

	Benzer işlemler ile kısıtlar ve kısıt ekleme sayfaları da oluşturulmuştur.
![Kısıtlar](https://github.com/AliEmirTuran/Lesson-Program-Project-with-Graph-Coloring/assets/89272211/c9b692f9-07b2-4426-8386-f71676035a5f)

![Ksııt Ekleme](https://github.com/AliEmirTuran/Lesson-Program-Project-with-Graph-Coloring/assets/89272211/84f39024-1a54-4bac-935b-15cd87a09523)
 

 
	VERİTABANI TASARIMI: MySQL üzerinde tasarladığımız ilişkisel veritabanında normalizasyon kurallarına dikkat ederek oluşturduğumuz tablolar ile çeşitli verileri tablolarımızda tuttuk.Veritabanının projeye entegrasyonu aşamasında PHPMYADMİN kullanılmıştır.

![Veritabanı](https://github.com/AliEmirTuran/Lesson-Program-Project-with-Graph-Coloring/assets/89272211/23d63489-5243-4630-b47f-7dcf43f0c96d)

 
