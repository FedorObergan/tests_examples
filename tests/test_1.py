import pytest
from main import (perimeter_and_area_of_rectangle,
                  pairing_boys_and_girls_after_sorting,
                  solution_of_quadratic_equation)




@pytest.mark.parametrize(
    'a,b,expected_per,expected_area',
    (
        [1, 1, 4, 1],
        [2, 3, 10, 6],
        [0, 4, -1, -1],
        [5, -2, -1, -1],
        [10, 10, 40, 100],
    )
)
def test_characteristics_of_rectangle(a, b, expected_per, expected_area):
    actual = perimeter_and_area_of_rectangle(a, b)
    assert actual['perimeter'] == expected_per
    assert actual['area'] == expected_area


@pytest.mark.parametrize(
    'boys,girls,exp_result',
    (
        [
            ['Peter', 'Alex', 'John', 'Arthur', 'Richard'],
            ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha'],
            "Alex и Emma, Arthur и Kate, John и Kira, Peter и Liza, Richard и Trisha"
        ],
        [
            ['Peter', 'Alex', 'John', 'Arthur'],
            ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha'],
            "Кто-то может остаться без пары!"
        ]
    )
)
def test_pairing(boys, girls, exp_result):
    actual_result = pairing_boys_and_girls_after_sorting(boys,girls)
    assert actual_result == exp_result


@pytest.mark.parametrize(
    'a,b,c,exp_result',
    (
        [1, 8, 15, '-3.0 -5.0'],
        [1, -13, 12, '12.0 1.0'],
        [-4, 28, -49, '3.5'],
        [1, 1, 1, 'вещественных корней нет']
    )
)
def test_solution_of_quadr_eq(a, b, c, exp_result):
    actual_result = solution_of_quadratic_equation(a,b,c)
    assert actual_result == exp_result
