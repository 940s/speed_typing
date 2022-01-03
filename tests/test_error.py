from speed_typing.back_end.logic import Logic

def test_import():
    assert Logic


def test_errors():
    logic = Logic()

    actual = logic.calculate_accuracy('12345', '00000')
    expected = 0
    assert actual == expected

