"""Find the number with the largest difference between itself and its digit sum."""
import random


numbers = random.sample(range(1, 201), 6)
print(numbers)

def difference(number):
    """Return the difference between a number and its digit sum."""
    return number - sum(int(digit) for digit in str(number))

selected = []
digit_sums = []
for _ in range(2):
    selected_index = max(
        range(len(numbers)),
        key=lambda index: difference(numbers[index]),
    )
    selected_number = numbers[selected_index]
    digit_sum = sum(int(digit) for digit in str(selected_number))
    numbers[selected_index] = digit_sum
    selected.append(selected_number)
    digit_sums.append(digit_sum)
    print(numbers, selected, digit_sums)

print(sum(numbers))
