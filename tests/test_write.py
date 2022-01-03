from speed_typing.back_end.logic import Logic

def test_import():
    assert Logic

def test_write():
    logic = Logic()

    logic.write_hi_score('90', '100')
