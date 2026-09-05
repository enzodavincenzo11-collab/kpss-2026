import sys
sys.path.append('scratch')

from tarih_data_1 import q61_list, q62_list, q63_list, q64_list, q65_list, q66_list, q67_list, q68_list, q69_list
from tarih_data_2 import q70_list, q71_list, q72_list, q73_list, q74_list, q75_list, q76_list, q77_list, q78_list
from tarih_data_3 import q79_list, q80_list, q81_list, q82_list, q83_list, q84_list, q85_list, q86_list, q87_list

all_topics = [
    q61_list, q62_list, q63_list, q64_list, q65_list, q66_list, q67_list, q68_list, q69_list,
    q70_list, q71_list, q72_list, q73_list, q74_list, q75_list, q76_list, q77_list, q78_list,
    q79_list, q80_list, q81_list, q82_list, q83_list, q84_list, q85_list, q86_list, q87_list
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

def build_all_tarih():
    all_exams = []
    
    for e in range(1, 11):
        idx = e - 1
        qs = []
        base_id = f"e{e}_q"
        
        for q_offset, topic_data in enumerate(all_topics):
            soru_no = 61 + q_offset
            q_info = topic_data[idx]
            stem, correct, dists, expl = q_info[0], q_info[1], q_info[2], q_info[3]
            letter_seed = e + q_offset
            qs.append(make_q(f"{base_id}{soru_no}", "Tarih", stem, correct, dists, expl, letter_seed))
            
        all_exams.append(qs)
        
    return all_exams

if __name__ == '__main__':
    exams = build_all_tarih()
    all_qs = [q for exam in exams for q in exam]
    print(f"Total tarih questions: {len(all_qs)}")
    unique_texts = len(set(q['text'] for q in all_qs))
    print(f"Unique tarih texts: {unique_texts}")
    import collections
    letter_counts = collections.Counter(q['correct'] for q in all_qs)
    print(f"Letter distribution: {letter_counts}")
