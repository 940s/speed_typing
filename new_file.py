import json


def write_hi_score(wpm, accuracy):

    score = int(wpm) * int(accuracy)

    with open('./hi_score.json', 'r') as file:

        old_file = json.load(file)
    
    obj = {"score": score, "wpm": wpm, "accuracy": accuracy}
    old_file['hi_scores'].append(obj)

    with open('./hi_score.json', 'w') as file:

        json.dump(old_file, file)

write_hi_score("1", "1")