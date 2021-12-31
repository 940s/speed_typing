import json

def clear_json():

    new_content = {"hi_scores": []}


    with open('./hi_score.json', 'w') as file:

        json.dump(new_content, file)

clear_json()