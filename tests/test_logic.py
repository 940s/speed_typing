from speed_typing.back_end.logic import Logic

def test_import():
    assert Logic()

def test_params():
    logic = Logic()

    actual = logic.calculate_accuracy('hi', 'ji')
    expected = .5
    assert actual == expected

def test_params_two():
    logic = Logic()

    actual = logic.calculate_accuracy('hi', 'hi')
    expected = 1
    assert actual == expected

def test_white_space():
    logic = Logic()

    actual = logic.calculate_accuracy('hi', 'hi')
    expected = 1
    assert actual == expected

def test_white_space_multi_char():
    logic = Logic()

    actual = logic.calculate_accuracy('hello world in python', 'hello world in python')
    expected = 1
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

def test_get_text():
    logic = Logic()

    actual = logic.get_text()
    expected = ['hello world', 'we love python', "why isn't this project easy"]
    assert actual in expected

def test_get_wpm_string():
    logic = Logic()

    actual = logic.calculate_wpm('1234567890     ', '1234567890     ', '120')
    expected = 1
    assert actual == expected

def test_accuracy_different_lengths():
    logic = Logic()

    actual = logic.calculate_accuracy('abc', 'abcdef', )
    expected = 1
    assert actual == expected

def test_accuracy_different_lengths_swapped():
    logic = Logic()

    actual = logic.calculate_accuracy('abcdef', 'abc')
    expected = 0.5
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

