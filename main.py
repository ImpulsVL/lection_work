

def count_and_sum(numbers):
    if not numbers:
        return 0, 0

    count = 0
    sum = 0

    for num in numbers:
        if num > 0 and num % 2 == 0:
            count += 1
            sum += num

    return count, sum


# numbers = [10, -20, 30, 40, 50, -25, 2, -40]
# count, total_sum = count_and_sum(numbers)
# print("Количество четных положительных элементов:", count)
# print("Сумма четных положительных элементов:", total_sum)