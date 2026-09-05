import sys, json, os, collections
sys.path.append('scratch')

from builder_turkce_300 import build_all_turkce
from builder_math_300 import build_all_math
from builder_tarih_270 import build_all_tarih
from builder_cografya_180 import build_all_cografya
from builder_vatandaslik_150 import build_all_vatandaslik

def main():
    print("Generating questions from builders...")
    turkce_exams = build_all_turkce()
    math_exams = build_all_math()
    tarih_exams = build_all_tarih()
    cografya_exams = build_all_cografya()
    vatandaslik_exams = build_all_vatandaslik()

    mock_exams = []
    all_qs = []

    for i in range(10):
        exam_num = i + 1
        t = turkce_exams[i]
        m = math_exams[i]
        ta = tarih_exams[i]
        c = cografya_exams[i]
        v = vatandaslik_exams[i]

        exam_qs = t + m + ta + c + v
        all_qs.extend(exam_qs)

        mock_exams.append({
            "id": f"deneme_{exam_num}",
            "name": f"{exam_num}. Deneme Sınavı",
            "totalQuestions": len(exam_qs),
            "durationMinutes": 130,
            "questions": exam_qs
        })
        print(f"Deneme {exam_num}: {len(exam_qs)} questions (T:{len(t)}, M:{len(m)}, Ta:{len(ta)}, C:{len(c)}, V:{len(v)})")

    # Sanity checks
    assert len(all_qs) == 1200, f"Expected 1200 questions, got {len(all_qs)}"
    unique_texts = set(q['text'] for q in all_qs)
    assert len(unique_texts) == 1200, f"Duplicate texts detected! Unique: {len(unique_texts)} / 1200"
    unique_ids = set(q['id'] for q in all_qs)
    assert len(unique_ids) == 1200, f"Duplicate IDs detected! Unique: {len(unique_ids)} / 1200"

    print("\n--- Integrity checks passed ---")
    print(f"Total questions: {len(all_qs)}")
    print(f"Unique question texts: {len(unique_texts)} (0 duplicates)")
    print(f"Unique question IDs: {len(unique_ids)}")

    letter_counts = collections.Counter(q['correct'] for q in all_qs)
    letters = ['A', 'B', 'C', 'D', 'E']
    for idx in range(5):
        print(f"Option {letters[idx]}: {letter_counts[idx]} ({letter_counts[idx]/len(all_qs)*100:.2f}%)")

    # Read data.js
    with open('data.js', 'r', encoding='utf-8') as f:
        content = f.read()

    prefix = 'const KPSS_DATA = '
    assert content.startswith(prefix), "data.js does not start with 'const KPSS_DATA = '"
    json_str = content[len(prefix):].rstrip()
    if json_str.endswith(';'):
        json_str = json_str[:-1].rstrip()

    data = json.loads(json_str)

    # Clean spurious keys if present
    if 'correct' in data:
        del data['correct']
    if 'solution' in data:
        del data['solution']

    # Update mockExams
    data['mockExams'] = mock_exams
    data['mockExam'] = mock_exams[0]

    # Write back to data.js
    new_json_str = json.dumps(data, ensure_ascii=False, indent=2)
    new_content = f"const KPSS_DATA = {new_json_str};\n"

    # Backup data.js first
    with open('data.js.bak', 'w', encoding='utf-8') as f:
        f.write(content)
    print("\nBackup saved as data.js.bak")

    with open('data.js', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("data.js successfully written!")

    # Verify reload
    with open('data.js', 'r', encoding='utf-8') as f:
        verify_content = f.read()
    verify_json = verify_content[len(prefix):].rstrip()
    if verify_json.endswith(';'):
        verify_json = verify_json[:-1].rstrip()
    loaded_data = json.loads(verify_json)

    assert len(loaded_data['mockExams']) == 10
    total_loaded_qs = sum(len(e['questions']) for e in loaded_data['mockExams'])
    assert total_loaded_qs == 1200
    print(f"Reload verification successful: 10 mock exams, {total_loaded_qs} questions loaded cleanly!")

if __name__ == '__main__':
    main()
