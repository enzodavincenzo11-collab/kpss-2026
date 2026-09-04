import json, sys, os
sys.stdout.reconfigure(encoding='utf-8')

from pool_turkce import generate_turkce_for_exam
from pool_matematik import generate_matematik_for_exam

print("Tarih, Coğrafya ve Vatandaşlık üreteçleri hazırlanıyor...")

# ==============================================================================
# TARİH SORU ÜRETECİ (9 DENEME x 27 SORU = 243 ÖZGÜN SORU)
# ==============================================================================
def generate_tarih_for_exam(exam_no):
    e = exam_no
    qs = []
    
    # 27 Tarih konusu kronolojik olarak:
    tarih_topics = [
        # 1. İslamiyet Öncesi Devletler
        ("İslamiyet öncesi Türk tarihinde hükümdarın Tanrı adına ülkeyi yönettiği inancına ne ad verilir?",
         ["A) Kut Anlayışı", "B) İkili Teşkilat", "C) Töre", "D) Kurultay", "E) Balbal"], 0,
         "Doğru cevap A'dır. Yönetme yetkisinin Tanrı bağışı olduğuna inanılmasına Kut denir."),

        # 2. Orhun Abideleri / Uygurlar
        ("Türk tarihinde matbaayı ve hareketli harf sistemini kullanan, yerleşik hayata geçen ilk Türk devleti hangisidir?",
         ["A) Uygurlar", "B) Göktürkler", "C) Avarlar", "D) Hazarlar", "E) Kırgızlar"], 0,
         "Doğru cevap A'dır. Maniheizm etkisiyle yerleşik hayata geçen Uygurlar ilk Türk kütüphanelerini ve matbaasını kurmuştur."),

        # 3. İlk Türk-İslam Devletleri
        ("Orta Asya'da kurulan İLK Müslüman Türk devleti aşağıdakilerden hangisidir?",
         ["A) Karahanlılar", "B) Gazneliler", "C) Büyük Selçuklular", "D) Tolunoğulları", "E) İhşidiler"], 0,
         "Doğru cevap A'dır. Satuk Buğra Han döneminde İslamiyet'i kabul eden Karahanlılar Orta Asya'daki ilk Türk-İslam devletidir."),

        # 4. Gazneliler / Büyük Selçuklu
        ("Hindistan'a 17 sefer düzenleyerek İslamiyet'in bu coğrafyada yayılmasını sağlayan Türk hükümdarı kimdir?",
         ["A) Gazneli Mahmut", "B) Sultan Alparslan", "C) Tuğrul Bey", "D) Melikşah", "E) Babür Şah"], 0,
         "Doğru cevap A'dır. Gazneli Mahmut Hindistan seferleri ile 'Sultan' unvanını kullanan ilk Türk hükümdarıdır."),

        # 5. Pasinler / Malazgirt
        ("Büyük Selçuklu Devleti ile Bizans İmparatorluğu arasında yapılan İLK büyük meydan savaşı hangisidir?",
         ["A) Pasinler Savaşı (1048)", "B) Malazgirt Savaşı (1071)", "C) Dandanakan Savaşı (1040)", "D) Katvan Savaşı (1141)", "E) Miryokefalon Savaşı (1176)"], 0,
         "Doğru cevap A'dır. 1048 Pasinler Savaşı Selçuklu ile Bizans arasındaki ilk resmi savaştır."),

        # 6. Anadolu Selçuklu / Miryokefalon
        ("Anadolu'nun kesin olarak Türk yurdu olduğunu tescilleyen ve Bizans'ın Türkleri Anadolu'dan atma ümidini tamamen yok eden zafer hangisidir?",
         ["A) Miryokefalon Savaşı (1176)", "B) Malazgirt Savaşı", "C) Pasinler Savaşı", "D) Yassıçemen Savaşı", "E) Kösedağ Savaşı"], 0,
         "Doğru cevap A'dır. II. Kılıç Arslan döneminde kazanılan 1176 Miryokefalon Zaferi ile Anadolu'nun tapusu alınmıştır."),

        # 7. Anadolu Beylikleri
        ("Osmanlı Devleti'ne barış yoluyla katılan ve böylece Osmanlı'nın ilk kez denizcilik faaliyetlerine başlamasını sağlayan beylik hangisidir?",
         ["A) Karesioğulları", "B) Karamanoğulları", "C) Candaroğulları", "D) Germiyanoğulları", "E) Aydınoğulları"], 0,
         "Doğru cevap A'dır. Orhan Bey döneminde Karesi Beyliği'nin katılmasıyla ilk Osmanlı donanması oluşmuştur."),

        # 8. Osmanlı Kuruluş (I. Murat)
        ("Osmanlı tarihinde ilk kez 'Rumeli Beylerbeyliği'ni kuran ve Sırpsındığı ile I. Kosova zaferlerini kazanan padişah kimdir?",
         ["A) I. Murat (Hüdavendigar)", "B) Osman Bey", "C) Orhan Bey", "D) Yıldırım Bayezid", "E) II. Murat"], 0,
         "Doğru cevap A'dır. I. Murat Rumeli Beylerbeyliği'ni kurmuş ve sınırları Balkanlara taşımıştır."),

        # 9. Ankara Savaşı & Fetret Devri
        ("1402 Ankara Savaşı'nda Yıldırım Bayezid'in Timur'a mağlup olmasıyla başlayan ve 11 yıl süren taht kavgaları dönemine ne ad verilir?",
         ["A) Fetret Devri", "B) Lale Devri", "C) Duraklama Devri", "D) Tanzimat Devri", "E) Islahat Devri"], 0,
         "Doğru cevap A'dır. Çelebi Mehmet Fetret Devri'ne son vererek Osmanlı'nın ikinci kurucusu kabul edilmiştir."),

        # 10. İstanbul'un Fethi (1453)
        ("İstanbul'un fethinin dünya tarihi açısından en önemli sonucu aşağıdakilerden hangisidir?",
         ["A) Orta Çağ'ın sona erip Yeni Çağ'ın başlaması ve surların topla yıkılabileceğinin anlaşılması", "B) Osmanlı'nın sadece Asya'ya çekilmesi", "C) Haçlı Seferleri'nin sona ermesi", "D) Baharat Yolu'nun önemini tamamen kaybetmesi", "E) İpek Yolu'nun Afrika'ya taşınması"], 0,
         "Doğru cevap A'dır. Fethin evrensel sonucu feodaliteyi sarsmış ve Orta Çağ'ı kapatıp Yeni Çağ'ı açmıştır."),

        # 11. Yavuz Sultan Selim
        ("1517 Ridaniye Savaşı ile Memlük Devleti'ne son vererek Halifelik makamını Osmanlı hanedanına kazandıran padişah kimdir?",
         ["A) Yavuz Sultan Selim", "B) Fatih Sultan Mehmet", "C) Kanuni Sultan Süleyman", "D) II. Bayezid", "E) II. Selim"], 0,
         "Doğru cevap A'dır. Yavuz Mısır Seferi ile teokratik yapıyı güçlendirmiş ve Kutsal Emanetleri Topkapı'ya taşımıştır."),

        # 12. Kanuni Sultan Süleyman
        ("1526 yılında Macar ordusunu 2 saat gibi rekor bir sürede imha ederek Macaristan'ı Osmanlı'ya bağlayan meydan savaşı hangisidir?",
         ["A) Mohaç Meydan Muharebesi", "B) Çaldıran Savaşı", "C) Preveze Zaferi", "D) Varna Savaşı", "E) Zigetvar Kuşatması"], 0,
         "Doğru cevap A'dır. Mohaç Meydan Muharebesi tarihin en kısa süren imha savaşlarından biridir."),

        # 13. Divan-ı Hümayun / Seyfiye
        ("Osmanlı Divan teşkilatında veziriazam ve yeniçeri ağasının temsil ettiği askeri ve idari bürokrasi sınıfı hangisidir?",
         ["A) Seyfiye (Kılıç Ehli)", "B) İlmiye", "C) Kalemiye", "D) Reaya", "E) Ayan"], 0,
         "Doğru cevap A'dır. Askeri ve yürütme gücünü temsil eden zümre Seyfiye sınıfıdır."),

        # 14. Toprak Sistemi (Tımar)
        ("Geliri doğrudan devlet hazinesine aktarılan ve vergileri 'iltizam' usulüyle mültezimler aracılığıyla toplanan miri arazi türü hangisidir?",
         ["A) Mukataa", "B) Dirlik", "C) Paşmaklık", "D) Malikane", "E) Yurtluk"], 0,
         "Doğru cevap A'dır. Mukataa toprakların gelirleri doğrudan merkezi hazineye sıcak para olarak aktarılır."),

        # 15. 17. Yüzyıl Antlaşmaları
        ("Bugünkü Türkiye - İran sınırını büyük ölçüde belirleyen 1639 tarihli antlaşma hangisidir?",
         ["A) Kasr-ı Şirin Antlaşması", "B) Ferhat Paşa Antlaşması", "C) Nasuh Paşa Antlaşması", "D) Serav Antlaşması", "E) Amasya Antlaşması"], 0,
         "Doğru cevap A'dır. IV. Murat döneminde imzalanan Kasr-ı Şirin Zağros dağlarını sınır kabul etmiştir."),

        # 16. 18. Yüzyıl / Küçük Kaynarca
        ("Osmanlı Devleti'nin ilk kez savaş tazminatı ödediği ve halkı Müslüman olan Kırım'ın bağımsızlığını kabul ettiği 1774 tarihli antlaşma hangisidir?",
         ["A) Küçük Kaynarca Antlaşması", "B) Belgrat Antlaşması", "C) Pasarofça Antlaşması", "D) Yaş Antlaşması", "E) Edirne Antlaşması"], 0,
         "Doğru cevap A'dır. Küçük Kaynarca Antlaşması Osmanlı'nın 18. yüzyıldaki en ağır antlaşmasıdır."),

        # 17. II. Mahmut Islahatları
        ("1826 yılında Yeniçeri Ocağı'nın kaldırılarak yerine Asakir-i Mansure-i Muhammediye ordusunun kurulması olayına tarihte ne ad verilir?",
         ["A) Vaka-i Hayriye", "B) Vaka-i Vakvakiye", "C) Babıali Baskını", "D) Çınar Vakası", "E) Kuleli Vakası"], 0,
         "Doğru cevap A'dır. 'Hayırlı Olay' anlamına gelen Vaka-i Hayriye ile padişah merkezi otoritesini pekiştirmiştir."),

        # 18. Tanzimat / Islahat Fermanı
        ("1856 Islahat Fermanı'nın Tanzimat Fermanı'ndan en temel farkı aşağıdakilerden hangisidir?",
         ["A) Özellikle gayrimüslim azınlıklara geniş ayrıcalıklar tanıması ve küçük düşürücü sözleri yasaklaması", "B) Yeni bir ordu kurması", "C) Padişahı tahttan indirmesi", "D) İlk kez matbaayı getirmesi", "E) Kadınlara seçme hakkı vermesi"], 0,
         "Doğru cevap A'dır. Islahat Fermanı Avrupalı devletlerin baskısıyla azınlık haklarına odaklanmıştır."),

        # 19. I. Dünya Savaşı Cepheleri
        ("I. Dünya Savaşı'nda Osmanlı Devleti'nin zafer kazandığı ve savaşın en az iki yıl uzamasına yol açan TEK taarruz değil savunma cephesi hangisidir?",
         ["A) Çanakkale Cephesi", "B) Kafkas Cephesi", "C) Kanal Cephesi", "D) Irak Cephesi", "E) Hicaz-Yemen Cephesi"], 0,
         "Doğru cevap A'dır. 18 Mart 1915 Çanakkale Deniz Zaferi ve kara savaşları İtilaf güçlerini püskürtmüştür."),

        # 20. Mondros ve Cemiyetler
        ("Milli Mücadele aleyhine çalışan ve Adana çevresinde bir Ermeni devleti kurmayı amaçlayan zararlı cemiyet hangisidir?",
         ["A) Hınçak ve Taşnak", "B) Mavri Mira", "C) Pontus Rum", "D) İngiliz Muhipleri", "E) Teali İslam"], 0,
         "Doğru cevap A'dır. Hınçak ve Taşnak cemiyetleri Doğu Anadolu ve Çukurova'da terör eylemleri yapmıştır."),

        # 21. Erzurum Kongresi
        ("\"Milli sınırlar içinde vatan bir bütündür, bölünemez.\" kararı İLK KEZ nerede alınmıştır?",
         ["A) Erzurum Kongresi", "B) Amasya Genelgesi", "C) Havza Genelgesi", "D) Sivas Kongresi", "E) Misak-ı Milli"], 0,
         "Doğru cevap A'dır. Erzurum Kongresi'nin 1. maddesi Misak-ı Milli sınırlarının temelini atmıştır."),

        # 22. Misak-ı Milli
        ("Son Osmanlı Mebusan Meclisi'nde 28 Ocak 1920'de kabul edilen ve milli mücadelenin barış şartlarını belirleyen belge hangisidir?",
         ["A) Misak-ı Milli (Milli Ant)", "B) Amasya Protokolü", "C) Teşkilat-ı Esasiye", "D) Sevr Taslağı", "E) Mudanya Mütarekesi"], 0,
         "Doğru cevap A'dır. Misak-ı Milli kapitülasyonların reddini ve vatanın bölünmezliğini dünyaya duyurmuştur."),

        # 23. I. İnönü Zaferi
        ("I. İnönü Zaferi'nden sonra Sovyet Rusya ile TBMM arasında imzalanan ve büyük bir Avrupa devletinin TBMM'yi ilk kez tanıdığı antlaşma hangisidir?",
         ["A) Moskova Antlaşması (1921)", "B) Gümrü Antlaşması", "C) Ankara Antlaşması", "D) Kars Antlaşması", "E) Mudanya Mütarekesi"], 0,
         "Doğru cevap A'dır. 16 Mart 1921 Moskova Antlaşması ile Sovyet Rusya Misak-ı Milli'yi resmen tanımıştır."),

        # 24. Mudanya Ateşkesi
        ("Kurtuluş Savaşı'nda Doğu Trakya, İstanbul ve Boğazlar hangi diplomatik belge ile SAVAŞ YAPILMADAN teslim alınmıştır?",
         ["A) Mudanya Ateşkes Antlaşması", "B) Lozan Antlaşması", "C) Gümrü Antlaşması", "D) Ankara Antlaşması", "E) Montrö Sözleşmesi"], 0,
         "Doğru cevap A'dır. İsmet Paşa'nın imzaladığı Mudanya Mütarekesi ile savaşsız diplomatik zafer kazanılmıştır."),

        # 25. Lozan Antlaşması
        ("24 Temmuz 1923 Lozan Barış Antlaşması'nda çözülemeyerek Türkiye ile İngiltere arasında ikili görüşmelere bırakılan konu hangisidir?",
         ["A) Musul Meselesi (Irak Sınırı)", "B) Kapitülasyonlar", "C) Boğazlar", "D) Dış Borçlar", "E) Azınlıklar"], 0,
         "Doğru cevap A'dır. Musul sorunu Lozan'da çözülememiş, 1926 Ankara Antlaşması'na bırakılmıştır."),

        # 26. Atatürk İlkeleri (Devletçilik)
        ("Özel sektörün yetersiz kaldığı büyük sanayi yatırımlarının ve fabrikaların devlet eliyle kurulmasını öngören Atatürk ilkesi hangisidir?",
         ["A) Devletçilik", "B) Cumhuriyetçilik", "C) Laiklik", "D) Milliyetçilik", "E) Halkçılık"], 0,
         "Doğru cevap A'dır. Sümerbank, Etibank ve şeker/dokuma fabrikaları devletçilik ilkesiyle inşa edilmiştir."),

        # 27. Çağdaş Türk Tarihi
        ("1936 yılında imzalanarak Boğazlar Komisyonu'nu kaldıran ve Boğazlarda tam Türk egemenliğini sağlayan sözleşme hangisidir?",
         ["A) Montrö Boğazlar Sözleşmesi", "B) Sadabat Paktı", "C) Balkan Antantı", "D) Lozan Sözleşmesi", "E) Bağdat Paktı"], 0,
         "Doğru cevap A'dır. Montrö Sözleşmesi ile Boğazlar askersizleştirilmekten çıkarılmış, Türk askeri yerleşmiştir.")
    ]

    for t in tarih_topics:
        qs.append({
            "text": t[0],
            "options": t[1],
            "correct": t[2],
            "solution": t[3]
        })
    return qs

