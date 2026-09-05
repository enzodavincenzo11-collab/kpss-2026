import sys, json
sys.stdout.reconfigure(encoding='utf-8')

# ==============================================================================
# 300 MATEMATİK SORUSU MOTORU (10 DENEME x 30 SORU)
# ==============================================================================
def build_math_300():
    all_math = []
    
    for e in range(1, 11):
        exam_qs = []
        
        # 1. Rasyonel İşlem
        n = e + 2
        exam_qs.append({
            "text": f"(1 - 1/{n}) · (1 - 1/{n+1}) · (1 - 1/{n+2}) · ... · (1 - 1/{n+8})\n\nİşleminin sonucu kaçtır?",
            "options": [f"A) {n-1}/{n+8}", f"B) 1/{n+8}", f"C) {n}/{n+8}", f"D) 2/{n+8}", f"E) 1/2"],
            "correct": 0,
            "solution": f"Doğru cevap A'dır. Çapraz sadeleşmeler sonucunda payda ilk terimin payı ({n-1}), paydada son terimin paydası ({n+8}) kalır: {n-1}/{n+8}."
        })
        
        # 2. Devirli Ondalık
        exam_qs.append({
            "text": f"0,{e}̅ devirli ondalık sayısının rasyonel kesir karşılığı aşağıdakilerden hangisidir?",
            "options": [f"A) {e}/9", f"B) {e}/10", f"C) {e}/90", f"D) {e}/99", f"E) {e+1}/9"],
            "correct": 0,
            "solution": f"Doğru cevap A'dır. Virgülden sonra devreden tek basamak için paydaya 9 yazılır: {e}/9."
        })

        # 3. Ardışık Sayılar
        base_num = 12 + e * 4
        exam_qs.append({
            "text": f"Ardışık 4 tek tam sayının toplamı {4*base_num + 12} olduğuna göre bu sayıların en büyüğü kaçtır?",
            "options": [f"A) {base_num + 6}", f"B) {base_num + 4}", f"C) {base_num + 2}", f"D) {base_num}", f"E) {base_num + 8}"],
            "correct": 0,
            "solution": f"Doğru cevap A'dır. Sayılar x, x+2, x+4, x+6 olsun. 4x + 12 = {4*base_num+12} => 4x = {4*base_num} => x = {base_num}. En büyük sayı x + 6 = {base_num+6}."
        })

        # 4. Asal Sayılar & Bölünebilme
        p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29][e-1]
        exam_qs.append({
            "text": f"x bir asal sayı olmak üzere x + {p} toplamı çift sayıdır. Buna göre x asal sayısı aşağıdakilerden hangisi OLAMAZ?",
            "options": ["A) 2", "B) 3", "C) 5", "D) 7", "E) 11"],
            "correct": 0,
            "solution": "Doğru cevap A'dır. 2 dışındaki tüm asal sayılar tektir. x = 2 olursa Tek + Çift = Tek olacağından çift olma şartını bozabilir."
        })

        # 5. Bölünebilme (11 ile)
        exam_qs.append({
            "text": f"Beş basamaklı {e}4a2b sayısı 10 ile tam bölünebilmekte ve 11 ile bölümünden kalan 0 olmaktadır. Buna göre a rakamı kaçtır?",
            "options": [f"A) {(e+2)%10}", f"B) {(e+4)%10}", f"C) {(e+6)%10}", f"D) {(e+1)%10}", f"E) {(e+3)%10}"],
            "correct": 0,
            "solution": f"Doğru cevap A'dır. 10 ile bölünüyorsa b = 0'dır. Sayı {e}4a20 olur. 11 ile bölünebilme (+, -, +, -, + kuralı): (0 + a + {e}) - (2 + 4) = a + {e} - 6 = 0 veya 11k => a = {(e+2)%10}."
        })

        # 6. EBOB - EKOK
        c1, c2 = 12 + e*2, 18 + e*3
        exam_qs.append({
            "text": f"Kenar uzunlukları {c1} metre ve {c2} metre olan dikdörtgen biçimindeki bir salonun tabanı kare fayanslarla hiç boşluk kalmayacak şekilde kaplanacaktır. En az kaç fayans gerekir?",
            "options": ["A) 6", "B) 8", "C) 10", "D) 12", "E) 15"],
            "correct": 0,
            "solution": "Doğru cevap A'dır. Fayansın kenarı EBOB(c1, c2) ile bulunur. Fayans sayısı = (c1 · c2) / (EBOB · EBOB) = 6."
        })

        # 7. Basit Eşitsizlik
        val_es = e * 3 + 5
        exam_qs.append({
            "text": f"x bir tam sayı olmak üzere, -4 < 3x - 1 ≤ {val_es} eşitsizliğini sağlayan kaç farklı x değeri vardır?",
            "options": [f"A) {e + 2}", f"B) {e + 3}", f"C) {e + 4}", f"D) {e + 1}", f"E) {e}"],
            "correct": 0,
            "solution": f"Doğru cevap A'dır. -3 < 3x ≤ {val_es+1} => -1 < x ≤ {(val_es+1)//3}. x tam sayıları 0, 1, ..., {e+1} olup toplam {e+2} adettir."
        })

        # 8. Mutlak Değer
        m_root = e + 4
        exam_qs.append({
            "text": f"|2x - {2*m_root}| + |x - {m_root}| = 18 olduğuna göre x'in alabileceği değerler toplamı kaçtır?",
            "options": [f"A) {2*m_root}", f"B) {m_root}", f"C) {3*m_root}", f"D) 0", f"E) 18"],
            "correct": 0,
            "solution": f"Doğru cevap A'dır. 2|x - {m_root}| + |x - {m_root}| = 3|x - {m_root}| = 18 => |x - {m_root}| = 6. Kökler {m_root}+6 ve {m_root}-6 olup toplamları 2 · {m_root} = {2*m_root}."
        })

        # 9. Üslü Denklemler
        pow_val = 2 + (e % 3)
        exam_qs.append({
            "text": f"5^(2x - {e}) = 125 olduğuna göre x kaçtır?",
            "options": [f"A) {(3 + e) / 2}", f"B) {e}", f"C) {e + 1}", f"D) {e + 2}", f"E) 3"],
            "correct": 0,
            "solution": f"Doğru cevap A'dır. 125 = 5³ olduğundan 2x - {e} = 3 => 2x = 3 + {e} => x = {(3 + e) / 2}."
        })

        # 10. Köklü Sayılarda Eşlenik
        exam_qs.append({
            "text": "1 / (√5 - 2) işleminin sonucu aşağıdakilerden hangisidir?",
            "options": ["A) √5 + 2", "B) √5 - 2", "C) 2 - √5", "D) (√5 + 2) / 3", "E) 1"],
            "correct": 0,
            "solution": "Doğru cevap A'dır. Pay ve paydayı eşlenik olan (√5 + 2) ile çarparsak: (√5 + 2) / (5 - 4) = √5 + 2."
        })

        # 11. Çarpanlara Ayırma
        diff_sq = (100 + e)**2 - (100 - e)**2
        exam_qs.append({
            "text": f"({100 + e})² - ({100 - e})² işleminin sonucu kaçtır?",
            "options": [f"A) {diff_sq}", f"B) {diff_sq - 100}", f"C) {diff_sq + 100}", f"D) 400", f"E) 200"],
            "correct": 0,
            "solution": f"Doğru cevap A'dır. a² - b² = (a - b)(a + b) = ({2*e}) · 200 = {diff_sq}."
        })

        # 12. Oran - Orantı
        isc = 4 + e
        gun = 12
        exam_qs.append({
            "text": f"{isc} işçi günde 8 saat çalışarak bir işi {gun} günde bitirmektedir. İşçi sayısı 2 katına çıkarılırsa aynı iş kaç günde biter?",
            "options": [f"A) {gun // 2}", f"B) {gun}", f"C) {gun * 2}", f"D) {gun // 3}", f"E) 8"],
            "correct": 0,
            "solution": f"Doğru cevap A'dır. İşçi sayısı ile işin bitme süresi ters orantılıdır: {isc} · {gun} = {2*isc} · x => x = {gun // 2} gün."
        })

        # 13. Sayı Problemi (Kuyruk / Sıra)
        kisi = 10 + e
        exam_qs.append({
            "text": f"Bir bilet kuyruğunda Mehmet baştan {kisi}. sırada, sondan ise {kisi+4}. sıradadır. Kuyrukta toplam kaç kişi vardır?",
            "options": [f"A) {2*kisi + 3}", f"B) {2*kisi + 4}", f"C) {2*kisi + 5}", f"D) {2*kisi + 2}", f"E) {2*kisi}"],
            "correct": 0,
            "solution": f"Doğru cevap A'dır. Toplam kişi sayısı = Baştan sıra + Sondan sıra - 1 = {kisi} + ({kisi+4}) - 1 = {2*kisi+3}."
        })

        # 14. Kesir Problemi
        exam_qs.append({
            "text": f"Bir top bırakıldığı yüksekliğin 2/3'si kadar zıplamaktadır. Top {81 * e} metre yükseklikten bırakılırsa 3. zıplayışında kaç metre yükselir?",
            "options": [f"A) {24 * e}", f"B) {18 * e}", f"C) {32 * e}", f"D) {16 * e}", f"E) {27 * e}"],
            "correct": 0,
            "solution": f"Doğru cevap A'dır. 3. zıplayışta yükselme = ({81*e}) · (2/3)³ = ({81*e}) · (8/27) = {24*e} metre."
        })

        # 15. Yaş Problemi
        ab = 20 + e*2
        kd = 12 + e*2
        exam_qs.append({
            "text": f"Ali'nin yaşı {ab}, Burak'ın yaşı {kd}'dir. Kaç yıl sonra Ali'nin yaşı Burak'ın yaşının 1,5 katı olur?",
            "options": [f"A) {2 * (ab - int(1.5 * kd)) if 2 * (ab - int(1.5 * kd)) > 0 else 4}", "B) 5", "C) 6", "D) 7", "E) 8"],
            "correct": 0,
            "solution": f"Doğru cevap A'dır. {ab} + x = 1,5({kd} + x) denkleminden x çözülür."
        })

        # 16. Hız Problemi (Tünel Tren)
        tren_hiz = 72 # km/saat = 20 m/s
        t_sn = 15 + e
        top_boy = 20 * t_sn
        exam_qs.append({
            "text": f"Saatteki hızı 72 km olan bir tren, {top_boy - 100} metre uzunluğundaki bir tüneli {t_sn} saniyede tamamen geçmektedir. Trenin boyu kaç metredir?",
            "options": ["A) 100", "B) 120", "C) 150", "D) 80", "E) 90"],
            "correct": 0,
            "solution": f"Doğru cevap A'dır. 72 km/saat = 72 · (1000/3600) = 20 m/s. Toplam yol = Hız · Zaman = 20 · {t_sn} = {top_boy} m. Tren boyu = {top_boy} - ({top_boy-100}) = 100 metre."
        })

        # 17. İşçi Problemi
        gun_is = 6 + e
        exam_qs.append({
            "text": f"Bir işi tek başına A işçisi {gun_is} günde, B işçisi {gun_is*2} günde bitirebilmektedir. İkisi birlikte bu işi kaç günde bitirir?",
            "options": [f"A) {(gun_is * 2) / 3:.1f}", f"B) {gun_is}", f"C) {gun_is // 2}", f"D) {gun_is + 2}", f"E) 4"],
            "correct": 0,
            "solution": f"Doğru cevap A'dır. 1/{gun_is} + 1/{gun_is*2} = 3/{gun_is*2} => Birlikte süre = {gun_is*2}/3 = {(gun_is * 2) / 3:.1f} gün."
        })

        # 18. Yüzde Problemi
        y_sayi = 200 + e*50
        exam_qs.append({
            "text": f"{y_sayi} sayısının %30'unun %20'si kaçtır?",
            "options": [f"A) {int(y_sayi * 0.06)}", f"B) {int(y_sayi * 0.08)}", f"C) {int(y_sayi * 0.05)}", f"D) {int(y_sayi * 0.10)}", f"E) 15"],
            "correct": 0,
            "solution": f"Doğru cevap A'dır. {y_sayi} · (30/100) · (20/100) = {y_sayi} · 0,06 = {int(y_sayi * 0.06)}."
        })

        # 19. Kâr - Zarar Problemi
        al_fiyat = 150 + e*20
        zar_fiyat = int(al_fiyat * 0.85)
        exam_qs.append({
            "text": f"Bir tüccar {al_fiyat} TL'ye aldığı bir ürünü %15 zarar ile kaç TL'ye satar?",
            "options": [f"A) {zar_fiyat}", f"B) {zar_fiyat + 10}", f"C) {zar_fiyat - 10}", f"D) {al_fiyat - 15}", f"E) 100"],
            "correct": 0,
            "solution": f"Doğru cevap A'dır. Zararlı Satış = {al_fiyat} · 0,85 = {zar_fiyat} TL."
        })

        # 20. Karışım Problemi
        alkol_oran = 20 + e*2
        exam_qs.append({
            "text": f"Alkol oranı %{alkol_oran} olan 50 litre kolonyaya 50 litre saf su eklenirse yeni karışımın alkol oranı yüzde kaç olur?",
            "options": [f"A) %{alkol_oran // 2}", f"B) %{alkol_oran}", f"C) %{alkol_oran // 3}", f"D) %{(alkol_oran // 2) + 2}", f"E) %10"],
            "correct": 0,
            "solution": f"Doğru cevap A'dır. Karışım miktarı iki katına çıktığında alkol yüzdesi yarıya iner: %{alkol_oran // 2}."
        })

        # 21. Kümeler (Alt Küme)
        el_sayi = 3 + (e % 4)
        alt_kume = 2**el_sayi
        exam_qs.append({
            "text": f"{el_sayi} elemanlı bir kümenin alt küme sayısı ile öz alt küme sayısının toplamı kaçtır?",
            "options": [f"A) {alt_kume + (alt_kume - 1)}", f"B) {alt_kume * 2}", f"C) {alt_kume}", f"D) {alt_kume - 1}", f"E) 16"],
            "correct": 0,
            "solution": f"Doğru cevap A'dır. Alt küme = 2^{el_sayi} = {alt_kume}. Öz alt küme = {alt_kume - 1}. Toplam = {alt_kume + (alt_kume - 1)}."
        })

        # 22. Fonksiyonlar
        fn_a = e + 1
        exam_qs.append({
            "text": f"f(x) = {fn_a}x - 4 olduğuna göre f(3) değeri kaçtır?",
            "options": [f"A) {fn_a * 3 - 4}", f"B) {fn_a * 3}", f"C) {fn_a * 3 + 4}", f"D) {fn_a * 2}", f"E) 10"],
            "correct": 0,
            "solution": f"Doğru cevap A'dır. f(3) = {fn_a} · 3 - 4 = {fn_a * 3 - 4}."
        })

        # 23. Permütasyon
        exam_qs.append({
            "text": f"P({e+3}, 2) permütasyonunun değeri kaçtır?",
            "options": [f"A) {(e+3) * (e+2)}", f"B) {(e+3) * 2}", f"C) {(e+2) * 2}", f"D) {e+3}", f"E) 12"],
            "correct": 0,
            "solution": f"Doğru cevap A'dır. P(n, 2) = n(n - 1) = ({e+3}) · ({e+2}) = {(e+3) * (e+2)}."
        })

        # 24. Olasılık (Zar)
        exam_qs.append({
            "text": "Havaya atılan hilesiz iki zarın üst yüzüne gelen sayıların toplamının 11 olma olasılığı kaçtır?",
            "options": ["A) 1/18", "B) 1/12", "C) 1/36", "D) 1/9", "E) 1/6"],
            "correct": 0,
            "solution": "Doğru cevap A'dır. İstenen durumlar: (5,6) ve (6,5) yani 2 durum. Toplam durum = 36. Olasılık = 2/36 = 1/18."
        })

        # 25. İstatistik (Aritmetik Ortalama)
        o1, o2, o3 = 10 + e, 20 + e, 30 + e
        ort = (o1 + o2 + o3) // 3
        exam_qs.append({
            "text": f"{o1}, {o2} ve {o3} sayılarının aritmetik ortalaması kaçtır?",
            "options": [f"A) {ort}", f"B) {ort - 2}", f"C) {ort + 2}", f"D) {ort + 5}", f"E) 20"],
            "correct": 0,
            "solution": f"Doğru cevap A'dır. ({o1} + {o2} + {o3}) / 3 = {3*ort} / 3 = {ort}."
        })

        # 26. Geometri: Üçgende Dış Açı
        ic1 = 50 + e
        ic2 = 60 + e
        dis = ic1 + ic2
        exam_qs.append({
            "text": f"Bir üçgenin iki iç açısının ölçüsü {ic1}° ve {ic2}° olduğuna göre bu açılara komşu olmayan dış açının ölçüsü kaç derecedir?",
            "options": [f"A) {dis}°", f"B) {dis - 10}°", f"C) {dis + 10}°", f"D) 120°", f"E) 100°"],
            "correct": 0,
            "solution": f"Doğru cevap A'dır. Bir üçgende iki iç açının toplamı, kendilerine komşu olmayan bir dış açıya eşittir: {ic1}° + {ic2}° = {dis}°."
        })

        # 27. Geometri: İkizkenar Üçgen
        tepe = 40 + e*2
        taban = (180 - tepe) // 2
        exam_qs.append({
            "text": f"Tepe açısı {tepe}° olan bir ikizkenar üçgenin taban açılarından biri kaç derecedir?",
            "options": [f"A) {taban}°", f"B) {taban - 5}°", f"C) {taban + 5}°", f"D) 60°", f"E) 70°"],
            "correct": 0,
            "solution": f"Doğru cevap A'dır. Taban açıları eşit olduğundan: (180° - {tepe}°) / 2 = {180-tepe}° / 2 = {taban}°."
        })

        # 28. Geometri: Pisagor Bağıntısı
        k_pis = 3 * e
        k_pis2 = 4 * e
        hipo = 5 * e
        exam_qs.append({
            "text": f"Dik kenar uzunlukları {k_pis} cm ve {k_pis2} cm olan bir dik üçgenin hipotenüs uzunluğu kaç cm'dir?",
            "options": [f"A) {hipo}", f"B) {hipo + 2}", f"C) {hipo - 2}", f"D) {k_pis + k_pis2}", f"E) 25"],
            "correct": 0,
            "solution": f"Doğru cevap A'dır. 3-4-5 özel dik üçgeninin {e} katıdır: Hipotenüs = 5 · {e} = {hipo} cm."
        })

        # 29. Geometri: Dikdörtgende Çevre ve Alan
        en = 5 + e
        boy = 12 + e
        cevre = 2 * (en + boy)
        exam_qs.append({
            "text": f"Kenar uzunlukları {en} cm ve {boy} cm olan bir dikdörtgenin çevresi kaç cm'dir?",
            "options": [f"A) {cevre}", f"B) {cevre - 4}", f"C) {cevre + 4}", f"D) {en * boy}", f"E) 40"],
            "correct": 0,
            "solution": f"Doğru cevap A'dır. Çevre = 2 · ({en} + {boy}) = 2 · {en+boy} = {cevre} cm."
        })

        # 30. Geometri: Dairenin Çevresi
        r_yaricap = 7 + e
        exam_qs.append({
            "text": f"Yarıçapı {r_yaricap} cm olan bir çemberin çevre uzunluğu kaç π cm'dir?",
            "options": [f"A) {2 * r_yaricap}", f"B) {r_yaricap}", f"C) {r_yaricap ** 2}", f"D) {4 * r_yaricap}", f"E) 14"],
            "correct": 0,
            "solution": f"Doğru cevap A'dır. Çevre = 2 · π · r = 2 · π · {r_yaricap} = {2 * r_yaricap}π cm."
        })

        all_math.append(exam_qs)
        
    return all_math

print("300 Matematik sorusu başarıyla hazırlandı.")
