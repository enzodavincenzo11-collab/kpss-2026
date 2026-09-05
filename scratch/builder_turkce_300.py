import sys
sys.path.append('scratch')

from turkce_data_1 import deyimler, atasozleri, cok_anlamli, mecazlar, soz_obekleri
from turkce_data_2 import yazimlar, buyuk_harf, noktalama_paragraflar, ses_unlu, virgul_islev, ses_unsuz
from turkce_data_3 import yapi_qs, tamlamalar, zamirler, fiilimsiler, ogeler, cumle_turleri, cati
from turkce_data_4 import anlatim_bozuklugu, cumle_anlam_iliskileri, oznel_nesnel, ana_fikir, degilmemistir, akisi_bozan
from turkce_data_5 import ikiye_bolme, bosluk_doldurma, anlatim_bicimleri, anlatim_nitelikleri, sozel_mantik_1, sozel_mantik_2

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

def build_all_turkce():
    all_exams = []
    
    for e in range(1, 11):
        idx = e - 1
        qs = []
        base_id = f"e{e}_q"
        
        # 1. Deyim
        d = deyimler[idx]
        stem1 = f"\"{d[2]}\"\n\nBu cümledeki altı çizili deyimin kattığı anlam hangisidir?"
        dist1 = ["Önemsememek ve ertelemek", "Kendi çıkarlarını önde tutmak", "Başkalarının yönlendirmesiyle hareket etmek", "Zorluk karşısında pes etmek"]
        qs.append(make_q(f"{base_id}1", "Türkçe", stem1, d[1], dist1, f"'{d[0]}' deyimi '{d[1]}' anlamında kullanılır.", e + 0))

        # 2. Atasözü
        at = atasozleri[idx]
        stem2 = f"Aşağıdaki atasözlerinden hangisi '{at[2]}' düşüncesini öğütler?"
        dist2 = [a[0] for a in atasozleri if a[0] != at[0]][:4]
        qs.append(make_q(f"{base_id}2", "Türkçe", stem2, at[0], dist2, f"'{at[0]}' atasözü; {at[2]} düşüncesini öğütler.", e + 1))

        # 3. Çok anlamlılık
        ca = cok_anlamli[idx]
        qs.append(make_q(f"{base_id}3", "Türkçe", ca[1], ca[2], ca[3], ca[4], e + 2))

        # 4. Mecaz
        mc = mecazlar[idx]
        qs.append(make_q(f"{base_id}4", "Türkçe", mc[0], mc[1], mc[2], mc[3], e + 3))

        # 5. Söz öbeği
        so = soz_obekleri[idx]
        stem5 = f"\"{so[0]}\"\n\nBu sözle anlatılmak istenen temel düşünce nedir?"
        qs.append(make_q(f"{base_id}5", "Türkçe", stem5, so[1], so[2], so[3], e + 4))

        # 6. Yazım yanlışı (altı çizili)
        yz = yazimlar[idx]
        stem6 = f"{yz[0]}\n\nNumaralanmış altı çizili sözlerden hangisinin yazımı YANLIŞTIR?"
        qs.append(make_q(f"{base_id}6", "Türkçe", stem6, yz[1], yz[2], yz[3], e + 0))

        # 7. Büyük harf / eklerin yazımı
        bh = buyuk_harf[idx]
        qs.append(make_q(f"{base_id}7", "Türkçe", bh[0], bh[1], bh[2], bh[3], e + 1))

        # 8. Noktalama yay ayraç
        np = noktalama_paragraflar[idx]
        qs.append(make_q(f"{base_id}8", "Türkçe", np[0], np[1], np[2], np[3], e + 2))

        # 9. Virgül / noktalama işlevi
        vi = virgul_islev[idx]
        qs.append(make_q(f"{base_id}9", "Türkçe", vi[0], vi[1], vi[2], vi[3], e + 3))

        # 10. Ses olayı (ünlü)
        su = ses_unlu[idx]
        qs.append(make_q(f"{base_id}10", "Türkçe", su[0], su[1], su[2], su[3], e + 4))

        # 11. Ses olayı (ünsüz)
        sb = ses_unsuz[idx]
        qs.append(make_q(f"{base_id}11", "Türkçe", sb[0], sb[1], sb[2], sb[3], e + 0))

        # 12. Sözcükte yapı
        yp = yapi_qs[idx]
        qs.append(make_q(f"{base_id}12", "Türkçe", yp[0], yp[1], yp[2], yp[3], e + 1))

        # 13. Tamlamalar
        tm = tamlamalar[idx]
        qs.append(make_q(f"{base_id}13", "Türkçe", tm[0], tm[1], tm[2], tm[3], e + 2))

        # 14. Zamirler
        zm = zamirler[idx]
        qs.append(make_q(f"{base_id}14", "Türkçe", zm[0], zm[1], zm[2], zm[3], e + 3))

        # 15. Fiilimsiler
        fl = fiilimsiler[idx]
        qs.append(make_q(f"{base_id}15", "Türkçe", fl[0], fl[1], fl[2], fl[3], e + 4))

        # 16. Cümlenin ögeleri
        og = ogeler[idx]
        qs.append(make_q(f"{base_id}16", "Türkçe", og[0], og[1], og[2], og[3], e + 0))

        # 17. Cümle türleri
        ct = cumle_turleri[idx]
        qs.append(make_q(f"{base_id}17", "Türkçe", ct[0], ct[1], ct[2], ct[3], e + 1))

        # 18. Fiil çatısı
        cti = cati[idx]
        qs.append(make_q(f"{base_id}18", "Türkçe", cti[0], cti[1], cti[2], cti[3], e + 2))

        # 19. Anlatım bozukluğu
        ab = anlatim_bozuklugu[idx]
        qs.append(make_q(f"{base_id}19", "Türkçe", ab[0], ab[1], ab[2], ab[3], e + 3))

        # 20. Cümlede anlam ilişkisi
        ca_il = cumle_anlam_iliskileri[idx]
        qs.append(make_q(f"{base_id}20", "Türkçe", ca_il[0], ca_il[1], ca_il[2], ca_il[3], e + 4))

        # 21. Öznel / Nesnel
        on = oznel_nesnel[idx]
        qs.append(make_q(f"{base_id}21", "Türkçe", on[0], on[1], on[2], on[3], e + 0))

        # 22. Ana fikir
        af = ana_fikir[idx]
        qs.append(make_q(f"{base_id}22", "Türkçe", af[0], af[1], af[2], af[3], e + 1))

        # 23. Değinilmemiştir
        dg = degilmemistir[idx]
        qs.append(make_q(f"{base_id}23", "Türkçe", dg[0], dg[1], dg[2], dg[3], e + 2))

        # 24. Akışı bozan
        ab_q = akisi_bozan[idx]
        qs.append(make_q(f"{base_id}24", "Türkçe", ab_q[0], ab_q[1], ab_q[2], ab_q[3], e + 3))

        # 25. İkiye bölme
        ib = ikiye_bolme[idx]
        qs.append(make_q(f"{base_id}25", "Türkçe", ib[0], ib[1], ib[2], ib[3], e + 4))

        # 26. Boşluk doldurma
        bd = bosluk_doldurma[idx]
        qs.append(make_q(f"{base_id}26", "Türkçe", bd[0], bd[1], bd[2], bd[3], e + 0))

        # 27. Anlatım biçimleri
        ab_t = anlatim_bicimleri[idx]
        qs.append(make_q(f"{base_id}27", "Türkçe", ab_t[0], ab_t[1], ab_t[2], ab_t[3], e + 1))

        # 28. Anlatım nitelikleri
        an_n = anlatim_nitelikleri[idx]
        qs.append(make_q(f"{base_id}28", "Türkçe", an_n[0], an_n[1], an_n[2], an_n[3], e + 2))

        # 29. Sözel mantık 1
        sm1 = sozel_mantik_1[idx]
        qs.append(make_q(f"{base_id}29", "Türkçe", sm1[0], sm1[1], sm1[2], sm1[3], e + 3))

        # 30. Sözel mantık 2
        sm2 = sozel_mantik_2[idx]
        qs.append(make_q(f"{base_id}30", "Türkçe", sm2[0], sm2[1], sm2[2], sm2[3], e + 4))

        all_exams.append(qs)
        
    return all_exams

if __name__ == '__main__':
    exams = build_all_turkce()
    all_qs = [q for exam in exams for q in exam]
    print(f"Total turkce questions: {len(all_qs)}")
    unique_texts = len(set(q['text'] for q in all_qs))
    print(f"Unique turkce texts: {unique_texts}")
    import collections
    letter_counts = collections.Counter(q['correct'] for q in all_qs)
    print(f"Letter distribution: {letter_counts}")
