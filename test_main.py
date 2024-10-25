from main import count_and_sum


def test_sum_and_count():
    numbers = [-42, -2, 4, 3]

    count, total_sum = count_and_sum(numbers)

    assert (count == 1 and total_sum == 4)