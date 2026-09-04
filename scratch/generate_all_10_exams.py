import json, sys, os, random
sys.stdout.reconfigure(encoding='utf-8')

print("10 Deneme İçin Büyük Veri Üreteci Başlatılıyor...")

# Deneme 1'i data.js'den oku ve koru
with open(r'c:\Users\oktay\Desktop\kpss\data.js', 'r', encoding='utf-8') as f:
    raw = f.read()

json_str = raw[raw.find('{'):raw.rfind('}')+1]
full_data = json.loads(json_str)

# Deneme 1'i al
exam_1 = full_data['mockExams'][0]
print(f"Deneme 1 mevcut: {len(exam_1['questions'])} soru (KORUNUYOR).")
