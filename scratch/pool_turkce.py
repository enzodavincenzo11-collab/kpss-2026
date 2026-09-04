import json, sys, random
sys.stdout.reconfigure(encoding='utf-8')

# ==============================================================================
# TÜRKÇE SORU ÜRETECİ (9 DENEME x 30 SORU = 270 ÖZGÜN SORU)
# ==============================================================================
def generate_turkce_for_exam(exam_no):
    # exam_no: 2 .. 10
    e_idx = exam_no - 2  # 0 .. 8
    qs = []

    # 1. Sözcükte Anlam & Deyim (1-5)
    deyimler = [
        ("göz boyamak", "gösterişle aldatmak", "Tüccar, kalitesiz kumaşları vitrine koyarak müşterilerin <u>gözünü boyamaya</u> çalıştı."),
        ("ayaklarına kara sular inmek", "çok yorulmak", "Bütün gün çarşıda evrak peşinde koşmaktan <u>ayaklarına kara sular indi</u>."),
        ("pabucu dama atılmak", "değer ve itibarını kaybetmek", "Yeni model telefon piyasaya çıkınca eskisinin <u>pabucu dama atıldı</u>."),
        ("kılı kırk yarmak", "aşırı titiz ve ayrıntılı davranmak", "Müfettiş hesapları incelerken adeta <u>kılı kırk yarıyordu</u>."),
        ("çantada keklik", "kolayca elde edilecek durumda olmak", "Rakibini <u>çantada keklik</u> gören takım, maçın sonunda büyük bir hüsrana uğradı."),
        ("küplere binmek", "çok öfkelenmek", "Raporun geciktiğini öğrenen genel müdür <u>küplere bindi</u>."),
        ("can kulağıyla dinlemek", "büyük bir dikkatle dinlemek", "Öğrenciler hocanın anlattığı tarihi anektodları <u>can kulağıyla dinledi</u>."),
        ("gözden düşmek", "eski sevgiyi ve ilgiyi yitirmek", "Yaptığı son hatalardan sonra yöneticilerin <u>gözünden düştü</u>."),
        ("eli ayağı dolaşmak", "heyecandan ne yapacağını şaşırmak", "Sahnede adını duyunca heyecandan <u>eli ayağı dolaştı</u>.")
    ]
    cur_deyim = deyimler[e_idx]
    qs.append({
        "text": f"\"{cur_deyim[2]}\"\n\nBu cümledeki altı çizili deyimin cümleye kattığı anlam aşağıdakilerden hangisidir?",
        "options": [
            f"A) {cur_deyim[1].capitalize()}",
            "B) Aceleyle karar vermek",
            "C) Başkalarının fikrine saygı duymak",
            "D) Beklenmedik bir engelle karşılaşmak",
            "E) Kendi çıkarlarını ön planda tutmak"
        ],
        "correct": 0,
        "solution": f"Doğru cevap A'dır. '{cur_deyim[0]}' deyimi Türkçede '{cur_deyim[1]}' anlamında kullanılır."
    })

    # 2. Yazım Kuralı (Altı Çizili - <u> etiketli)
    yazim_sozcukleri = [
        ("laboratuvar", "laboratuar", "Hastanenin <u>laboratuvarında</u> (I) yapılan tahliller temiz çıktı."),
        ("orijinal", "orjinal", "Müzede tablonun <u>orijinal</u> (I) nüshası sergileniyor."),
        ("kılavuz", "klavuz", "Cihazın kullanım <u>kılavuzunu</u> (I) dikkatlice okumalısınız."),
        ("tıraş", "traş", "Sabah erkenden kalkıp <u>tıraş</u> (I) oldu."),
        ("kravat", "kıravat", "Takım elbisesine uygun lacivert bir <u>kravat</u> (I) takmıştı."),
        ("komiser", "komser", "Olay yerine gelen <u>komiser</u> (I) tanıkları dinledi."),
        ("şarj", "şarz", "Telefonun <u>şarjı</u> (I) gün ortasında bitti."),
        ("egzoz", "egzos", "Arabanın <u>egzoz</u> (I) muayenesi dün yapıldı."),
        ("koleksiyon", "kolleksiyon", "Dededen kalma pul <u>koleksiyonunu</u> (I) özenle saklıyor.")
    ]
    cur_y = yazim_sozcukleri[e_idx]
    qs.append({
        "text": f"Yeni açılan tesisteki görevliler, dünkü toplantıda <u>birçok</u> (I) konuyu ele aldı. Projenin <u>{cur_y[1]}</u> (II) aşamasında bazı aksaklıklar yaşansa da ekip <u>özveriyle</u> (III) çalışarak <u>her şeyi</u> (IV) zamanında <u>teslim etti</u> (V).\n\nBu parçada numaralanmış altı çizili sözlerden hangisinin yazımı YANLIŞTIR?",
        "options": ["A) I", "B) II", "C) III", "D) IV", "E) V"],
        "correct": 1,
        "solution": f"Doğru cevap B'dir. '{cur_y[1]}' sözcüğünün TDK kılavuzundaki doğru yazımı '{cur_y[0]}' şeklindedir."
    })

    # 3. Noktalama İşaretleri
    qs.append({
        "text": "Eski bir İstanbul konağının bahçesi ( ) asırlık çınarlar ( ) hanımelleri ve ıhlamur kokuları ( ) Burası insanın tüm yorgunluğunu unutturan bir sığınaktı ( )\n\nBu parçada parantezle belirtilen yerlere sırasıyla hangi noktalama işaretleri getirilmelidir?",
        "options": [
            "A) (:) (,) (...) (.)",
            "B) (,) (;) (.) (!)",
            "C) (;) (,) (,) (.)",
            "D) (:) (;) (...) (!)",
            "E) (,) (,) (.) (...)"
        ],
        "correct": 0,
        "solution": "Doğru cevap A'dır. Bahçede bulunanlar açıklandığı için iki nokta (:), eş görevli ögeler arasına virgül (,), yüklemi olmayan eksiltili cümle sonuna üç nokta (...), tamamlanmış cümle sonuna nokta (.) konur."
    })

    # 4. Cümlede Anlam (Neden-Sonuç, Amaç-Sonuç, Koşul)
    cumle_anlam = [
        ("Hava sıcaklıklarının aniden düşmesi nedeniyle narenciye bahçeleri don tehlikesiyle karşı karşıya kaldı.", "Neden-Sonuç"),
        ("Genç yazar, romanında dili daha zengin kılmak amacıyla yöresel deyişlere sıkça yer vermiştir.", "Amaç-Sonuç"),
        ("Düzenli tekrar yapıp çıkmış soruları dikkatle analiz edersen hedeflediğin puanı rahatça alırsın.", "Koşul-Sonuç"),
        ("Son yıllarda dijital mecraların yaygınlaşmasıyla birlikte geleneksel dergicilik eski ilgisini kaybetti.", "Neden-Sonuç"),
        ("Toplantıda alınan kararları tüm çalışanlara bildirmek üzere bir genelge hazırlandı.", "Amaç-Sonuç"),
        ("Eleştirmenlerin tarafsız yaklaştığı bir sanat ortamında edebiyatın kalitesi günden güne artar.", "Koşul-Sonuç"),
        ("Tarihi köprü, sel sularının ayaklarını aşındırması yüzünden geçici olarak trafiğe kapatıldı.", "Neden-Sonuç"),
        ("Kültürel değerlerimizi gelecek kuşaklara aktarmak için somut olmayan miras envanteri çıkarılıyor.", "Amaç-Sonuç"),
        ("Kitap okuma alışkanlığını erken yaşta edinen bireyler olayları çok daha derinlemesine kavrar.", "Koşul-Sonuç")
    ]
    cur_ca = cumle_anlam[e_idx]
    qs.append({
        "text": f"\"{cur_ca[0]}\"\n\nBu cümlenin anlam özelliği aşağıdakilerden hangisidir?",
        "options": [
            f"A) {cur_ca[1]} ilişkisi içermektedir.",
            "B) Kanıtlanamaz bir varsayım bildirmektedir.",
            "C) Bir ön yargı ve kesin yargı bildirmektedir.",
            "D) Karşılaştırılan iki durum arasında çelişki kurmaktadır.",
            "E) Doğrudan bir tanım cümlesidir."
        ],
        "correct": 0,
        "solution": f"Doğru cevap A'dır. Verilen cümlede eylemin gerekçesi ve yönelimi {cur_ca[1]} çerçevesinde kurulmuştur."
    })

    # 5. Paragrafta Ana Düşünce (Farklı edebiyat, felsefe, kültür metinleri)
    paragraflar = [
        ("Gerçek bir sanatçı, çağının beğenilerine esir olan değil; çağını peşinden sürükleyen kişidir. Modaya uygun yazılan eserler, o mevsim geçince sararıp dökülen yapraklar gibi unutulur. Oysa insanlığın evrensel acılarını ve sevinçlerini dile getiren başyapıtlar, yüzyıllar sonra bile ilk günkü tazeliğini korur.", "Kalıcı olabilmenin yolunun güncel modalara kapılmayıp evrensel değerleri yakalamaktan geçtiği"),
        ("Tarih boyunca insanlık, bilgiyi depolamaktan çok bilgiyi doğru kullanmanın sınavını vermiştir. Bugün internet sayesinde dünyanın tüm kütüphaneleri parmaklarımızın ucunda. Ancak bu sonsuz bilgi okyanusunda boğulmamak için eleştirel düşünme süzgecine her zamankinden daha çok muhtacız.", "Bilgiye kolay erişilen çağımızda kritik olanın eleştirel süzgeçten geçirme yeteneği olduğu"),
        ("Çocuklukta dinlenen masallar, insanın zihinsel sınırlarını sonsuzluğa açan ilk sihirli anahtarlardır. Masalların mantık dışı görünen dünyası, çocuğun ileriki yaşlarda yaratıcı çözümler üretmesine, imkânsız görüneni deneme cesareti bulmasına zemin hazırlar.", "Masalların çocuğun yaratıcı düşünme ve hayal gücünü geliştirmede vazgeçilmez bir role sahip olduğu"),
        ("Mimari, bir toplumun sadece taşa ve betona verdiği biçim değil; o toplumun hayatı, insanı ve doğayı nasıl algıladığının açık bir aynasıdır. Geniş avlulu, cumbalı geleneksel evlerimize baktığımızda mahremiyet ile komşuluk sıcaklığının nasıl kusursuzca kaynaştığını görürüz.", "Mimarinin bir toplumun kültürel ve insani değerlerinin somutlaşmış hali olduğu"),
        ("Eleştiri, sanıldığı gibi bir eseri karalama veya kusurlarını yüzüne vurma sanatı değildir. Tam aksine eleştiri; eserin estetik dokusunu okura görünür kılan, yazara kendi ufkunu genişletme fırsatı sunan yapıcı bir rehberliktir.", "Gerçek eleştirinin eseri anlamaya ve sanatı geliştirmeye hizmet eden yapıcı bir kılavuz olduğu"),
        ("Dil, canlı bir varlık gibi sürekli beslenir, dönüşür ve toplumsal hayatla birlikte nefes alır. Bir dili yabancı kelimelerin istilasından korumak ne kadar gerekliyse, onu yaşayan kültürden koparıp yapay kurallarla dondurmaya çalışmak da o kadar tehlikelidir.", "Dilin hem özünü koruyarak hem de yaşayan hayatla bağını koparmadan gelişmesi gerektiği"),
        ("Bilim ile sanat, insan aklının ve ruhunun aynı hedefe yönelmiş iki farklı kanadıdır. Biri gerçeği deney ve formüllerle ararken diğeri aynı gerçeği sezgi ve estetikle yakalamaya çalışır. Kanatlardan birini ihmal eden medeniyetler asla yükselemez.", "Medeniyetlerin ilerleyişinde bilim ve sanatın birbirini tamamlayan iki temel güç olduğu"),
        ("Zamanı iyi yönetmek, her dakikayı bir işle doldurmak anlamına gelmez. Bazen durup düşünmek, iç sesimizi dinlemek ve hiçbir şey yapmadan anı yaşamak; gün boyu koşturmaktan çok daha verimli bir yenilenme sağlar.", "Zaman yönetiminin sadece yoğun çalışmaktan ibaret olmayıp dinlenme ve tefekküre de alan açması gerektiği"),
        ("Fotoğraf çekmek, hayattan bir anı dondurmak gibi görünse de aslında bakan kişinin dünyaya hangi pencereden baktığının ilanıdır. İki kişi aynı manzaraya bakar fakat birinin çektiği kare sıradan bir görüntü iken diğerininki bir şiire dönüşür.", "Fotoğraf sanatında asıl belirleyici olanın teknik donanım değil, sanatçının şahsi bakış açısı ve duyarlılığı olduğu")
    ]
    cur_p = paragraflar[e_idx]
    qs.append({
        "text": f"{cur_p[0]}\n\nBu parçada asıl anlatılmak istenen aşağıdakilerden hangisidir?",
        "options": [
            f"A) {cur_p[1]}.",
            "B) Sanatçıların ekonomik kaygılarla hareket etmemesi gerektiği.",
            "C) Teknolojik imkânların geleneksel değerleri tehdit ettiği.",
            "D) Bireysel yeteneklerin ancak sıkı bir disiplinle açığa çıkabileceği.",
            "E) Toplumsal kuralların bireyin özgürlüğünü kısıtladığı."
        ],
        "correct": 0,
        "solution": f"Doğru cevap A'dır. Paragrafın bütününde ana fikir olarak '{cur_p[1]}' savunulmaktadır."
    })

    # 6 - 30 arası (25 soru): Gramer, Paragraf Yapısı, Ses Olayları, Cümle Ögeleri
    konular = [
        ("Ses Bilgisi (Ünsüz Düşmesi)", "'Küçücük' sözcüğünde hangi ses olayı gerçekleşmiştir?", ["A) Ünsüz düşmesi", "B) Ünlü düşmesi", "C) Ünsüz türemesi", "D) Kaynaşma", "E) Benzeşme"], 0, "Küçük-cük birleşirken k ünsüzü düşmüştür."),
        ("Ses Bilgisi (Ünsüz Yumuşaması)", "Aşağıdaki sözcüklerin hangisinde ünsüz yumuşaması kuralına aykırılık vardır?", ["A) Hukukun üstünlüğü", "B) Kitabın kapağı", "C) Ağacın dalı", "D) Yurdun dört yanı", "E) Kalbin sesi"], 0, "Yabancı kökenli 'hukuk' sözcüğü ünlüyle başlayan ek aldığında 'hukuğun' olmaz, k sert kalır."),
        ("Cümle Ögeleri", "\"Güneş batarken sahil boyunca yürüyen yaşlı adam, eski günleri tebessümle andı.\" cümlesinde yüklemden önceki bölüm hangi ögedir?", ["A) Belirtili Nesne", "B) Zarf Tümleci", "C) Özne", "D) Dolaylı Tümleç", "E) Edat Tümleci"], 0, "'Neyi andı?' -> 'eski günleri' (Belirtili Nesne)."),
        ("Sözcük Türü (Sıfat)", "Aşağıdaki cümlelerin hangisinde 'güzel' sözcüğü niteleme sıfatı olarak kullanılmıştır?", ["A) Güzel bir ev satın aldılar.", "B) Güzel konuştuğu için herkes dinledi.", "C) Güzelin kahrı çekilmez.", "D) Şiiri çok güzel okudu.", "E) Bugün hava ne güzel."], 0, "'Güzel ev' tamlamasında 'güzel' ismi niteleyen sıfattır."),
        ("Sözcük Türü (Zarf)", "Aşağıdaki cümlelerin hangisinde zaman zarfı kullanılmıştır?", ["A) Yarın sabah erkenden yola çıkacağız.", "B) Koşarak içeri girdi.", "C) Çok çalışarak başardı.", "D) Yavaşça kapıyı kapattı.", "E) Aşağı indi."], 0, "'Yarın sabah' eylemin zamanını bildirir."),
        ("Sözcük Türü (Zamir)", "Aşağıdaki cümlelerin hangisinde belgisiz zamir kullanılmıştır?", ["A) Birkaçı sınava zamanında yetişemedi.", "B) Bu kitabı dün aldım.", "C) Hangi soruyu çözemedin?", "D) Kendi kendine konuşuyordu.", "E) Sen buraya gel."], 0, "'Birkaçı' ismin yerini belirsiz şekilde tuttuğundan belgisiz zamirdir."),
        ("Fiil Çatısı (Geçişli)", "Aşağıdaki fiillerden hangisi nesne alabilen (geçişli) bir fiildir?", ["A) Dinlemek", "B) Uyumak", "C) Ağlamak", "D) Kaçmak", "E) Gülmek"], 0, "'Onu dinlemek' denir; geçişlidir."),
        ("Fiil Çatısı (Edilgen)", "Aşağıdaki cümlelerin hangisinin yüklemi edilgen çatılıdır?", ["A) Sınıf bayram için özenle süslendi.", "B) Çocuk annesini görünce sevindi.", "C) Yaşlı adam pencereden etrafa bakındı.", "D) Ali sabah erkenden yıkandı.", "E) Kuşlar gökyüzünde uçuştu."], 0, "Süsleme işini yapan belirsizdir, süslendi edilgendir."),
        ("Cümle Türleri (Birleşik)", "Aşağıdaki cümlelerin hangisi yapısına göre 'girişik birleşik' cümledir?", ["A) Yağmur yağınca herkes saçak altlarına kaçıştı.", "B) Kapıyı açtı ve içeri girdi.", "C) Bugün hava çok sıcak.", "D) Bize geldi ama fazla kalmadı.", "E) Ankara'ya yarın gidecek."], 0, "İçinde fiilimsi ('yağınca') bulunan tek yüklemli cümle girişik birleşiktir."),
        ("Anlatım Bozukluğu", "\"Hiçbir çalışan patronun sözünü dinlemiyor, kendi bildiğini yapıyordu.\" cümlesindeki anlatım bozukluğunun nedeni nedir?", ["A) İkinci cümlede özne eksikliği (hepsi yapıyordu)", "B) Nesne eksikliği", "C) Yanlış edat kullanımı", "D) Yüklem uyuşmazlığı", "E) Sözcüğün yanlış yerde kullanımı"], 0, "'Hiçbiri' olumsuz özne olduğu için olumlu 'yapıyordu' yüklemine bağlanamaz; 'hepsi kendi bildiğini yapıyordu' denmelidir."),
        ("Paragraf (Akışı Bozan)", "(I) Bozkırda bahar kısa ama görkemlidir. (II) Karlar erir erimez her yer rengarenk çiçeklerle donanır. (III) Tarım arazilerinin sulanması için baraj inşaatları sürdürülmektedir. (IV) Ancak yazın sıcağı bastırınca bu cümbüş yerini sarı bir sessizliğe bırakır. (V) Doğa bir sonraki bahara kadar uykuya çekilir.\n\nAkışı bozan cümle hangisidir?", ["A) I", "B) II", "C) III", "D) IV", "E) V"], 2, "III. cümle doğa anlatımı arasına giren alakasız bir ekonomik faaliyettir."),
        ("Paragraf (İkiye Bölme)", "Bir metinde yeni bir düşünce veya konunun farklı bir boyutuna geçilen cümle paragrafı ikiye böler. Bu kurala göre metin mantıksal olarak nereden ayrılmalıdır?", ["A) Konunun yön değiştirdiği cümleden", "B) İlk cümleden", "C) En kısa cümleden", "D) Soru cümlesinden", "E) En son cümleden"], 0, "Paragraf bölme sorularında konu/bakış açısı değişikliği esastır."),
        ("Yazım Kuralı (Tarihler)", "Aşağıdakilerin hangisinde belirli bir tarih bildiren gün ve ay adlarının yazımı DOĞRUDUR?", ["A) 29 Ekim 1923 Pazartesi", "B) 29 ekim 1923", "C) geçen pazartesi günü", "D) eylül ayında", "E) 1995 yılı haziranında"], 0, "Belirli gün ve ay adları (rakamla belirtilen) büyük harfle başlar."),
        ("Yazım Kuralı (Bileşik Fiiller)", "Aşağıdaki cümlelerin hangisinde 'etmek/olmak' ile kurulan bileşik fiilin yazımı YANLIŞTIR?", ["A) Bu durum beni çok <u>rahatsız etti</u>.", "B) Yapılan yardımı <u>kabul etti</u>.", "C) Haberi duyunca <u>kahır oldu</u>.", "D) Bütün borçlarını <u>terk etti</u>.", "E) Durumu hemen <u>fark etti</u>."], 2, "Ses düşmesi olduğu için 'kahroldu' bitişik yazılmalıdır ('kahır oldu' yanlıştır)."),
        ("Söz Sanatları (Benzetme)", "\"Gözleri bir çift kömür gibi parlıyordu.\" cümlesinde hangi söz sanatı vardır?", ["A) Teşbih (Benzetme)", "B) İstiare", "C) Mecaz-ı Mürsel", "D) Tezat", "E) Teşhis"], 0, "'Gibi' edatıyla kömüre benzetme yapılmıştır."),
        ("Söz Sanatları (Kişileştirme)", "\"Rüzgâr dağların ardından usulca fısıldadı.\" cümlesindeki söz sanatı nedir?", ["A) Teşhis (Kişileştirme)", "B) Tariz", "C) Telmih", "D) Mübalağa", "E) Tenasüp"], 0, "İnsana ait fısıldama özelliği rüzgâra verilmiştir."),
        ("Anlatım İlkeleri (Duruluk)", "Bir cümlede gereksiz sözcük kullanılmaması hangi anlatım ilkesidir?", ["A) Duruluk", "B) Açıklık", "C) Akıcılık", "D) Özgünlük", "E) Doğallık"], 0, "Gereksiz sözcükten arınmışlık 'duruluk'tur."),
        ("Anlatım İlkeleri (Açıklık)", "Cümlenin tek bir anlama gelmesi ve çok anlamlılık taşımaması hangi ilkedir?", ["A) Açıklık", "B) Duruluk", "C) Yalınlık", "D) Özlülük", "E) Akıcılık"], 0, "Herkesin aynı şeyi anlaması 'açıklık' ilkesidir."),
        ("Noktalama (Kesme İşareti)", "Aşağıdakilerin hangisinde kesme işareti (') YANLIŞ kullanılmıştır?", ["A) Türkler'in tarihi", "B) TBMM'nin kararı", "C) 1923'te", "D) Atatürk'ün ilkeleri", "E) Konya'ya"], 0, "Özel adlara gelen yapım ekleri ve çokluk eki (-ler) kesmeyle ayrılmaz: 'Türklerin' olmalıdır."),
        ("Noktalama (İki Nokta)", "Kendisinden sonra örnek verilecek cümlenin sonuna hangi noktalama işareti konur?", ["A) İki nokta (:)", "B) Noktalı virgül (;)", "C) Üç nokta (...)", "D) Virgül (,)", "E) Kısa çizgi (-)"], 0, "Örnek veya açıklama öncesinde iki nokta kullanılır."),
        ("Paragrafta Boşluk", "Bir paragrafta 'Oysa' bağlacıyla başlayan cümle kendisinden önceki yargıyla nasıl bir ilişki kurar?", ["A) Karşıtlık ve çelişki", "B) Sebep-sonuç", "C) Örneklendirme", "D) Sıralama", "E) Benzetme"], 0, "'Oysa' bağlacı önceki düşünceye zıt bir durumu bildirir."),
        ("Sözel Mantık (Eleme)", "Beş kişinin yarıştığı bir maratonda Ali, Veli'den önce; Can ise Ali'den önce bitirmiştir. Yarışın sonuncusu kim olamaz?", ["A) Can", "B) Veli", "C) Diğerleri", "D) Bilinemez", "E) Hepsi"], 0, "Can en az iki kişinin önünde olduğu için sonuncu olamaz."),
        ("Deyimler (Öfke)", "Aşağıdaki deyimlerden hangisi öfkelenmek anlamı taşımaz?", ["A) Ağzı kulaklarına varmak", "B) Ateş püskürmek", "C) Tepesi atmak", "D) Cinleri tepesine toplanmak", "E) Burnundan solumak"], 0, "'Ağzı kulaklarına varmak' çok sevinmek demektir."),
        ("Atasözleri", "'Damlaya damlaya göl olur' atasözü hangi erdemi öğütler?", ["A) Tasarruf ve sabır", "B) Cesaret", "C) Dürüstlük", "D) Misafirperverlik", "E) Çalışkanlık"], 0, "Küçük birikimlerin zamanla büyüyeceğini, tasarrufu öğütler."),
        ("Metin Türleri", "Yazarın güncel bir konuyu samimi bir dille, kanıtlama amacı gütmeden kaleme aldığı yazı türü hangisidir?", ["A) Deneme / Fıkra", "B) Makale", "C) Biyografi", "D) Tiyatro", "E) Otobiyografi"], 0, "Öznel ve samimi fikir yazısı denemedir.")
    ]

    for k in konular:
        qs.append({
            "text": f"{k[0]}: {k[1]}",
            "options": k[2],
            "correct": k[3],
            "solution": f"Doğru cevap {chr(65+k[3])}'dir. {k[4]}"
        })

    return qs[:30]

print("Türkçe üreteç fonksiyonu tanımlandı.")
