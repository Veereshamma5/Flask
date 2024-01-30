def test_multiply_with_11(input_value):
    assert input_value * 11 == 33


def test_multiply_with_10(input_value):
    assert input_value * 8 == 24


def test_disabling_capturing(capsys):
    print("this output is captured, 11111111111")
    with capsys.disabled():
        print("output not captured, going directly to sys.stdout")
    print("this output is also captured......... Hello")


def test_capssys(capsys):
    print("Hello World")