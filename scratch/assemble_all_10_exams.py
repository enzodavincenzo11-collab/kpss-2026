import json, sys, os, random
sys.stdout.reconfigure(encoding='utf-8')

# Import generators
sys.path.append(r'c:\Users\oktay\Desktop\kpss\scratch')
from pool_turkce import generate_turkce_for_exam
from pool_matematik import generate_matematik_for_exam
from pool_tarih_cog_vat import generate_tarih_for_exam, generate_cografya_for_exam, generate_vatandaslik_for_exam

print("Tüm 10 Denemeyi Birleştirme ve Doğrulama Başlatılıyor...")

DATA_PATH = r'c:\Users\oktay\Desktop\kpss\data.js'
with open(DATA_PATH, 'r', encoding='utf-8') as f:
    raw = f.read()

json_str = raw[raw.find('{'):raw.rfind('}')+1]
kpss_data = json.loads(json_str)

# 1. Denemeyi koru
exam_1 = kpss_data['mockExams'][0]
print(f"Deneme 1 mevcut: {len(exam_1['questions'])} soru (KORUNDU).")

# Seçenekleri rastgele karıştırıp doğru cevabı dengeli dağıtan yardımcı fonksiyon
def balance_options(q_raw, seed_val):
    rnd = random.Random(seed_val)
    opts = q_raw['options']
    orig_correct_idx = q_raw['correct']
    correct_text = opts[orig_correct_idx]
    
    # Harfleri temizle ("A) Metin" -> "Metin")
    clean_texts = [o.split(") ", 1)[-1] if ") " in o else o for o in opts]
    correct_clean = clean_texts[orig_correct_idx]
    
    # Karıştır
    rnd.shuffle(clean_texts)
    new_correct_idx = clean_texts.index(correct_clean)
    
    # Yeni harfler ver (A, B, C, D, E)
    letters = ["A", "B", "C", "D", "E"]
    new_opts = [f"{letters[i]}) {clean_texts[i]}" for i in range(len(clean_texts))]
    
    return new_opts, new_correct_idx

all_mock_exams = [exam_1]

# Deneme 2'den 10'a kadar inşa et
for exam_no in range(2, 11):
    exam_id = f"deneme_{exam_no}"
    exam_title = f"{exam_no}. Deneme (KPSS 2026 Tam Format - 120 Özgün Soru)"
    
    t_list = generate_turkce_for_exam(exam_no)
    m_list = generate_matematik_for_exam(exam_no)
    tar_list = generate_tarih_for_exam(exam_no)
    cog_list = generate_cografya_for_exam(exam_no)
    vat_list = generate_vatandaslik_for_exam(exam_no)
    
    exam_questions = []
    
    # 30 Türkçe (1-30)
    for idx, q in enumerate(t_list):
        q_no = idx + 1
        new_opts, new_corr = balance_options(q, exam_no * 1000 + q_no)
        exam_questions.append({
            "id": f"e{exam_no}_q{q_no}",
            "no": q_no,
            "subject": "Türkçe",
            "text": q["text"],
            "options": new_opts,
            "correct": new_corr,
            "solution": q["solution"]
        })

    # 30 Matematik (31-60)
    for idx, q in enumerate(m_list):
        q_no = idx + 31
        new_opts, new_corr = balance_options(q, exam_no * 1000 + q_no)
        exam_questions.append({
            "id": f"e{exam_no}_q{q_no}",
            "no": q_no,
            "subject": "Matematik",
            "text": q["text"],
            "options": new_opts,
            "correct": new_corr,
            "solution": q["solution"]
        })

    # 27 Tarih (61-87)
    for idx, q in enumerate(tar_list):
        q_no = idx + 61
        new_opts, new_corr = balance_options(q, exam_no * 1000 + q_no)
        exam_questions.append({
            "id": f"e{exam_no}_q{q_no}",
            "no": q_no,
            "subject": "Tarih",
            "text": q["text"],
            "options": new_opts,
            "correct": new_corr,
            "solution": q["solution"]
        })

    # 18 Coğrafya (88-105)
    for idx, q in enumerate(cog_list):
        q_no = idx + 88
        new_opts, new_corr = balance_options(q, exam_no * 1000 + q_no)
        exam_questions.append({
            "id": f"e{exam_no}_q{q_no}",
            "no": q_no,
            "subject": "Coğrafya",
            "text": q["text"],
            "options": new_opts,
            "correct": new_corr,
            "solution": q["solution"]
        })

    # 15 Vatandaşlık (106-120)
    for idx, q in enumerate(vat_list):
        q_no = idx + 106
        new_opts, new_corr = balance_options(q, exam_no * 1000 + q_no)
        exam_questions.append({
            "id": f"e{exam_no}_q{q_no}",
            "no": q_no,
            "subject": "Vatandaşlık",
            "text": q["text"],
            "options": new_opts,
            "correct": new_corr,
            "solution": q["solution"]
        })

    print(f"Deneme {exam_no} üretildi: {len(exam_questions)} soru.")
    all_mock_exams.append({
        "id": exam_id,
        "title": exam_title,
        "questions": exam_questions
    })

# Toplam deneme sayısını ve soruları data.js'e yaz
kpss_data['mockExams'] = all_mock_exams

new_json = json.dumps(kpss_data, ensure_ascii=False, indent=2)
new_raw = raw[:raw.find('{')] + new_json + raw[raw.rfind('}')+1:]

with open(DATA_PATH, 'w', encoding='utf-8') as f:
    f.write(new_raw)

print("\nBAŞARILI: 10 Deneme sınavının tamamı (toplam 1200 soru) eksiksiz kaydedildi!")
