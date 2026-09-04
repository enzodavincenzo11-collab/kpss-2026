import sys, json
sys.stdout.reconfigure(encoding='utf-8')

content = open(r'c:\Users\oktay\Desktop\kpss\data.js', encoding='utf-8').read()
d = json.loads(content[content.find('{'):content.rfind('}')+1])

exam1 = d['mockExams'][0]
print("=== FIRST 15 QUESTIONS OF EXAM 1 ===")
for i, q in enumerate(exam1['questions'][:15]):
    print(f"Q{i+1} [{q['subject']}]:")
    print("  Text:", q['text'].replace('\n', ' '))
    print("  Options:", q['options'])
    print("  Solution:", q.get('solution', ''))
    print("-" * 50)
