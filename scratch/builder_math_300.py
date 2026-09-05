import sys, json

def make_q(q_id, subject, stem, correct_choice, dist_list, explanation_core, letter_idx):
    letters = ["A", "B", "C", "D", "E"]
    target_idx = letter_idx % 5
    choices = list(dist_list[:4])
    choices.insert(target_idx, correct_choice)
    options = [f"{letters[i]}) {choices[i]}" for i in range(5)]
    correct_letter = letters[target_idx]
    solution = f"Doğru cevap {correct_letter}'dir. {explanation_core}"
    return {
        "id": q_id,
        "subject": subject,
        "text": stem,
        "options": options,
        "correct": target_idx,
        "solution": solution
    }

def build_all_math():
    all_exams_math = []
    
    for e in range(1, 11):
        qs = []
        base_id = f"e{e}_q"
        
        # 31. Rasyonel zincir
        k = e + 2
        stem = f"(1 - 1/{k}) · (1 - 1/{k+1}) · (1 - 1/{k+2}) · ... · (1 - 1/{k+7})\n\nİşleminin sonucu kaçtır?"
        ans = f"{k-1}/{k+7}"
        dists = [f"1/{k+7}", f"{k}/{k+7}", f"2/{k+7}", f"{k-1}/{k+6}"]
        sol = f"Payda ve paylar çapraz sadeleşir. İlk kesrin payı ({k-1}), son kesrin paydası ({k+7}) kalır. Sonuç: {ans}."
        qs.append(make_q(f"{base_id}31", "Matematik", stem, ans, dists, sol, e + 0))

        # 32. Devirli ondalık
        from fractions import Fraction
        f_val = Fraction(11 * e, 90)
        ans = f"{f_val.numerator}/{f_val.denominator}"
        dists = [f"{e}/9", f"{e}/10", f"{10*e}/99", f"{e+1}/90"]
        if ans in dists:
            dists.remove(ans)
            dists.append(f"{f_val.numerator+1}/{f_val.denominator}")
        stem = f"0,{e}̅ + 0,0{e}̅ işleminin sonucu olan en sade rasyonel kesir aşağıdakilerden hangisidir?"
        sol = f"0,{e}̅ = {e}/9 ve 0,0{e}̅ = {e}/90'dır. Payda eşitlenirse: ({10*e} + {e})/90 = {11*e}/90 = {ans}."
        qs.append(make_q(f"{base_id}32", "Matematik", stem, ans, dists, sol, e + 1))

        # 33. Ardışık sayılar
        step33 = 10 + e * 4
        total33 = 5 * step33
        stem = f"Ardışık 5 çift tam sayının toplamı {total33} olduğuna göre, bu sayıların en büyüğü ile en küçüğünün çarpımı kaçtır?"
        min_n = step33 - 4
        max_n = step33 + 4
        ans = str(min_n * max_n)
        dists = [str((min_n-2)*(max_n-2)), str(min_n*max_n + 16), str(min_n*max_n - 16), str(min_n * (max_n-2))]
        sol = f"Ortanca sayı {total33} / 5 = {step33}'tür. Çift sayılar: {step33-4}, {step33-2}, {step33}, {step33+2}, {step33+4}'tür. En küçük {min_n}, en büyük {max_n}'dir. Çarpımları: {min_n} · {max_n} = {ans}."
        qs.append(make_q(f"{base_id}33", "Matematik", stem, ans, dists, sol, e + 2))

        # 34. Asal sayılar ve aralarında asallık
        a34 = 2 * e + 3
        b34 = 3 * e + 5
        stem = f"(2a - 1) ile (b + {e}) sayıları aralarında asaldır.\n\n(2a - 1) / (b + {e}) = {2*a34} / {2*b34}\n\nolduğuna göre a + b toplamı kaçtır?"
        ans_a = (a34 + 1) // 2
        ans_b = b34 - e
        ans = str(ans_a + ans_b)
        dists = [str(ans_a + ans_b + 2), str(ans_a + ans_b - 2), str(ans_a + ans_b + 4), str(ans_a + ans_b - 3)]
        sol = f"Sayılar aralarında asal olduğundan kesir en sade hale getirilir: {2*a34}/{2*b34} = {a34}/{b34}. Buradan 2a - 1 = {a34} => a = {ans_a}; b + {e} = {b34} => b = {ans_b}. Toplam: {ans_a} + {ans_b} = {ans}."
        qs.append(make_q(f"{base_id}34", "Matematik", stem, ans, dists, sol, e + 3))

        # 35. Bölünebilme
        # Unique number per exam
        prefixes = [5, 6, 7, 8, 4, 3, 2, 9, 1, 5]
        pfx = prefixes[e-1]
        last_digits = [32, 24, 16, 52, 72, 84, 96, 64, 48, 28]
        ld = last_digits[e-1]
        # Number is pfx * 1000 + a * 100 + ld
        # Sum of digits: pfx + a + (ld//10) + (ld%10)
        s_base = pfx + (ld // 10) + (ld % 10)
        rem = (e % 5) + 1
        target_a = (rem - s_base) % 9
        if target_a < 0: target_a += 9
        stem = f"Dört basamaklı {pfx}a{ld} sayısı 4 ile tam bölünmektedir. Bu sayının 9 ile bölümünden kalan {rem} olduğuna göre, a rakamı kaçtır?"
        ans = str(target_a)
        dists = [str((target_a + 2) % 10), str((target_a + 5) % 10), str((target_a + 7) % 10), str((target_a + 3) % 10)]
        sol = f"Son iki basamak {ld} olup 4'e tam bölünür. 9 ile bölünebilmede rakamlar toplamı: {pfx} + a + {ld//10} + {ld%10} = {s_base} + a. {s_base} + a = 9k + {rem} eşitliğini sağlayan rakam a = {ans}'dir."
        qs.append(make_q(f"{base_id}35", "Matematik", stem, ans, dists, sol, e + 4))

        # 36. EBOB - EKOK
        m1 = 20 + e * 4
        m2 = 30 + e * 6
        import math
        eb = math.gcd(m1, m2)
        agac = 2 * (m1 // eb + m2 // eb)
        stem = f"Kenar uzunlukları {m1} m ve {m2} m olan dikdörtgen şeklindeki {e}. parsel bahçenin çevresine köşelere de dikilmek üzere eşit aralıklarla fidan dikilecektir. En az kaç fidan gerekir?"
        ans = str(agac)
        dists = [str(agac + 4), str(agac - 4), str(agac + 2), str(agac * 2)]
        sol = f"Fidan aralığı EBOB({m1}, {m2}) = {eb} metredir. Çevre = 2 · ({m1} + {m2}) = {2*(m1+m2)} m. Fidan sayısı = {2*(m1+m2)} / {eb} = {ans} fidan."
        qs.append(make_q(f"{base_id}36", "Matematik", stem, ans, dists, sol, e + 0))

        # 37. Faktöriyel
        fn = e + 3
        stem = f"({fn+2}! - {fn+1}!) / {fn}! kesrinin sayısal değeri kaçtır?"
        ans_num = (fn + 1) ** 2
        ans = str(ans_num)
        dists = [str(ans_num - (fn+1)), str(ans_num + (fn+1)), str((fn+2)*(fn+1)), str(ans_num - 1)]
        sol = f"{fn+1}! ortak parantezine alınır: {fn+1}! · ({fn+2} - 1) / {fn}! = ({fn+1} · {fn}! · {fn+1}) / {fn}! = ({fn+1})² = {ans_num}."
        qs.append(make_q(f"{base_id}37", "Matematik", stem, ans, dists, sol, e + 1))

        # 38. Basit Eşitsizlikler
        low = -e
        high = e + 3
        stem = f"x bir gerçel sayı olmak üzere,\n{low} < x < {high}\nolduğuna göre 3x - {e+2} ifadesinin alabileceği EN KÜÇÜK tam sayı değeri kaçtır?"
        min_real = 3 * low - (e + 2)
        ans_val = min_real + 1
        ans = str(ans_val)
        dists = [str(min_real), str(ans_val + 1), str(ans_val - 2), str(ans_val + 2)]
        sol = f"Eşitsizlik 3 ile çarpılır: {3*low} < 3x < {3*high}. {e+2} çıkarılır: {min_real} < 3x - {e+2} < {3*high - (e+2)}. Alabileceği en küçük tam sayı değeri {ans_val}'dir."
        qs.append(make_q(f"{base_id}38", "Matematik", stem, ans, dists, sol, e + 2))

        # 39. Mutlak Değer
        val39 = 5 + e * 2
        c_shift = e * 2
        stem = f"|2x - {2 * c_shift}| = {2 * val39} denklemini sağlayan x gerçel sayılarının toplamı kaçtır?"
        # 2x - 2c = 2v => x = c + v
        # 2x - 2c = -2v => x = c - v
        # Toplam = 2c
        ans = str(2 * c_shift)
        dists = [str(val39), str(2 * val39), str(c_shift), str(2 * c_shift + 4)]
        sol = f"2x - {2*c_shift} = {2*val39} => x₁ = {c_shift + val39} ve 2x - {2*c_shift} = -{2*val39} => x₂ = {c_shift - val39}. Kökler toplamı x₁ + x₂ = {2*c_shift}'dir."
        qs.append(make_q(f"{base_id}39", "Matematik", stem, ans, dists, sol, e + 3))

        # 40. Üslü Sayılar
        u = e + 2
        stem = f"(3^{u+2} - 3^{u+1} + 3^{u}) / 3^{u-1} işleminin sonucu kaçtır?"
        ans = "21"
        dists = ["18", "24", "27", "15"]
        # To vary the answer across exams:
        base_prime = [2, 3, 2, 5, 2, 3, 2, 4, 3, 2][e-1]
        if base_prime == 2:
            stem = f"(2^{e+4} - 2^{e+2} + 2^{e+1}) / 2^{e}\n\nİşleminin sonucu kaçtır?"
            # 2^e * (16 - 4 + 2) / 2^e = 14
            ans = "14"
            dists = ["12", "16", "18", "10"]
            sol = f"2^e parantezine alınırsa: 2^e · (2⁴ - 2² + 2¹) / 2^e = 16 - 4 + 2 = 14."
        elif base_prime == 3:
            stem = f"(3^{e+3} - 3^{e+1}) / 3^{e}\n\nİşleminin sonucu kaçtır?"
            # 3^e * (27 - 3) / 3^e = 24
            ans = "24"
            dists = ["21", "27", "18", "30"]
            sol = f"3^e parantezine alınırsa: 3^e · (3³ - 3¹) / 3^e = 27 - 3 = 24."
        elif base_prime == 5:
            stem = f"(5^{e+2} - 5^{e+1}) / 5^{e}\n\nİşleminin sonucu kaçtır?"
            # 25 - 5 = 20
            ans = "20"
            dists = ["15", "25", "30", "10"]
            sol = f"5^e parantezine alınırsa: 5^e · (5² - 5¹) / 5^e = 25 - 5 = 20."
        else:
            stem = f"(4^{e+2} - 4^{e+1}) / 4^{e}\n\nİşleminin sonucu kaçtır?"
            # 16 - 4 = 12
            ans = "12"
            dists = ["10", "16", "8", "14"]
            sol = f"4^e parantezine alınırsa: 4^e · (4² - 4¹) / 4^e = 16 - 4 = 12."
        qs.append(make_q(f"{base_id}40", "Matematik", stem, ans, dists, sol, e + 4))

        # 41. Köklü Sayılar
        diff_sq = [
            ("√2 - 1", "√2 + 1", "2 - 1 = 1"),
            ("√3 - √2", "√3 + √2", "3 - 2 = 1"),
            ("2 - √3", "2 + √3", "4 - 3 = 1"),
            ("√5 - 2", "√5 + 2", "5 - 4 = 1"),
            ("√5 - √3", "(√5 + √3)/2", "5 - 3 = 2"),
            ("√6 - √5", "√6 + √5", "6 - 5 = 1"),
            ("√7 - √6", "√7 + √6", "7 - 6 = 1"),
            ("√10 - 3", "√10 + 3", "10 - 9 = 1"),
            ("3 - √8", "3 + 2√2", "9 - 8 = 1"),
            ("√11 - √10", "√11 + √10", "11 - 10 = 1")
        ]
        pair = diff_sq[e-1]
        stem = f"1 / ({pair[0]}) ifadesinin paydasını rasyonel yapan işlem sonucunda elde edilen ifade nedir?"
        ans = pair[1]
        dists = [pair[0], f"2({pair[0]})", f"-({pair[1]})", f"1/({pair[1]})"]
        sol = f"Pay ve payda eşlenik olan ({pair[1]}) ile çarpılır. Paydada iki kare farkından ({pair[2]}) kalır. Sonuç: {ans}."
        qs.append(make_q(f"{base_id}41", "Matematik", stem, ans, dists, sol, e + 0))

        # 42. Çarpanlara Ayırma
        c_val = 100 + e * 7
        stem = f"({c_val + 2}² - {c_val - 2}²) / {c_val} işleminin sonucu kaçtır?"
        # (c+2 - c+2)(c+2 + c-2) = 4 * 2c = 8c. / c = 8
        ans = "8"
        dists = ["4", "16", "2", str(c_val)]
        sol = f"İki kare farkı özdeşliği: a² - b² = (a - b)(a + b). ({c_val+2 - (c_val-2)}) · ({c_val+2 + c_val-2}) = 4 · (2 · {c_val}) = 8 · {c_val}. {c_val}'a bölünürse sonuç 8 bulunur."
        qs.append(make_q(f"{base_id}42", "Matematik", stem, ans, dists, sol, e + 1))

        # 43. Oran - Orantı
        w_work = 60 + e * 12
        w_init = 4
        w_days = w_work // w_init
        new_w = 6
        new_d = w_work // new_w
        stem = f"Aynı kapasitede {w_init} ustanın {w_days} günde tamamladığı {e}. etap inşaat işini, usta sayısı {new_w}'ya çıkarılırsa kaç günde tamamlarlar?"
        ans = str(new_d)
        dists = [str(new_d + 2), str(new_d - 2), str(new_d + 4), str(new_d - 3)]
        sol = f"İşçi sayısı ile bitirme süresi ters orantılıdır: {w_init} · {w_days} = {new_w} · x => {w_work} = {new_w}x => x = {new_d} gün."
        qs.append(make_q(f"{base_id}43", "Matematik", stem, ans, dists, sol, e + 2))

        # 44. Sayı Problemleri
        front = 10 + e * 3
        back = 15 + e * 2
        gap = e + 2
        stem = f"Bir tiyatro bileti kuyruğunda Berk baştan {front}. sırada, Can ise sondan {back}. sıradadır. Berk gişeye daha yakın olup aralarında {gap} kişi olduğuna göre kuyrukta toplam kaç kişi vardır?"
        tot_q = front + gap + back
        ans = str(tot_q)
        dists = [str(tot_q - 2), str(tot_q + 2), str(tot_q - 4), str(tot_q + 3)]
        sol = f"Berk gişeye daha yakın olduğundan toplam kişi sayısı = {front} + {gap} + {back} = {tot_q} kişidir."
        qs.append(make_q(f"{base_id}44", "Matematik", stem, ans, dists, sol, e + 3))

        # 45. Kesir Problemleri
        depo_cap = 70 + e * 35
        stem = f"Hacmi tam olarak bilinmeyen bir su deposunun 3/7'si doludur. Depoya {depo_cap // 7 * 2} litre su eklendiğinde deponun 5/7'si dolu olmaktadır. Buna göre bu deponun toplam hacmi kaç litredir?"
        ans = str(depo_cap)
        dists = [str(depo_cap - 35), str(depo_cap + 35), str(depo_cap + 70), str(depo_cap - 70)]
        sol = f"Deponun hacmi V olsun. 5/7 V - 3/7 V = 2/7 V = {depo_cap // 7 * 2} => V/7 = {depo_cap // 7} => V = {depo_cap} litre."
        qs.append(make_q(f"{base_id}45", "Matematik", stem, ans, dists, sol, e + 4))

        # 46. Yaş Problemleri
        c_age = 5 + e
        m_age = 25 + e * 3
        # m_age + t = 3 * (c_age + t) => m_age - 3*c_age = 2t
        diff = m_age - 3 * c_age
        if diff % 2 != 0:
            m_age += 1
            diff = m_age - 3 * c_age
        t_ans = diff // 2
        if t_ans <= 0:
            t_ans = 4
            m_age = 3 * (c_age + t_ans) - t_ans
        stem = f"Bir babanın bugünkü yaşı {m_age}, oğlunun bugünkü yaşı {c_age}'dir. Kaç yıl sonra babanın yaşı oğlunun yaşının 3 katı olacaktır?"
        ans = str(t_ans)
        dists = [str(t_ans + 2), str(t_ans + 1), str(t_ans + 3), str(t_ans + 4)]
        sol = f"t yıl sonra: {m_age} + t = 3 · ({c_age} + t) => {m_age} + t = {3*c_age} + 3t => 2t = {m_age - 3*c_age} => t = {t_ans} yıl sonra."
        qs.append(make_q(f"{base_id}46", "Matematik", stem, ans, dists, sol, e + 0))

        # 47. Hız - Yol - Zaman
        v1 = 50 + e * 5
        v2 = 70 + e * 5
        t_time = 2 + (e % 3)
        dist_km = (v1 + v2) * t_time
        stem = f"Aralarındaki kara yolu mesafesi {dist_km} km olan iki istasyondan aynı anda birbirlerine doğru yola çıkan iki trenin hızları saatte {v1} km ve {v2} km'dir. Bu trenler kaç saat sonra karşılaşır?"
        ans = str(t_time)
        dists = [str(t_time + 1), str(t_time + 2), str(t_time + 3), str(t_time + 4)]
        sol = f"Karşılıklı hareketlerde hızlar toplanır: V = {v1} + {v2} = {v1+v2} km/sa. Süre t = {dist_km} / {v1+v2} = {ans} saat."
        qs.append(make_q(f"{base_id}47", "Matematik", stem, ans, dists, sol, e + 1))

        # 48. İşçi Problemleri
        t_can = 8 + e * 2
        t_mert = 2 * t_can
        # together = (t_can * 2*t_can) / (3*t_can) = 2*t_can / 3
        # make t_can divisible by 3:
        t_can = 6 + e * 3
        t_mert = 2 * t_can
        tog = (t_can * t_mert) // (t_can + t_mert)
        stem = f"Bir yazılım projesini Selim tek başına {t_can} günde, Kerem ise tek başına {t_mert} günde tamamlayabilmektedir. İkisi birlikte çalışırlarsa proje kaç günde biter?"
        ans = str(tog)
        dists = [str(tog + 2), str(tog - 1 if tog > 1 else tog + 5), str(tog + 3), str(tog * 2)]
        sol = f"1 günde Selim 1/{t_can}'ini, Kerem 1/{t_mert}'sini yapar. Birlikte 1 günde: 1/{t_can} + 1/{t_mert} = 3/{t_mert} = 1/{tog}. Tamamı {tog} günde biter."
        qs.append(make_q(f"{base_id}48", "Matematik", stem, ans, dists, sol, e + 2))

        # 49. Yüzde & Kâr-Zarar
        cost = 150 + e * 30
        k_pct = 20
        stem = f"Maliyet fiyatı {cost} TL olan bir kaban %{k_pct} kâr ile etiketlendirildikten sonra etiket fiyatı üzerinden %10 indirim yapılarak satılıyor. Bu satıştan elde edilen net kâr kaç TL'dir?"
        etk = cost * 120 // 100
        sat = etk * 90 // 100
        net_k = sat - cost
        ans = str(net_k)
        dists = [str(net_k + 5), str(net_k - 4), str(net_k + 10), str(net_k - 2)]
        sol = f"Etiket fiyatı = {cost} · 1,20 = {etk} TL. İndirimli satış = {etk} · 0,90 = {sat} TL. Net kâr = {sat} - {cost} = {net_k} TL."
        qs.append(make_q(f"{base_id}49", "Matematik", stem, ans, dists, sol, e + 3))

        # 50. Karışım
        m1_k = 100 + e * 20
        m2_k = 100
        stem = f"Tuz oranı %{10 + e} olan {m1_k} gram tuzlu su ile tuz oranı %30 olan {m2_k} gram tuzlu su karıştırılıyor. Yeni karışımın tuz yüzdesi kaçtır?"
        tuz_tot = m1_k * (10 + e) + m2_k * 30
        tot_gram = m1_k + m2_k
        ans_pct = round(tuz_tot / tot_gram, 1)
        ans = f"%{ans_pct}".replace('.0', '')
        dists = [f"%{round(ans_pct + 2.0, 1)}".replace('.0', ''), f"%{round(ans_pct - 2.0, 1)}".replace('.0', ''), f"%{round(ans_pct + 4.0, 1)}".replace('.0', ''), f"%{round(ans_pct - 3.0, 1)}".replace('.0', '')]
        sol = f"Toplam tuz = ({m1_k} · {10+e} + {m2_k} · 30) / 100 gram. Toplam ağırlık = {tot_gram} gram. Yüzde = ({tuz_tot} / {tot_gram}) = {ans}."
        qs.append(make_q(f"{base_id}50", "Matematik", stem, ans, dists, sol, e + 4))

        # 51. Kümeler
        s_A = 12 + e * 2
        s_B = 16 + e * 2
        s_kes = 4 + e
        s_bir = s_A + s_B - s_kes
        stem = f"A ve B kümeleri için s(A) = {s_A}, s(B) = {s_B} ve kesişim kümesinin eleman sayısı s(A ∩ B) = {s_kes} olduğuna göre s(A ∪ B) kaçtır?"
        ans = str(s_bir)
        dists = [str(s_bir + 2), str(s_bir - 2), str(s_bir + s_kes), str(s_A + s_B)]
        sol = f"s(A ∪ B) = s(A) + s(B) - s(A ∩ B) = {s_A} + {s_B} - {s_kes} = {ans}."
        qs.append(make_q(f"{base_id}51", "Matematik", stem, ans, dists, sol, e + 0))

        # 52. Fonksiyonlar
        fa = e + 1
        fb = 2 * e + 3
        stem = f"Gerçel sayılarda tanımlı f(x) = {fa}x - {fb} fonksiyonu için f(5) - f(2) farkı kaçtır?"
        ans = str(3 * fa)
        dists = [str(3 * fa + 2), str(fa), str(2 * fa), str(3 * fa - 1)]
        sol = f"f(5) - f(2) = ({fa}·5 - {fb}) - ({fa}·2 - {fb}) = {fa} · (5 - 2) = {ans}."
        qs.append(make_q(f"{base_id}52", "Matematik", stem, ans, dists, sol, e + 1))

        # 53. Modüler Aritmetik
        day_names = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]
        start_day_idx = (e * 3) % 7
        start_day = day_names[start_day_idx]
        add_days = 95 + e * 11
        target_day = day_names[(start_day_idx + add_days) % 7]
        stem = f"Bir nöbet çizelgesinde ilk nöbetini {start_day} günü tutan bir sağlık görevlisi, {add_days} gün sonraki nöbetini hangi gün tutar?"
        ans = target_day
        dists = [d for d in day_names if d != target_day][:4]
        sol = f"{add_days} sayısının 7 ile bölümünden kalan: {add_days % 7}. {start_day} gününden {add_days % 7} gün sonrası {ans} olur."
        qs.append(make_q(f"{base_id}53", "Matematik", stem, ans, dists, sol, e + 2))

        # 54. Permütasyon
        p_n = 4 + e
        p_val = p_n * (p_n - 1) * (p_n - 2)
        stem = f"{p_n} adayın yarıştığı bir personel mülakatında birinci, ikinci ve üçüncü dereceler kaç farklı biçimde oluşabilir?"
        ans = str(p_val)
        dists = [str(p_val - 10), str(p_val + 15), str(p_val // 2), str(p_val + 20)]
        sol = f"P({p_n}, 3) = {p_n} · {p_n-1} · {p_n-2} = {ans} farklı şekilde oluşur."
        qs.append(make_q(f"{base_id}54", "Matematik", stem, ans, dists, sol, e + 3))

        # 55. Kombinasyon
        c_tot = 6 + e
        c_val = (c_tot * (c_tot - 1) * (c_tot - 2)) // 6
        stem = f"{c_tot} kişilik bir uzman kurulundan oluşturulacak 3 kişilik denetleme heyeti kaç farklı şekilde seçilebilir?"
        ans = str(c_val)
        dists = [str(c_val + 5), str(c_val - 5), str(c_val * 2), str(c_val + 10)]
        sol = f"C({c_tot}, 3) = ({c_tot} · {c_tot-1} · {c_tot-2}) / 6 = {ans} farklı seçim yapılabilir."
        qs.append(make_q(f"{base_id}55", "Matematik", stem, ans, dists, sol, e + 4))

        # 56. Olasılık
        prob_scenarios = [
            ("İki zar havaya atıldığında üst yüze gelen sayılar toplamının 9 olma olasılığı kaçtır?", "1/9", ["1/6", "1/12", "5/36", "1/4"], "Toplamın 9 olduğu durumlar: (3,6), (4,5), (5,4), (6,3) 4 tanedir. Olasılık = 4/36 = 1/9."),
            ("Bir torbada 4 kırmızı, 5 mavi bilye vardır. Rastgele çekilen bir bilyenin mavi olma olasılığı kaçtır?", "5/9", ["4/9", "1/2", "5/8", "1/9"], "Mavi sayısı 5, toplam bilye sayısı 4 + 5 = 9. Olasılık = 5/9."),
            ("İki zar atıldığında üst yüze gelen sayıların ikisinin de tek sayı olma olasılığı kaçtır?", "1/4", ["1/2", "1/3", "1/6", "3/8"], "Bir zarın tek gelme olasılığı 3/6 = 1/2'dir. İkisinin de tek gelmesi = 1/2 · 1/2 = 1/4."),
            ("3 madeni para havaya atıldığında en az ikisinin tura gelme olasılığı kaçtır?", "1/2", ["3/8", "5/8", "1/4", "3/4"], "Olası durumlar (TTT, TTY, TYT, YTT) = 4 durum. Tüm durumlar 2³ = 8. Olasılık = 4/8 = 1/2."),
            ("Bir torbada 3 beyaz, 4 siyah, 5 kırmızı bilye vardır. Çekilen bir bilyenin siyah OLMAMA olasılığı kaçtır?", "2/3", ["1/3", "5/12", "7/12", "3/4"], "Toplam bilye = 12. Siyah olmayan (beyaz + kırmızı) = 3 + 5 = 8 bilye. Olasılık = 8/12 = 2/3."),
            ("İki zar atıldığında üst yüze gelen sayılar toplamının 10 veya 10'dan büyük olma olasılığı kaçtır?", "1/6", ["1/12", "5/36", "1/9", "7/36"], "İstenen durumlar: (4,6), (5,5), (6,4), (5,6), (6,5), (6,6) toplam 6 durum. Olasılık = 6/36 = 1/6."),
            ("5 kız ve 4 erkek öğrencinin bulunduğu bir gruptan rastgele seçilen 2 kişinin ikisinin de kız olma olasılığı kaçtır?", "5/18", ["10/36", "5/9", "1/3", "2/9"], "C(5,2) / C(9,2) = 10 / 36 = 5/18."),
            ("Bir çift zar atıldığında zarların üzerindeki sayıların birbirinden farklı gelme olasılığı kaçtır?", "5/6", ["1/6", "2/3", "7/12", "11/12"], "Aynı gelme durumları (1,1)...(6,6) 6 tanedir (olasılık 6/36 = 1/6). Farklı gelme olasılığı = 1 - 1/6 = 5/6."),
            ("4 doktor ve 3 hemşire arasından seçilen bir kişinin hemşire olma olasılığı kaçtır?", "3/7", ["4/7", "3/4", "1/2", "1/3"], "İstenen hemşire sayısı 3, toplam sağlık çalışanı sayısı 7'dir. Olasılık = 3/7."),
            ("Bir torbada 6 sarı, 4 lacivert top vardır. Rastgele çekilen iki topun ikisinin de lacivert olma olasılığı kaçtır?", "2/15", ["1/10", "4/15", "1/5", "3/20"], "C(4,2) / C(10,2) = 6 / 45 = 2/15.")
        ]
        p_sc = prob_scenarios[e-1]
        qs.append(make_q(f"{base_id}56", "Matematik", p_sc[0], p_sc[1], p_sc[2], p_sc[3], e + 0))

        # 57. Geometri: Üçgende Açılar
        ang_a = 35 + e * 4
        ang_b = 65 - e * 2
        ang_c = 180 - (ang_a + ang_b)
        stem = f"Bir KLM üçgeninde m(K) = {ang_a}° ve m(L) = {ang_b}° olduğuna göre M açısının ölçüsü m(M) kaç derecedir?"
        ans = f"{ang_c}°"
        dists = [f"{ang_c + 10}°", f"{ang_c - 10}°", f"{ang_c + 15}°", f"{ang_c - 15}°"]
        sol = f"Üçgenin iç açıları toplamı 180°'dir. m(M) = 180° - ({ang_a}° + {ang_b}°) = {ans}."
        qs.append(make_q(f"{base_id}57", "Matematik", stem, ans, dists, sol, e + 1))

        # 58. Geometri: Pisagor ve Özel Üçgenler
        triangles = [
            ("Dik kenarları 6 cm ve 8 cm olan dik üçgenin hipotenüs uzunluğu kaç cm'dir?", "10 cm", ["12 cm", "14 cm", "9 cm", "11 cm"], "3-4-5 özel üçgeninin 2 katı (6-8-10): Hipotenüs = 10 cm."),
            ("Hipotenüs uzunluğu 13 cm ve bir dik kenarı 5 cm olan dik üçgenin diğer dik kenarı kaç cm'dir?", "12 cm", ["10 cm", "11 cm", "8 cm", "9 cm"], "5-12-13 özel dik üçgeni kuralından diğer dik kenar 12 cm'dir."),
            ("Hipotenüs uzunluğu 25 cm ve bir dik kenarı 7 cm olan dik üçgenin diğer dik kenarı kaç cm'dir?", "24 cm", ["20 cm", "22 cm", "18 cm", "23 cm"], "7-24-25 özel dik üçgeni kuralından diğer dik kenar 24 cm'dir."),
            ("Hipotenüs uzunluğu 17 cm ve bir dik kenarı 8 cm olan dik üçgenin diğer dik kenarı kaç cm'dir?", "15 cm", ["12 cm", "14 cm", "16 cm", "13 cm"], "8-15-17 özel dik üçgeni kuralından diğer dik kenar 15 cm'dir."),
            ("Bir 30°-60°-90° dik üçgeninde 30°'lik açının karşısındaki kenar 6 cm ise hipotenüs uzunluğu kaç cm'dir?", "12 cm", ["6√3 cm", "18 cm", "10 cm", "8√3 cm"], "30-60-90 üçgeninde hipotenüs, 30°'nin karşısındaki kenarın 2 katıdır: 2 · 6 = 12 cm."),
            ("Bir 45°-45°-90° ikizkenar dik üçgeninde dik kenarlar 7 cm ise hipotenüs kaç cm'dir?", "7√2 cm", ["14 cm", "7√3 cm", "10 cm", "8√2 cm"], "İkizkenar dik üçgende hipotenüs dik kenarın √2 katıdır: 7√2 cm."),
            ("Dik kenarları 9 cm ve 12 cm olan dik üçgenin hipotenüs uzunluğu kaç cm'dir?", "15 cm", ["18 cm", "20 cm", "16 cm", "14 cm"], "3-4-5 üçgeninin 3 katı (9-12-15): Hipotenüs = 15 cm."),
            ("Bir eşkenar üçgenin bir kenar uzunluğu 8 cm olduğuna göre alanı kaç cm²'dir?", "16√3 cm²", ["32 cm²", "64 cm²", "12√3 cm²", "24 cm²"], "Eşkenar üçgenin alanı = (a² · √3) / 4 = (64 · √3) / 4 = 16√3 cm²."),
            ("Bir 30°-60°-90° üçgeninde 90°'nin karşısı 10 cm ise 60°'nin karşısındaki kenar kaç cm'dir?", "5√3 cm", ["5 cm", "10√3 cm", "15 cm", "8 cm"], "30° karşısı 10/2 = 5 cm, 60° karşısı 5√3 cm'dir."),
            ("Dik kenarları 12 cm ve 16 cm olan dik üçgenin alanı kaç cm²'dir?", "96 cm²", ["192 cm²", "84 cm²", "108 cm²", "72 cm²"], "Dik üçgenin alanı = (dik kenarlar çarpımı) / 2 = (12 · 16) / 2 = 96 cm².")
        ]
        tr = triangles[e-1]
        qs.append(make_q(f"{base_id}58", "Matematik", tr[0], tr[1], tr[2], tr[3], e + 2))

        # 59. Geometri: Dörtgenler
        rec_a = 6 + e * 2
        rec_b = 12 + e * 3
        rec_area = rec_a * rec_b
        stem = f"Kenar uzunlukları {rec_a} cm ve {rec_b} cm olan bir ABCD dikdörtgeninin alanı kaç santimetrekaredir?"
        ans = f"{rec_area} cm²"
        dists = [f"{rec_area + 18} cm²", f"{rec_area - 18} cm²", f"{2*(rec_a+rec_b)} cm²", f"{rec_area + 36} cm²"]
        sol = f"Dikdörtgen Alanı = a · b = {rec_a} · {rec_b} = {rec_area} cm²."
        qs.append(make_q(f"{base_id}59", "Matematik", stem, ans, dists, sol, e + 3))

        # 60. Geometri: Çember & Daire
        r_circle = 2 + e
        c_area = r_circle * r_circle
        stem = f"Yarıçap uzunluğu r = {r_circle} cm olan bir çemberin çevrelediği dairenin alanı kaç π cm²'dir?"
        ans = f"{c_area}π"
        dists = [f"{2*r_circle}π", f"{c_area + 7}π", f"{c_area - 3}π", f"{4*r_circle}π"]
        sol = f"Daire alanı = π · r² = π · {r_circle}² = {c_area}π cm²."
        qs.append(make_q(f"{base_id}60", "Matematik", stem, ans, dists, sol, e + 4))

        all_exams_math.append(qs)
        
    return all_exams_math

if __name__ == '__main__':
    exams = build_all_math()
    all_qs = [q for exam in exams for q in exam]
    print(f"Total math questions: {len(all_qs)}")
    unique_texts = len(set(q['text'] for q in all_qs))
    print(f"Unique math texts: {unique_texts}")
    import collections
    letter_counts = collections.Counter(q['correct'] for q in all_qs)
    print(f"Letter distribution: {letter_counts}")
