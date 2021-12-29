import random


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
                    'I\'ve seen things you people wouldn\'t believe. Attack ships on fire off the shoulder of Orion. I watched C-beams glitter in the dark near the Tannhauser Gate. All those moments will be lost in time, like tears in rain.'
                    ]

    @staticmethod
    def find_shorter(a, b):
        if a < b:
            return a
        return b

    def calculate_accuracy(self, original_string, comparison_string):
        original = [letter for letter in original_string]
        comparison = [letter for letter in comparison_string]
        
    
        shortest_list = self.find_shorter(len(comparison), len(original))


        total = 0
        for i in range(shortest_list):
            if original[i] == comparison[i]:
                total += 1

        return total / len(original)


    def calculate_wpm(self, original_string, comparison_string, time):
        letters = [letter for letter in comparison_string]
        letter_count = len(letters)

        minutes = int(time) / 60

        return int(letter_count // 5 // minutes)

    def get_text(self):
        return random.choice(self.text)

    def net_words_wpm(self, original_string, comparison_string, time, errors):
        gross_words_per_minute = self.calculate_wpm(original_string, comparison_string, time)
        errors_per_minute = int(errors) / int(time)
        return gross_words_per_minute - errors_per_minute

    def new_accuracy(self, original_string, comparison_string, time, errors):
        net_words_per_minute = self.net_words_wpm(original_string, comparison_string, time, errors)
        gross_words_per_minute = self.calculate_wpm(original_string, comparison_string, time)
        return net_words_per_minute/gross_words_per_minute

