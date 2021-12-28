class Logic:
    
    def calculate_accuracy(self, original_string, comparison_string):
        original = [letter for letter in original_string]
        comparison = [letter for letter in comparison_string]
        total = 0

        for i,_ in enumerate(original):
            if original[i] == comparison[i]:
                total += 1

        return total / len(original)


    def calculate_wpm(self, original_string, comparison_string, time):
        words = comparison_string.split()
        word_count = len(words)

        minutes = time / 60

        return int(word_count // minutes)
