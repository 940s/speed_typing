import random


class Logic:
    
    def __init__(self) -> None:
        self.text = ['hello world', 'we love python', "why isn't this project easy"]

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

