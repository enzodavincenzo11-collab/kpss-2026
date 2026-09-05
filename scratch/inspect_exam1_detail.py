import sys, json
sys.stdout.reconfigure(encoding='utf-8')
content = open(r'c:\Users\oktay\Desktop\kpss\data.js', encoding='utf-8').read()
d = json.loads(content[content.find('{'):content.rfind('}')+1])
exam1 = d['mockExams'][0]

print('=== EXAM 1: Q15 to Q30 (Turkce) ===')
for i in range(14, 30):
    q = exam1['questions'][i]
    print(f"Q{i+1}: {q['text'][:75]}")

print('\n=== EXAM 1: Q45 to Q60 (Matematik) ===')
for i in range(44, 60):
    q = exam1['questions'][i]
    print(f"Q{i+1}: {q['text'][:75]}")

print('\n=== EXAM 1: Q75 to Q87 (Tarih) ===')
for i in range(74, 87):
    q = exam1['questions'][i]
    print(f"Q{i+1}: {q['text'][:75]}")

print('\n=== EXAM 1: Q95 to Q105 (Cografya) ===')
for i in range(94, 105):
    q = exam1['questions'][i]
    print(f"Q{i+1}: {q['text'][:75]}")

print('\n=== EXAM 1: Q113 to Q120 (Vatandaslik) ===')
for i in range(113, 120):
    q = exam1['questions'][i]
    print(f"Q{i+1}: {q['text'][:75]}")
