import json

def write_hi_score(wpm, accuracy):
    score = int(wpm) * int(accuracy)

    with open('./hi_score.json', 'r') as file:

        old_file = json.load(file)
    
    obj = {'score': score, 'wpm': wpm, 'accuracy': accuracy}
    old_file['hi_scores'].append(obj)

    with open('./hi_score.json', 'w') as file:


        file.write(json.dumps(old_file))


        # new_object = {'hi_scores': []}
        # for key, val in enumerate(old_file):
        #     new_object[key] = val
        # for key, val in enumerate(obj):
        #     new_object[key] = val

write_hi_score('90', '100')