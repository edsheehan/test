"""Find the number with the largest difference between itself and its digit sum."""
import random


numbers = random.sample(range(1, 201), 6)
print(numbers)

selected = max(
	numbers,
	key=lambda number: number - sum(int(digit) for digit in str(number)),
)
digit_sum = sum(int(digit) for digit in str(selected))
print(selected, digit_sum, selected - digit_sum)
