from logic import calc_response


def test_leading_zeros_are_handled():
    # secret and guess are numerically small but should be treated with leading zeros
    assert "****" == calc_response(12, 12, 4)  # 0012 vs 0012 -> all exact
    assert "" == calc_response(12, 3456, 4)  # 0012 vs 3456 -> no matches


def test_repeated_digits_full_misplaced():
    # 1122 vs 2211 -> no exact matches, all digits present but misplaced
    assert "++++" == calc_response(1122, 2211, 4)


def test_all_misplaced_different_order():
    # 1234 vs 4321 -> all digits present but none in correct position
    assert "++++" == calc_response(1234, 4321, 4)


def test_mixed_exact_and_misplaced():
    # two exact matches and two misplaced
    assert "**++" == calc_response(1212, 1221, 4)


def test_variable_number_of_digits():
    # 3-digit mode
    assert "***" == calc_response(123, 123, 3)
    # 01 vs 10 -> both digits are present but misplaced => '++'
    assert "++" == calc_response(1, 10, 2)
