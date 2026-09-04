import sys, json
sys.stdout.reconfigure(encoding='utf-8')

content = open(r'c:\Users\oktay\Desktop\kpss\data.js', encoding='utf-8').read()
d = json.loads(content[content.find('{'):content.rfind('}')+1])

exam1 = d['mockExams'][0]
print("=== MATEMATIK (Q31-Q40) ===")
for i in range(30, 40):
    q = exam1['questions'][i]
    print(f"Q{i+1}: {q['text'][:70]} | Ans: {q['options'][q['correct']]}")

print("\n=== TARIH (Q61-Q70) ===")
for i in range(60, 70):
    q = exam1['questions'][i]
    print(f"Q{i+1}: {q['text'][:70]} | Ans: {q['options'][q['correct']]}")

print("\n=== COGRAFYA (Q88-Q95) ===")
for i in range(87, 95):
    q = exam1['questions'][i]
    print(f"Q{i+1}: {q['text'][:70]} | Ans: {q['options'][q['correct']]}")

print("\n=== VATANDASLIK (Q106-Q113) ===")
for i in range(105, 113):
    q = exam1['questions'][i]
    print(f"Q{i+1}: {q['text'][:70]} | Ans: {q['options'][q['correct']]}")
