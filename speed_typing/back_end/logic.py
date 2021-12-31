import random
import json

class Logic:
    
    def __init__(self) -> None:
        self.text = [
                    'One Ring to rule them all, One ring to find them; One ring to bring them all and in the darkness bind them.',
                    'Many were increasingly of the opinion that they\'d all made a big mistake in coming down from the trees in the first place. And some said that even the trees had been a bad move, and that no one should ever have left the oceans.', 
                    'Verily this vichyssoise of verbiage veers most verbose, so let me simply add that it\'s my very good honour to meet you and you may call me V.', 
                    'Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. Flat is better than nested. Sparse is better than dense. Readability counts.',
                    'Strangers from distant lands, friends of old. You have been summoned here to answer the threat of Mordor. Middle-Earth stands upon the brink of destruction. None can escape it. You will unite or you will fall.',
                    "You know you are working on clean code when each routine you read turns out to be pretty much what you expected. You can call it beautiful code when the code also makes it look like the language was made for the problem.",
                    'Permanence, perseverance and persistence in spite of all obstacles, discouragements, and impossibilities: It is this, that in all things distinguishes the strong soul from the weak.',
                    'I\'ve seen things you people wouldn\'t believe. Attack ships on fire off the shoulder of Orion. I watched C-beams glitter in the dark near the Tannhauser Gate. All those moments will be lost in time, like tears in rain.',
                    'It is not the critic who counts; not the man who points out how the strong man stumbles or where the doer of deeds could have done them better. The credit belongs to the man who is actually in the arena, whose face is marred by dust and sweat and blood; who strives valiantly; who errs, who comes short again and again, because there is no effort without error and shortcoming; but who does actually strive to do the deeds; who knows the great enthusiasms, the great devotions; who spends himself in a worthy cause; who at the best knows in the end the triumph of high achievement, and who at the worst, if he fails, at least fails while daring greatly, so that his place shall never be with those cold and timid souls who neither know victory nor defeat.',
                    'Sons of Gondor! Of Rohan! My brothers! I see in your eyes the same fear that would take the heart of me! A day may come when the courage of men fails, when we forsake our friends and break all bonds of fellowship. But it is not this day. An hour of wolves and shattered shields when the age of Men comes crashing down! But it is not this day! This day we fight! By all that you hold dear on this good Earth, I bid you stand! Men of the West!',
                    ]

        self.easy_text = [
            'the quick brown fox jumps over the lazy dog', 
            'you asked me if i was in the meth business or the money business neither im in the empire business', 
            'bran thought about it can a man be brave if hes afraid thats the only time he can be brave his father told him', 
            'if you live to be a hundred i hope i live to be a hundred minus one day so that i never have to live a day without you',
            'this day does not belong to one man but to all let us together rebuild this world that we may share in the days of peace',
            'so do all who live to see such times but that is not for them to decide all we have to decide is what to do with the time that is given us',
            ]

    @staticmethod
    def find_shorter(a, b):
        if a < b:
            return a
        return b

    def calculate_accuracy(self, original_string, comparison_string):


        return int(self.string_percent_match(original_string, comparison_string)) * 100
        # original = [letter for letter in original_string]
        # comparison = [letter for letter in comparison_string]
        
    
        # shortest_list = self.find_shorter(len(comparison), len(original))


        # total = 0
        # for i in range(shortest_list):
        #     if original[i] == comparison[i]:
        #         total += 1

        # return int((total / len(original)) * 100)
    
    def string_percent_match(self, original_string, comparison_string) -> float:
        original = [letter for letter in original_string]
        offset = 0

        for letter in comparison_string:
            try:
                original.remove(letter)
            except ValueError:
                offset += 1
        if offset > len(original):
            return ((len(original_string) - offset) / len(original_string))

        return  ((len(original_string) - len(original)) / len(original_string))


    def calculate_wpm(self, original_string, comparison_string, time):
        letters = [letter for letter in comparison_string]
        letter_count = len(letters)

        minutes = int(time) / 60

        if minutes == 0:
            minutes = 0.1

        return int(letter_count // 5 // minutes)

    def get_text(self):
        return random.choice(self.text)

    def get_easy_text(self):
        return random.choice(self.easy_text)

    def net_words_wpm(self, original_string, comparison_string, time, errors):
        gross_words_per_minute = self.calculate_wpm(original_string, comparison_string, time)
        errors_per_minute = int(errors) / int(time)
        return gross_words_per_minute - errors_per_minute

    def new_accuracy(self, original_string, comparison_string, time, errors):
        net_words_per_minute = self.net_words_wpm(original_string, comparison_string, time, errors)
        gross_words_per_minute = self.calculate_wpm(original_string, comparison_string, time)
        return net_words_per_minute/gross_words_per_minute

    def write_hi_score(self, wpm, accuracy):

        score = int(wpm) * int(accuracy)

        with open('./hi_score.json', 'r') as file:

            old_file = json.load(file)
        
        obj = {"score": score, "wpm": wpm, "accuracy": accuracy}
        old_file['hi_scores'].append(obj)

        with open('./hi_score.json', 'w') as file:

            file.write(json.dumps(old_file))




    def get_hi_score(self):
        
        with open('./hi_score.json', 'r') as file:
                scores = json.load(file)
        scores_list = sorted(scores['hi_scores'], key=lambda x: int(x['score']))

        return_list = []
        for _ in range(10):
            try:
                return_list.append(scores_list.pop())
            except IndexError:
                print('list is empty')

        return return_list
            
    def clear_json(self):

        new_content = {"hi_scores": []}


        with open('./hi_score.json', 'w') as file:

            file.write(json.dumps(new_content))
    