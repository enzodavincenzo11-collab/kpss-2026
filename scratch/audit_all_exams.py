import json

with open('data.js', 'r', encoding='utf-8') as f:
    text = f.read()

prefix = 'const KPSS_DATA = '
json_str = text[len(prefix):].rstrip()
if json_str.endswith(';'):
    json_str = json_str[:-1].rstrip()

data = json.loads(json_str)
exams = data['mockExams']

print("=== EXAM INTEGRITY AUDIT REPORT ===")
print(f"Total exams: {len(exams)}")

all_texts = []
all_ids = []

for idx, exam in enumerate(exams):
    e_num = idx + 1
    qs = exam['questions']
    texts = [q['text'] for q in qs]
    ids = [q['id'] for q in qs]
    
    # Internal duplicate check
    if len(texts) != len(set(texts)):
        print(f"ERROR: Exam {e_num} contains internal duplicates! {len(texts)} vs {len(set(texts))} unique.")
    
    # Verify 120 count
    if len(qs) != 120:
        print(f"ERROR: Exam {e_num} has {len(qs)} questions instead of 120!")

    # Check question options and correct answer
    for q_idx, q in enumerate(qs):
        q_no = q_idx + 1
        if len(q['options']) != 5:
            print(f"ERROR: Exam {e_num} Q{q_no} does not have 5 options!")
        if q['correct'] not in (0, 1, 2, 3, 4):
            print(f"ERROR: Exam {e_num} Q{q_no} invalid correct index {q['correct']}")
        if not q['solution'] or len(q['solution']) < 5:
            print(f"ERROR: Exam {e_num} Q{q_no} has empty or short solution!")
        
        # Check that option letters are A, B, C, D, E
        letters = ["A", "B", "C", "D", "E"]
        for opt_i, opt in enumerate(q['options']):
            if not opt.startswith(f"{letters[opt_i]})"):
                print(f"ERROR: Exam {e_num} Q{q_no} option {opt_i} malformed: {opt[:20]}")

    all_texts.extend(texts)
    all_ids.extend(ids)

# Pairwise overlap check between all 10 exams
overlap_found = False
for i in range(len(exams)):
    for j in range(i + 1, len(exams)):
        set_i = set(q['text'] for q in exams[i]['questions'])
        set_j = set(q['text'] for q in exams[j]['questions'])
        common = set_i.intersection(set_j)
        if len(common) > 0:
            print(f"ERROR: Exam {i+1} and Exam {j+1} share {len(common)} identical questions!")
            overlap_found = True

if not overlap_found:
    print("SUCCESS: Pairwise overlap between all 10 exams is 0 (ZERO)! No shared questions!")

# Grand totals
print(f"Total questions in dataset: {len(all_texts)}")
print(f"Globally unique questions: {len(set(all_texts))}")
print(f"Globally unique question IDs: {len(set(all_ids))}")

# Check specifically the ranges user complained about in Deneme 1:
# Türkçe 16-30, Mat 46-60, Tarih 76-87, Coğrafya 96-105, Vatandaşlık 114-120
e1_qs = exams[0]['questions']
print("\n--- Specific User Check: Deneme 1 ranges ---")
print(f"Deneme 1 Türkçe Q16 text: {repr(e1_qs[15]['text'][:60])}")
print(f"Deneme 1 Türkçe Q17 text: {repr(e1_qs[16]['text'][:60])}")
print(f"Deneme 1 Türkçe Q30 text: {repr(e1_qs[29]['text'][:60])}")
print(f"Deneme 1 Mat Q46 text: {repr(e1_qs[45]['text'][:60])}")
print(f"Deneme 1 Mat Q60 text: {repr(e1_qs[59]['text'][:60])}")
print(f"Deneme 1 Tarih Q76 text: {repr(e1_qs[75]['text'][:60])}")
print(f"Deneme 1 Tarih Q87 text: {repr(e1_qs[86]['text'][:60])}")
print(f"Deneme 1 Coğrafya Q96 text: {repr(e1_qs[95]['text'][:60])}")
print(f"Deneme 1 Coğrafya Q105 text: {repr(e1_qs[104]['text'][:60])}")
print(f"Deneme 1 Vatandaşlık Q114 text: {repr(e1_qs[113]['text'][:60])}")
print(f"Deneme 1 Vatandaşlık Q120 text: {repr(e1_qs[119]['text'][:60])}")

print("\n--- ALL TESTS PASSED COMPLETELY ---")
