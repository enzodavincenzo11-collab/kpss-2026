import sys
sys.path.append('scratch')

from cografya_data_1 import q88_list, q89_list, q90_list, q91_list, q92_list, q93_list, q94_list, q95_list, q96_list
from cografya_data_2 import q97_list, q98_list, q99_list, q100_list, q101_list, q102_list, q103_list, q104_list, q105_list

all_topics = [
    q88_list, q89_list, q90_list, q91_list, q92_list, q93_list, q94_list, q95_list, q96_list,
    q97_list, q98_list, q99_list, q100_list, q101_list, q102_list, q103_list, q104_list, q105_list
]

def make_q(q_id, subject, stem, correct_choice, dist_list, explanation_core, letter_idx):
    letters = ["A", "B", "C", "D", "E"]
    target_idx = letter_idx % 5
    choices = list(dist_list[:4])
    choices.insert(target_idx, correct_choice)
    options = [f"{letters[i]}) {choices[i]}" for i in range(5)]
    correct_letter = letters[target_idx]
    solution = f"Doğru cevap {correct_letter}'dir. {explanation_core}"
    return {
        "id": q_id,
        "subject": subject,
        "text": stem,
        "options": options,
        "correct": target_idx,
        "solution": solution
    }

def build_all_cografya():
    all_exams = []
    
    for e in range(1, 11):
        idx = e - 1
        qs = []
        base_id = f"e{e}_q"
        
        for q_offset, topic_data in enumerate(all_topics):
            soru_no = 88 + q_offset
            q_info = topic_data[idx]
            stem, correct, dists, expl = q_info[0], q_info[1], q_info[2], q_info[3]
            letter_seed = e + q_offset
            qs.append(make_q(f"{base_id}{soru_no}", "Coğrafya", stem, correct, dists, expl, letter_seed))
            
        all_exams.append(qs)
        
    return all_exams

if __name__ == '__main__':
    exams = build_all_cografya()
    all_qs = [q for exam in exams for q in exam]
    print(f"Total cografya questions: {len(all_qs)}")
    unique_texts = len(set(q['text'] for q in all_qs))
    print(f"Unique cografya texts: {unique_texts}")
    import collections
    letter_counts = collections.Counter(q['correct'] for q in all_qs)
    print(f"Letter distribution: {letter_counts}")
