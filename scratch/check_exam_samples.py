import json, sys
sys.stdout.reconfigure(encoding='utf-8')

d = json.loads(open(r'c:\Users\oktay\Desktop\kpss\data.js', encoding='utf-8').read().split('KPSS_DATA = ')[1].rstrip(';\n '))
for exam_idx in range(1, 4):
    exam = d['mockExams'][exam_idx]
    print(f"=== Exam {exam_idx+1} ===")
    for q_idx in [0, 5, 10, 15, 20, 25, 29, 30, 40, 50, 59, 60, 70, 80, 86, 87, 95, 104, 105, 113, 119]:
        q = exam['questions'][q_idx]
        print(f"  Q{q_idx+1}: {q['text'][:75]}")
