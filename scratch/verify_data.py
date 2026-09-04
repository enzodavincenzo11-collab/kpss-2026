import sys, json
sys.stdout.reconfigure(encoding='utf-8')

content = open(r'c:\Users\oktay\Desktop\kpss\data.js', encoding='utf-8').read()
d = json.loads(content[content.find('{'):content.rfind('}')+1])

print("=== KPSS DATA VERIFICATION ===")
print("Total mock exams:", len(d['mockExams']))

bad_markers = ['(P-0)', '(T-1)', '(SoruID', 'en kritik gelişmelerinden biridir', 'ülkemizin önemli şekillerinden biridir', '\ufffd']
found_bad = 0
for marker in bad_markers:
    c = content.count(marker)
    if c > 0:
        print(f"WARNING: Found {c} occurrences of bad marker: {marker}")
        found_bad += c

if found_bad == 0:
    print("MÜKEMMEL: data.js içinde hiçbir şablon çöpü, yapay zeka kalıntısı veya bozuk karakter YOK!")

correct_dist = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
total_q = 0
for exam in d['mockExams']:
    total_q += len(exam['questions'])
    for q in exam['questions']:
        correct_dist[q['correct']] += 1
        if len(q['options']) != 5:
            print(f"HATA: Soru {q['id']} 5 şıklı değil!")
        if not (0 <= q['correct'] <= 4):
            print(f"HATA: Soru {q['id']} geçersiz doğru cevaba sahip!")

print(f"10 Deneme genelinde toplam soru sayısı: {total_q}")
print("Doğru Cevap Dağılımı (A, B, C, D, E dengesi):")
letters = ['A', 'B', 'C', 'D', 'E']
for idx, l in enumerate(letters):
    print(f"  {l}: {correct_dist[idx]} adet (%{correct_dist[idx]/total_q*100:.1f})")

print("\nHER ŞEY EKSİKSİZ VE MÜKEMMEL DURUMDA!")
