from speed_typing.back_end.logic import Logic

def test_import():
    assert Logic()

def test_params():
    logic = Logic()

    actual = logic.calculate_accuracy('hi', 'ji')
    expected = 50
    assert actual == expected

def test_params_two():
    logic = Logic()

    actual = logic.calculate_accuracy('hi', 'hi')
    expected = 100
    assert actual == expected

def test_white_space():
    logic = Logic()

    actual = logic.calculate_accuracy('hi', 'hi')
    expected = 100
    assert actual == expected

def test_white_space_multi_char():
    logic = Logic()

    actual = logic.calculate_accuracy('hello world in python', 'hello world in python')
    expected = 100
    assert actual == expected


def test_wpm_calc():
    logic = Logic()

    actual = logic.calculate_wpm('123456789 ', '123456789 ', 60)
    expected = 2
    assert actual == expected

def test_wpm_calc_short():
    logic = Logic()

    actual = logic.calculate_wpm('hello world9   ', 'hello world9   ', 60)
    expected = 3
    assert actual == expected


def test_wpm_calc_long():
    logic = Logic()

    actual = logic.calculate_wpm('1234567890     ', '1234567890     ', 60)
    expected = 3
    assert actual == expected


def test_wpm_calc_with_variable_time():
    logic = Logic()

    actual = logic.calculate_wpm('1234567890     ', '1234567890     ', 120)
    expected = 1
    assert actual == expected

# def test_get_text():
    logic = Logic()

    actual = logic.get_text()
    expected = [
                    'One Ring to rule them all, One ring to find them; One ring to bring them all and in the darkness bind them.',
                    'Many were increasingly of the opinion that they\'d all made a big mistake in coming down from the trees in the first place. And some said that even the trees had been a bad move, and that no one should ever have left the oceans.', 
                    'Verily this vichyssoise of verbiage veers most verbose, so let me simply add that it\'s my very good honour to meet you and you may call me V.', 
                    'Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. Flat is better than nested. Sparse is better than dense. Readability counts.',
                    'Strangers from distant lands, friends of old. You have been summoned here to answer the threat of Mordor. Middle-Earth stands upon the brink of destruction. None can escape it. You will unite or you will fall.',
                    "You know you are working on clean code when each routine you read turns out to be pretty much what you expected. You can call it beautiful code when the code also makes it look like the language was made for the problem.",
                    'Permanence, perseverance and persistence in spite of all obstacles, discouragements, and impossibilities: It is this, that in all things distinguishes the strong soul from the weak.',
                    'I\'ve seen things you people wouldn\'t believe. Attack ships on fire off the shoulder of Orion. I watched C-beams glitter in the dark near the Tannhauser Gate. All those moments will be lost in time, like tears in rain.'
                    ]
    assert actual in expected

def test_get_wpm_string():
    logic = Logic()

    actual = logic.calculate_wpm('1234567890     ', '1234567890     ', '120')
    expected = 1
    assert actual == expected

def test_accuracy_different_lengths():
    logic = Logic()

    actual = logic.calculate_accuracy('abc', 'abcdef', )
    expected = 0
    assert actual == expected

def test_accuracy_different_lengths_swapped():
    logic = Logic()

    actual = logic.calculate_accuracy('abcdef', 'abc')
    expected = 50
    assert actual == expected

def test_words_perminute_by5():
    logic = Logic()

    actual = logic.calculate_wpm('abcdeadsfdsaasd', 'abcdefghijklasd','60')
    expected = 3
    assert actual == expected

def test_words_errors():
    logic = Logic()

    actual = logic.net_words_wpm('1234567890', '1234567890','60', '0')
    expected = 2
    assert actual == expected

def test_words_errors_2():
    logic = Logic()

    actual = logic.net_words_wpm('1234567890', '1234567890','60', '60')
    expected = 1
    assert actual == expected

def test_new_accuracy():
    logic = Logic()

    actual = logic.new_accuracy('1234567890', '1234567890', '60', '0')
    expected = 1
    assert actual == expected

def test_new_accuracy_2():
    logic = Logic()

    actual = logic.new_accuracy('1234567890', '1234567890', '60', '60')
    expected = .5
    assert actual == expected


