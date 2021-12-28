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

    actual = logic.calculate_wpm('hello world in python', 'hello world in python', 60)
    expected = 4
    assert actual == expected

def test_wpm_calc_short():
    logic = Logic()

    actual = logic.calculate_wpm('hello world', 'hello world', 60)
    expected = 2
    assert actual == expected


def test_wpm_calc_long():
    logic = Logic()

    actual = logic.calculate_wpm('hello world now in python', 'hello world now in python please count all these words', 60)
    expected = 10
    assert actual == expected


def test_wpm_calc_with_variable_time():
    logic = Logic()

    actual = logic.calculate_wpm('hello world now in python', 'hello world now in python please count all these words hello world now in python please count all these words', 120)
    expected = 10
    assert actual == expected

def test_get_text():
    logic = Logic()

    actual = logic.get_text()
    expected = ['hello world', 'we love python', "why isn't this project easy"]
    assert actual in expected

def test_get_wpm_string():
    logic = Logic()

    actual = logic.calculate_wpm('hello world now in python', 'hello world now in python please count all these words hello world now in python please count all these words', '120')
    expected = 10
    assert actual == expected