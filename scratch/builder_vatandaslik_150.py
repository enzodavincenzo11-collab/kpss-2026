import sys
sys.path.append('scratch')

from vatandaslik_data_1 import q106_list, q107_list, q108_list, q109_list, q110_list, q111_list, q112_list, q113_list
from vatandaslik_data_2 import q114_list, q115_list, q116_list, q117_list, q118_list, q119_list, q120_list

all_topics = [
    q106_list, q107_list, q108_list, q109_list, q110_list, q111_list, q112_list, q113_list,
    q114_list, q115_list, q116_list, q117_list, q118_list, q119_list, q120_list
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

def build_all_vatandaslik():
    all_exams = []
    
    for e in range(1, 11):
        idx = e - 1
        qs = []
        base_id = f"e{e}_q"
        
        for q_offset, topic_data in enumerate(all_topics):
            soru_no = 106 + q_offset
            q_info = topic_data[idx]
            stem, correct, dists, expl = q_info[0], q_info[1], q_info[2], q_info[3]
            letter_seed = e + q_offset
            qs.append(make_q(f"{base_id}{soru_no}", "Vatandaşlık", stem, correct, dists, expl, letter_seed))
            
        all_exams.append(qs)
        
    return all_exams

if __name__ == '__main__':
    exams = build_all_vatandaslik()
    all_qs = [q for exam in exams for q in exam]
    print(f"Total vatandaslik questions: {len(all_qs)}")
    unique_texts = len(set(q['text'] for q in all_qs))
    print(f"Unique vatandaslik texts: {unique_texts}")
    import collections
    letter_counts = collections.Counter(q['correct'] for q in all_qs)
    print(f"Letter distribution: {letter_counts}")