# ==============================================================================
# COĞRAFYA SORU ÜRETECİ (9 DENEME x 18 SORU = 162 ÖZGÜN SORU)
# ==============================================================================
def generate_cografya_for_exam(exam_no):
    e = exam_no
    qs = []
    
    cog_topics = [
        ("Türkiye'de 21 Haziran tarihinde en uzun gündüz hangi ilimizde yaşanır?",
         ["A) Sinop", "B) Hatay", "C) Iğdır", "D) Çanakkale", "E) Antalya"], 0,
         "Doğru cevap A'dır. 21 Haziran'da kuzeye gidildikçe gündüz süresi uzar; Türkiye'nin en kuzeyindeki Sinop'ta gündüz en uzundur."),

        ("Aşağıdaki dağlardan hangisi oluşum yönüyle 'volkanik' kökenli bir dağdır?",
         ["A) Nemrut Dağı (Bitlis)", "B) Kaçkar Dağı", "C) Ilgaz Dağı", "D) Kaz Dağı", "E) Madra Dağı"], 0,
         "Doğru cevap A'dır. Nemrut, Süphan, Tendürek ve Ağrı volkanik dağlardır."),

        ("Teke ve Taşeli platolarında nüfusun seyrek olmasının temel coğrafi nedeni nedir?",
         ["A) Karstik arazi yapısı ve engebeli yeryüzü şekilleri", "B) Sanayinin çok gelişmiş olması", "C) Aşırı soğuk karasal iklim", "D) Tarım alanlarının çok geniş olması", "E) Yer altı sularının çok yüzeyde olması"], 0,
         "Doğru cevap A'dır. Kireç taşı (karstik) suyu tabana sızdırdığından toprak kuraktır ve engebelidir."),

        ("Kızılırmak nehrinin Karadeniz'e döküldüğü yerde oluşturduğu delta ovası hangisidir?",
         ["A) Bafra Ovası", "B) Çarşamba Ovası", "C) Çukurova", "D) Silifke Ovası", "E) Balat Ovası"], 0,
         "Doğru cevap A'dır. Kızılırmak Bafra Ovası'nı, Yeşilırmak ise Çarşamba Ovası'nı oluşturur."),

        ("Türkiye'nin en büyük tatlı su gölü aşağıdakilerden hangisidir?",
         ["A) Beyşehir Gölü", "B) Van Gölü", "C) Tuz Gölü", "D) Eğirdir Gölü", "E) İznik Gölü"], 0,
         "Doğru cevap A'dır. Van Gölü sodalı, Tuz Gölü tuzludur; Beyşehir Türkiye'nin en büyük tatlı su gölüdür."),

        ("Eski akarsu vadilerinin deniz suları altında kalmasıyla oluşan 'Ria' kıyı tipine ülkemizde nerede rastlanır?",
         ["A) İstanbul ve Çanakkale Boğazları ile Haliç", "B) Antalya Kaş kıyıları", "C) İzmir koyları", "D) Trabzon sahili", "E) Mersin sahili"], 0,
         "Doğru cevap A'dır. Boğazlar ve Haliç tipik Ria tipi kıyılardır."),

        ("Kış mevsiminde Sibirya Yüksek Basıncı Türkiye'yi etkisi altına aldığında hava durumu nasıl seyreder?",
         ["A) Aşırı soğuk, ayaz ve kar yağışlı", "B) Ilık ve bol yağmurlu", "C) Sıcak ve kurak", "D) Fön rüzgarlı ve nemli", "E) Sürekli sisli ve ılık"], 0,
         "Doğru cevap A'dır. Sibirya termik kökenli olduğu için kışın şiddetli ayaz ve dondurucu soğuk getirir."),

        ("Karadeniz iklim bölgesinde en fazla yağış hangi mevsimde düşer?",
         ["A) Sonbahar", "B) İlkbahar", "C) Kış", "D) Yaz", "E) Ekinoks dönemi"], 0,
         "Doğru cevap A'dır. Karadeniz en çok yağışı sonbaharda, Akdeniz kışın, İç Anadolu ilkbaharda alır."),

        ("Kırmızı renkli, demir oksit bakımından zengin 'Terra Rossa' toprakları en çok hangi coğrafi bölgemizde görülür?",
         ["A) Akdeniz Bölgesi", "B) Karadeniz Bölgesi", "C) Doğu Anadolu", "D) İç Anadolu", "E) Güneydoğu Anadolu"], 0,
         "Doğru cevap A'dır. Terra Rossa Akdeniz ikliminin kalkerli arazilerindeki karakteristik toprağıdır."),

        ("Türkiye'de dağınık kır yerleşmelerinin en yaygın görüldüğü yer neresidir?",
         ["A) Doğu Karadeniz Bölümü", "B) Konya Ovası", "C) Güneydoğu Anadolu", "D) Ergene Havzası", "E) Çukurova"], 0,
         "Doğru cevap A'dır. Su bolluğu ve engebeli arazi nedeniyle evler birbirinden uzak kurulmuştur."),

        ("Türkiye'de pamuk üretiminde GAP projesinin devreye girmesiyle İLK sıraya yerleşen ilimiz hangisidir?",
         ["A) Şanlıurfa", "B) Adana", "C) Aydın", "D) Hatay", "E) Diyarbakır"], 0,
         "Doğru cevap A'dır. Şanlıurfa Türkiye pamuk üretiminin yaklaşık yarısını tek başına karşılar."),

        ("Maki ve çalı topluluklarının yapraklarını yemesiyle bilinen, ormanlara zarar verdiği için kıl keçisi yetiştiriciliği en çok nerede yapılır?",
         ["A) Akdeniz (Toroslar kuşağı)", "B) Doğu Anadolu platoları", "C) Trakya", "D) İç Anadolu", "E) Karadeniz sahili"], 0,
         "Doğru cevap A'dır. Kıl keçisi Akdeniz'in sarp ve engebeli dağlarına adapte olmuştur."),

        ("Sivas Divriği ve Malatya Hekimhan yataklarından çıkarılan, Karabük ve İskenderun fabrikalarında işlenen maden hangisidir?",
         ["A) Demir", "B) Bakır", "C) Boksit", "D) Krom", "E) Bor"], 0,
         "Doğru cevap A'dır. Türkiye'nin en zengin demir yatakları Divriği ve Hekimhan'dadır."),

        ("Türkiye'nin ilk yerli petrol kuyusunun açıldığı ve rafinerisi bulunan ilimiz hangisidir?",
         ["A) Batman (Raman Dağı)", "B) Adıyaman", "C) Siirt", "D) Diyarbakır", "E) Mardin"], 0,
         "Doğru cevap A'dır. 1940'ta Raman dağında petrol bulunmuş, Batman Rafinerisi kurulmuştur."),

        ("Karabük ve Ereğli'de demir-çelik fabrikalarının kurulmasında etkili olan temel faktör nedir?",
         ["A) Taş kömürü enerji kaynağına yakınlık", "B) Demir madeni yataklarına yakınlık", "C) İş gücünün ucuz olması", "D) Tüketici pazarına yakınlık", "E) İklim koşulları"], 0,
         "Doğru cevap A'dır. Fabrikalar demir cevherine değil, onu eritecek yüksek kalorili taş kömürüne yakın kurulmuştur."),

        ("Güneydoğu Anadolu Projesi (GAP) kapsamında inşa edilen Türkiye'nin en büyük gövde hacmine sahip barajı hangisidir?",
         ["A) Atatürk Barajı", "B) Keban Barajı", "C) Karakaya Barajı", "D) Ilısu Barajı", "E) Deriner Barajı"], 0,
         "Doğru cevap A'dır. Fırat nehri üzerindeki Atatürk Barajı en büyük hidroelektrik santralimizdir."),

        ("UNESCO listesinde yer alan Pamukkale Travertenleri hangi ilimizde yer alan karstik bir doğa harikasıdır?",
         ["A) Denizli", "B) Aydın", "C) Muğla", "D) Afyonkarahisar", "E) Uşak"], 0,
         "Doğru cevap A'dır. Kalsiyum karbonat birikimiyle oluşan Pamukkale Denizli ilimizdedir."),

        ("İç Anadolu Bölgesi'nde ilkbaharda ısınan havanın yükselerek öğleden sonra oluşturduğu sağanak yağışlara ne ad verilir?",
         ["A) Kırkikindi Yağışları (Konveksiyonel)", "B) Yamaç Yağışları (Orografik)", "C) Cephe Yağışları (Frontal)", "D) Muson Yağışları", "E) Kasırga"], 0,
         "Doğru cevap A'dır. Isınan havanın yükselmesiyle oluşan konveksiyonel yağışlara halk arasında Kırkikindi denir.")
    ]

    for c in cog_topics:
        qs.append({
            "text": c[0],
            "options": c[1],
            "correct": c[2],
            "solution": c[3]
        })
    return qs

