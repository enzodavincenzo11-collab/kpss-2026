import sys, json
sys.stdout.reconfigure(encoding='utf-8')

content = open(r'c:\Users\oktay\Desktop\kpss\data.js', encoding='utf-8').read()
d = json.loads(content[content.find('{'):content.rfind('}')+1])
exam1 = d['mockExams'][0]

answers = {}
correct_count = 0
wrong_count = 0
empty_count = 0

stats = {
    'Türkçe': {'d': 0, 'y': 0, 'b': 0, 'net': 0, 'total': 30},
    'Matematik': {'d': 0, 'y': 0, 'b': 0, 'net': 0, 'total': 30},
    'Tarih': {'d': 0, 'y': 0, 'b': 0, 'net': 0, 'total': 27},
    'Coğrafya': {'d': 0, 'y': 0, 'b': 0, 'net': 0, 'total': 18},
    'Vatandaşlık': {'d': 0, 'y': 0, 'b': 0, 'net': 0, 'total': 15}
}

for i, q in enumerate(exam1['questions']):
    qid = q['id']
    correct = q['correct']
    subj = q['subject']
    
    # Gerçekçi bir 90+ puan performansı simüle edelim:
    # 4 boş: 29 (Türkçe paragraf), 59 (Matematik geometri), 86 (Tarih çağdaş), 120 (Güncel)
    if i in [28, 58, 85, 119]:
        empty_count += 1
        stats[subj]['b'] += 1
        continue
    # 8 yanlış: çeldiricili sorular
    elif i in [11, 23, 44, 51, 69, 79, 94, 109]:
        wrong_opt = (correct + 1) % 5
        answers[qid] = wrong_opt
        wrong_count += 1
        stats[subj]['y'] += 1
    else:
        answers[qid] = correct
        correct_count += 1
        stats[subj]['d'] += 1

total_net = 0
for s, val in stats.items():
    net = val['d'] - (val['y'] / 4.0)
    val['net'] = net
    total_net += net

p94 = 40 + (total_net * 0.48)
if total_net <= 0: p94 = 0
if p94 > 100: p94 = 100

print(f"=== 1. DENEME SINAVI ÇÖZÜM RAPORU ===")
print(f"Toplam Soru  : 120")
print(f"Doğru Sayısı : {correct_count}")
print(f"Yanlış Sayısı: {wrong_count}")
print(f"Boş Sayısı   : {empty_count}")
print(f"Toplam Net   : {total_net:.2f}")
print(f"KPSS P94 Puanı: {p94:.2f}\n")

print("--- BRANŞ DETAYLARI ---")
for s, val in stats.items():
    print(f"{s:<12}: {val['total']} Soru | {val['d']} Doğru | {val['y']} Yanlış | {val['b']} Boş | Net: {val['net']:.2f}")

# Ayrıca bu çözümü JSON olarak kaydedelim ki isterse app.js'e bir otomatik doldurma fonksiyonu da ekleyebilelim:
simulated_state = {
    "examId": "deneme_1",
    "answers": answers,
    "timeRemaining": 24 * 60, # 130 dakikadan 24 dakika kalmış
    "isStarted": True,
    "isSubmitted": False
}

with open(r'c:\Users\oktay\Desktop\kpss\scratch\simulated_solve_deneme1.json', 'w', encoding='utf-8') as f:
    json.dump(simulated_state, f, ensure_ascii=False, indent=2)

print("\nSimülasyon durumu kaydedildi.")
