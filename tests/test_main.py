import Main
import pytest

@pytest.mark.parametrize("a, b, result", [
                                            (1, 2, 3),
                                            (2, 5, 7),
                                            (2, 2, 4),
                                            (6, 4, 10)
                                        ])
def test_main(a, b, result):
    assert Main.sum(a, b) == result


@pytest.mark.parametrize("a, b, result", [
                                            (1, 1, 1),
                                            (4, 2, 2),
                                            (5, 4, 1.25),
                                        ])
def test_division(a, b, result):
    assert Main.division(a, b) == result


@pytest.mark.parametrize("a, b, type_error", [
                                                (5, 0, ZeroDivisionError),
                                                (4, 0, ZeroDivisionError),
                                                (3, 0, ZeroDivisionError),
                                                (1, 0, ZeroDivisionError),
                                            ])
def test_errors_division(a, b, type_error):
    with pytest.raises(type_error):
        Main.division(a, b)