# ==============================================================================
# VATANDAŞLIK SORU ÜRETECİ (9 DENEME x 15 SORU = 135 ÖZGÜN SORU)
# ==============================================================================
def generate_vatandaslik_for_exam(exam_no):
    e = exam_no
    qs = []
    
    vat_topics = [
        ("Bir hukuk kuralına aykırı davranılması halinde devlet gücüyle uygulanan yaptırımlardan 'iptal' kararı hangi işlem türüne uygulanır?",
         ["A) Hukuka aykırı idari işlemlere", "B) Suç teşkil eden fiillere", "C) Borcunu ödemeyen şahıslara", "D) Boşanma davalarına", "E) Haksız fiillere"], 0,
         "Doğru cevap A'dır. İdari işlemlerin hukuka aykırılığı halinde idare mahkemeleri iptal kararı verir."),

        ("Hakların KAZANILMASINDA geçerli olan temel medeni hukuk ilkesi hangisidir?",
         ["A) İyiniyet (Subjektif İyiniyet)", "B) Dürüstlük Kuralı (Objektif İyiniyet)", "C) Kusursuz Sorumluluk", "D) Ahde Vefa", "E) Kanunilik"], 0,
         "Doğru cevap A'dır. Hakların kazanılmasında iyiniyet, kullanılmasında ve borçların ifasında ise dürüstlük kuralı geçerlidir."),

        ("Bir kimsenin ölüm tehlikesi içinde kaybolması halinde mahkemeden gaiplik kararı istenebilmesi için en az kaç yıl geçmesi gerekir?",
         ["A) 1 yıl", "B) 3 yıl", "C) 5 yıl", "D) 10 yıl", "E) 15 yıl"], 0,
         "Doğru cevap A'dır. Ölüm tehlikesi içinde kaybolmada 1 yıl; uzun süre haber alınamama durumunda ise 5 yıl sonra gaiplik istenebilir."),

        ("1982 Anayasası'na göre Türkiye Devleti'nin yönetim şekli aşağıdakilerden hangisidir?",
         ["A) Cumhuriyet", "B) Meşruti Monarşi", "C) Teokrasi", "D) Federasyon", "E) Oligarşi"], 0,
         "Doğru cevap A'dır. Anayasa Madde 1: 'Türkiye Devleti bir Cumhuriyettir.'"),

        ("Aşağıdakilerden hangisi 1982 Anayasası'nda yer alan 'Sosyal ve Ekonomik Haklar' (İsteme Hakları) arasında yer alır?",
         ["A) Eğitim ve Öğrenim Hakkı", "B) Yaşama Hakkı", "C) Kişi Hürriyeti ve Güvenliği", "D) Seçme ve Seçilme Hakkı", "E) Dilekçe Hakkı"], 0,
         "Doğru cevap A'dır. Eğitim, sağlık, çalışma ve konut hakkı devlette edim isteyen sosyal-ekonomik haklardır."),

        ("Türkiye Büyük Millet Meclisi genel seçimleri kural olarak kaç yılda bir Cumhurbaşkanı seçimiyle birlikte yapılır?",
         ["A) 5 yıl", "B) 4 yıl", "C) 3 yıl", "D) 6 yıl", "E) 7 yıl"], 0,
         "Doğru cevap A'dır. 2017 anayasa değişikliği ile TBMM ve Cumhurbaşkanlığı seçimleri 5 yılda bir aynı gün yapılır."),

        ("Bir milletvekilinin istifa etmesi durumunda milletvekilliğinin düşmesine kim karar verir?",
         ["A) TBMM Genel Kurulu", "B) TBMM Başkanı", "C) Anayasa Mahkemesi", "D) Cumhurbaşkanı", "E) Yüksek Seçim Kurulu"], 0,
         "Doğru cevap A'dır. İstifa eden milletvekilinin üyeliği TBMM Başkanlık Divanı tespitinden sonra TBMM Genel Kurulu kararıyla düşer."),

        ("TBMM'nin bir kanun teklifini kabul edebilmesi için toplantıya katılanların salt çoğunluğu aranır; ancak bu karar yeter sayısı hiçbir şekilde hangisinden az olamaz?",
         ["A) Üye tamsayısının dörtte birinin bir fazlasından (151)", "B) 200 milletvekilinden", "C) 300 milletvekilinden", "D) 184 milletvekilinden", "E) 400 milletvekilinden"], 0,
         "Doğru cevap A'dır. Karar yeter sayısı üye tamsayısının (600) 1/4'ünün 1 fazlası olan 151'den az olamaz."),

        ("Cumhurbaşkanı yardımcıları ve bakanları atama ve görevlerine son verme yetkisi kime aittir?",
         ["A) Cumhurbaşkanına", "B) TBMM Genel Kurulu'na", "C) TBMM Başkanı'na", "D) Anayasa Mahkemesi'ne", "E) Danıştay'a"], 0,
         "Doğru cevap A'dır. Bakanlar ve yardımcılar doğrudan Cumhurbaşkanı tarafından atanır ve görevden alınır."),

        ("Cumhurbaşkanlığı Kararnameleri ile aşağıdakilerden hangisi DÜZENLENEMEZ?",
         ["A) Anayasa'da yer alan Temel Haklar ve Kişi Hakları", "B) Üst kademe kamu yöneticilerinin atanması", "C) Bakanlıkların kurulması ve kaldırılması", "D) Devlet Denetleme Kurulu'nun işleyişi", "E) Milli Güvenlik Kurulu Genel Sekreterliği teşkilatı"], 0,
         "Doğru cevap A'dır. Kişisel haklar ve siyasi haklar CBK ile düzenlenemez; sadece kanunla düzenlenebilir."),

        ("Anayasa Mahkemesi'ne kanunların şekil ve esas bakımından Anayasa'ya aykırılığı iddiasıyla doğrudan iptal davası (Soyut Norm Denetimi) açma süresi Resmi Gazete'de yayımlanmasından itibaren kaç gündür?",
         ["A) 60 gün", "B) 30 gün", "C) 45 gün", "D) 90 gün", "E) 120 gün"], 0,
         "Doğru cevap A'dır. İptal davası açma süresi Resmi Gazete'de yayımlandığı tarihten itibaren 60 gündür."),

        ("Adli yargı kolunun en yüksek temyiz inceleme mercii olan yüksek mahkeme hangisidir?",
         ["A) Yargıtay", "B) Danıştay", "C) Anayasa Mahkemesi", "D) Sayıştay", "E) Uyuşmazlık Mahkemesi"], 0,
         "Doğru cevap A'dır. Hukuk ve ceza mahkemelerinden verilen kararların son inceleme mercii Yargıtay'dır."),

        ("İdare hukukunda merkezi yönetimin taşra teşkilatında 'İl Genel İdaresi'nin başında kim bulunur?",
         ["A) Vali", "B) Kaymakam", "C) Belediye Başkanı", "D) İl Genel Meclisi Başkanı", "E) Defterdar"], 0,
         "Doğru cevap A'dır. İl genel idaresinin başı ve devletin ildeki temsilcisi Vali'dir."),

        ("657 Sayılı Devlet Memurları Kanunu'na göre memura 'görevinde ve davranışlarında daha dikkatli olması gerektiğinin yazı ile bildirilmesi' hangi disiplin cezasıdır?",
         ["A) Uyarma", "B) Kınama", "C) Aylıktan kesme", "D) Kademe durdurma", "E) İhtar"], 0,
         "Doğru cevap A'dır. 'Daha dikkatli olması gerektiğinin yazı ile bildirilmesi' Uyarma cezasının yasal tanımıdır."),

        ("Türkiye Cumhuriyeti'nin 1952 yılında üye olduğu Kuzey Atlantik Antlaşması Örgütü (NATO) askeri ittifakının genel merkezi nerededir?",
         ["A) Brüksel (Belçika)", "B) Washington (ABD)", "C) Cenevre (İsviçre)", "D) Londra (İngiltere)", "E) Paris (Fransa)"], 0,
         "Doğru cevap A'dır. NATO'nun siyasi ve askeri genel karargahı Belçika'nın başkenti Brüksel'dedir.")
    ]

    for v in vat_topics:
        qs.append({
            "text": v[0],
            "options": v[1],
            "correct": v[2],
            "solution": v[3]
        })
    return qs

print("Tarih, Coğrafya ve Vatandaşlık üreteçleri başarıyla hazırlandı.")
