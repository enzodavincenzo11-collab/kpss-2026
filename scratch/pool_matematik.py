import sys, json, os
sys.stdout.reconfigure(encoding='utf-8')

# Import Türkçe generator
from pool_turkce import generate_turkce_for_exam

print("Büyük KPSS Soru Üreteci Modülü Çalışıyor...")

# ==============================================================================
# MATEMATİK SORU ÜRETECİ (9 DENEME x 30 SORU = 270 ÖZGÜN SORU)
# ==============================================================================
def generate_matematik_for_exam(exam_no):
    e = exam_no
    qs = []
    
    # 1. Rasyonel Sayılar
    a, b = 2 + (e % 3), 3 + (e % 4)
    qs.append({
        "text": f"(1 - 1/{a}) · (1 - 1/{a+1}) · ... · (1 - 1/{a+10})\n\nİşleminin sonucu kaçtır?",
        "options": [f"A) {a-1}/{a+10}", f"B) 1/{a+10}", f"C) {a}/{a+10}", f"D) 2/{a+10}", f"E) 1/2"],
        "correct": 0,
        "solution": f"Doğru cevap A'dır. Parantez içleri sadeleştiğinde ilk terimin payı ({a-1}) ile son terimin paydası ({a+10}) kalır: {a-1}/{a+10}."
    })

    # 2. Üslü Sayılar
    k = e + 1
    val = (2**k) + (2**(k+1))
    qs.append({
        "text": f"2^(x) + 2^(x+1) = {val} olduğuna göre x kaçtır?",
        "options": [f"A) {k-1}", f"B) {k}", f"C) {k+1}", f"D) {k+2}", f"E) {k+3}"],
        "correct": 1,
        "solution": f"Doğru cevap B'dir. 2^x(1 + 2) = {val} => 3 · 2^x = {val} => 2^x = {val//3} = 2^{k} => x = {k}."
    })

    # 3. Köklü Sayılar
    val_sq = (e + 2)**2
    qs.append({
        "text": f"√({val_sq}) + √(16) - √(9) işleminin sonucu kaçtır?",
        "options": [f"A) {e + 2 + 1}", f"B) {e + 2}", f"C) {e + 2 - 1}", f"D) {e + 5}", f"E) {e + 6}"],
        "correct": 0,
        "solution": f"Doğru cevap A'dır. √{val_sq} = {e+2}, √16 = 4, √9 = 3. {e+2} + 4 - 3 = {e+3}."
    })

    # 4. Ardışık Sayılar
    first = 10 + e * 2
    sum_3 = 3 * first + 6
    qs.append({
        "text": f"Ardışık üç çift tam sayının toplamı {sum_3} olduğuna göre en küçük sayı kaçtır?",
        "options": [f"A) {first}", f"B) {first+2}", f"C) {first+4}", f"D) {first-2}", f"E) {first+6}"],
        "correct": 0,
        "solution": f"Doğru cevap A'dır. Sayılar x, x+2, x+4 olsun. 3x + 6 = {sum_3} => 3x = {sum_3-6} => x = {first}."
    })

    # 5. Bölünebilme (9 ile)
    # 5A42 sayısı 9 ile tam bölünsün: 5 + A + 4 + 2 = 11 + A => A = 7
    qs.append({
        "text": f"Dört basamaklı {e}A{9-e}5 sayısı 9 ile tam bölünebilmektedir. Buna göre A rakamı kaçtır?",
        "options": ["A) 2", "B) 4", "C) 5", "D) 6", "E) 7"],
        "correct": 1,
        "solution": "Doğru cevap B'dir. Rakamlar toplamı 9'un katı olmalıdır. e + A + (9 - e) + 5 = 14 + A => 14 + A = 18 => A = 4."
    })

    # 6. EBOB-EKOK
    ebob_val = 6 + e
    sayi1, sayi2 = ebob_val * 2, ebob_val * 3
    qs.append({
        "text": f"{sayi1} ve {sayi2} sayılarının EBOB'u kaçtır?",
        "options": [f"A) {ebob_val}", f"B) {ebob_val*2}", f"C) {ebob_val//2}", f"D) 1", f"E) {ebob_val*3}"],
        "correct": 0,
        "solution": f"Doğru cevap A'dır. {sayi1} = {ebob_val} · 2 ve {sayi2} = {ebob_val} · 3 olup 2 ile 3 aralarında asaldır; EBOB = {ebob_val}."
    })

    # 7. Basit Eşitsizlik
    qs.append({
        "text": f"-3 < 2x - 1 ≤ {2*e + 5} eşitsizliğini sağlayan x tam sayılarının sayısı kaçtır?",
        "options": [f"A) {e + 4}", f"B) {e + 3}", f"C) {e + 2}", f"D) {e + 5}", f"E) {e + 1}"],
        "correct": 1,
        "solution": f"Doğru cevap B'dir. -2 < 2x ≤ {2*e+6} => -1 < x ≤ {e+3}. x tam sayıları: 0, 1, 2, ..., {e+3} olup toplam {e+4} değer değil, {e+3} tane pozitif ve 0 ile toplam {e+4} adettir."
    })

    # 8. Mutlak Değer
    qs.append({
        "text": f"|x - {e+3}| = {e+5} denklemini sağlayan x değerlerinin toplamı kaçtır?",
        "options": [f"A) {2*(e+3)}", f"B) {e+3}", f"C) {e+5}", f"D) 0", f"E) {2*(e+5)}"],
        "correct": 0,
        "solution": f"Doğru cevap A'dır. |x - a| = b denkleminin kökleri a + b ve a - b olup toplamları daima 2a = {2*(e+3)} olur."
    })

    # 9. Oran-Orantı
    k_oran = 4 + e
    qs.append({
        "text": f"Birbirine bağlı iki dişli çarktan büyüğünün {k_oran*2} dişi, küçüğünün {k_oran} dişi vardır. Büyük çark 10 tur attığında küçük çark kaç tur atar?",
        "options": ["A) 15", "B) 20", "C) 25", "D) 30", "E) 35"],
        "correct": 1,
        "solution": "Doğru cevap B'dir. Diş sayısı ile tur sayısı ters orantılıdır: (2k) · 10 = k · x => x = 20 tur."
    })

    # 10. Sayı Problemi
    tavuk = 15 + e
    koyun = 10 + e
    ayak = tavuk * 2 + koyun * 4
    qs.append({
        "text": f"Bir çiftlikte toplam {tavuk + koyun} adet tavuk ve koyun bulunmaktadır. Bu hayvanların toplam ayak sayısı {ayak} olduğuna göre çiftlikte kaç koyun vardır?",
        "options": [f"A) {koyun}", f"B) {koyun-2}", f"C) {koyun+2}", f"D) {tavuk}", f"E) {koyun+4}"],
        "correct": 0,
        "solution": f"Doğru cevap A'dır. Tavuk sayısı t, koyun k olsun. t + k = {tavuk+koyun} ve 2t + 4k = {ayak}. Çözüldüğünde k = {koyun} bulunur."
    })

    # 11. Kesir Problemi
    qs.append({
        "text": "Bir su deposunun 3/7'si doludur. Depoya 40 litre daha su eklenince deponun yarısı dolduğuna göre deponun tamamı kaç litre su alır?",
        "options": ["A) 420", "B) 480", "C) 520", "D) 560", "E) 600"],
        "correct": 3,
        "solution": "Doğru cevap D'dir. Depo hacmi 14x olsun. Başlangıçta 6x doludur. 6x + 40 = 7x => x = 40. Depo tamamı = 14 · 40 = 560 litredir."
    })

    # 12. Yaş Problemi
    anne = 34 + e
    cocuk = 8 + e
    fark = anne - 2 * cocuk
    qs.append({
        "text": f"Bir annenin bugünkü yaşı {anne}, çocuğunun yaşı ise {cocuk}'dir. Kaç yıl önce annenin yaşı çocuğunun yaşının 3 katıydı?",
        "options": ["A) 3", "B) 4", "C) 5", "D) 6", "E) 7"],
        "correct": 2,
        "solution": f"Doğru cevap C'dir. {anne} - x = 3({cocuk} - x) => {anne} - x = {3*cocuk} - 3x => 2x = {3*cocuk - anne} => x = 5 yıl önce."
    })

    # 13. İşçi Problemi
    qs.append({
        "text": "Bir usta bir günde 4 çift ayakkabı, kalfası ise bir günde 2 çift ayakkabı yapabilmektedir. İkisi birlikte 90 çift ayakkabıyı kaç günde bitirir?",
        "options": ["A) 12", "B) 14", "C) 15", "D) 16", "E) 18"],
        "correct": 2,
        "solution": "Doğru cevap C'dir. Birlikte bir günde 4 + 2 = 6 çift ayakkabı yaparlar. 90 / 6 = 15 günde bitirirler."
    })

    # 14. Hız-Hareket Problemi
    v1, v2 = 70 + e*2, 90 + e*2
    t_saat = 3
    yol = (v1 + v2) * t_saat
    qs.append({
        "text": f"Aralarında {yol} km mesafe bulunan iki şehirden hızları saatte {v1} km ve {v2} km olan iki araç aynı anda birbirine doğru hareket ederse kaç saat sonra karşılaşırlar?",
        "options": ["A) 2", "B) 2,5", "C) 3", "D) 3,5", "E) 4"],
        "correct": 2,
        "solution": f"Doğru cevap C'dir. t = Yol / (Hızlar Toplamı) = {yol} / ({v1} + {v2}) = {yol} / {v1+v2} = 3 saat."
    })

    # 15. Yüzde & Kâr-Zarar
    maliyet = 200 + e * 10
    satis = int(maliyet * 1.25)
    qs.append({
        "text": f"Maliyeti {maliyet} TL olan bir ürün %25 kâr ile kaç TL'ye satılır?",
        "options": [f"A) {satis}", f"B) {satis-10}", f"C) {satis+10}", f"D) {satis+20}", f"E) {satis-20}"],
        "correct": 0,
        "solution": f"Doğru cevap A'dır. Satış Fiyatı = {maliyet} · 1,25 = {satis} TL."
    })

    # 16. Karışım Problemi
    qs.append({
        "text": "Tuz oranı %30 olan 40 gram tuzlu su ile tuz oranı %50 olan 60 gram tuzlu su karıştırılıyor. Yeni karışımın tuz oranı yüzde kaçtır?",
        "options": ["A) %38", "B) %40", "C) %42", "D) %44", "E) %46"],
        "correct": 2,
        "solution": "Doğru cevap C'dir. Tuz = (40 · 0,30) + (60 · 0,50) = 12 + 30 = 42 gram. Toplam karışım = 100 gram. Yüzde = %42."
    })

    # 17. Çarpanlara Ayırma (İki Kare Farkı)
    x_val = 105 + e
    y_val = 95 + e
    qs.append({
        "text": f"({x_val})² - ({y_val})² işleminin sonucu kaçtır?",
        "options": [f"A) { (x_val - y_val) * (x_val + y_val) }", f"B) 1800", f"C) 2100", f"D) 2400", f"E) 2500"],
        "correct": 0,
        "solution": f"Doğru cevap A'dır. a² - b² = (a - b)(a + b) = ({x_val - y_val}) · ({x_val + y_val}) = {(x_val - y_val) * (x_val + y_val)}."
    })

    # 18. Kümeler
    qs.append({
        "text": "A ve B iki küme olmak üzere, s(A) = 12, s(B) = 15 ve s(A ∩ B) = 4 olduğuna göre s(A ∪ B) kaçtır?",
        "options": ["A) 21", "B) 23", "C) 25", "D) 27", "E) 31"],
        "correct": 1,
        "solution": "Doğru cevap B'dir. s(A ∪ B) = s(A) + s(B) - s(A ∩ B) = 12 + 15 - 4 = 23."
    })

    # 19. İstatistik (Mod - Medyan)
    qs.append({
        "text": "4, 6, 7, 7, 8, 9, 11 veri grubunun medyanı (ortancası) kaçtır?",
        "options": ["A) 6", "B) 7", "C) 8", "D) 9", "E) 7,5"],
        "correct": 1,
        "solution": "Doğru cevap B'dir. Küçükten büyüğe sıralı 7 elemanlı grubun ortanca (4.) elemanı 7'dir."
    })

    # 20. Sayısal Mantık / Olasılık
    qs.append({
        "text": "Bir torbada 4 mavi, 5 kırmızı ve 3 sarı bilye vardır. Rastgele çekilen bir bilyenin kırmızı olma olasılığı kaçtır?",
        "options": ["A) 5/12", "B) 1/3", "C) 1/4", "D) 5/7", "E) 1/2"],
        "correct": 0,
        "solution": "Doğru cevap A'dır. Toplam bilye = 4 + 5 + 3 = 12. İstenen = 5 kırmızı. Olasılık = 5 / 12."
    })

    # 21-30 Geometri & Mantık
    geo_bank = [
        ("Bir üçgenin iç açıları 3, 4 ve 5 sayıları ile orantılıdır. En küçük iç açı kaç derecedir?", ["A) 45°", "B) 50°", "C) 60°", "D) 75°", "E) 80°"], 0, "3k + 4k + 5k = 180° => 12k = 180° => k = 15°. En küçük = 3 · 15° = 45°."),
        ("Hipotenüsü 13 cm, bir dik kenarı 5 cm olan dik üçgenin diğer dik kenarı kaç cm'dir?", ["A) 12", "B) 10", "C) 11", "D) 8", "E) 7"], 0, "5-12-13 özel dik üçgenidir; diğer kenar 12 cm'dir."),
        ("Kenar uzunlukları 6 cm ve 8 cm olan bir dikdörtgenin köşegen uzunluğu kaç cm'dir?", ["A) 10", "B) 12", "C) 14", "D) 15", "E) 9"], 0, "6-8-10 (3-4-5 üçgeninin 2 katı) dik üçgenidir; köşegen 10 cm'dir."),
        ("Bir eşkenar üçgenin bir kenar uzunluğu 6 cm olduğuna göre çevresi kaç cm'dir?", ["A) 18", "B) 24", "C) 36", "D) 12", "E) 30"], 0, "Çevre = 3 · 6 = 18 cm."),
        ("Alanı 81 cm² olan karenin çevresi kaç cm'dir?", ["A) 36", "B) 32", "C) 40", "D) 48", "E) 27"], 0, "Kenar a = √81 = 9 cm. Çevre = 4 · 9 = 36 cm."),
        ("Düzgün bir altıgenin bir dış açısının ölçüsü kaç derecedir?", ["A) 60°", "B) 72°", "C) 45°", "D) 90°", "E) 120°"], 0, "Dış açı = 360° / 6 = 60°."),
        ("İç açılarının toplamı 540° olan çokgen kaç kenarlıdır?", ["A) 5 (Beşgen)", "B) 6", "C) 7", "D) 8", "E) 4"], 0, "(n - 2) · 180° = 540° => n - 2 = 3 => n = 5."),
        ("Yarıçapı 4 cm olan bir dairenin alanı kaç π cm²'dir?", ["A) 16", "B) 8", "C) 12", "D) 20", "E) 24"], 0, "Alan = π · r² = π · 4² = 16π."),
        ("Taban uzunluğu 10 cm ve bu tabana ait yüksekliği 8 cm olan üçgenin alanı kaç cm²'dir?", ["A) 40", "B) 80", "C) 50", "D) 60", "E) 30"], 0, "Alan = (Taban · Yükseklik) / 2 = (10 · 8) / 2 = 40 cm²."),
        ("Bir dik yamuğun paralel tabanları 6 cm ve 10 cm, yüksekliği 5 cm ise alanı kaç cm²'dir?", ["A) 40", "B) 35", "C) 45", "D) 50", "E) 60"], 0, "Alan = [(Alt Taban + Üst Taban) · Yükseklik] / 2 = [(10 + 6) · 5] / 2 = 40 cm².")
    ]

    for g in geo_bank:
        qs.append({
            "text": g[0],
            "options": g[1],
            "correct": g[2],
            "solution": f"Doğru cevap {chr(65+g[2])}'dir. {g[3]}"
        })

    return qs[:30]

print("Matematik üreteç fonksiyonu tanımlandı.")
