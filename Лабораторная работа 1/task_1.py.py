numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

trimmed_numbers = numbers[:numbers.index(None)] + numbers[numbers.index(None) + 1:]
numbers[numbers.index(None)] = sum(trimmed_numbers) / (len(trimmed_numbers) + 1)

print("Измененный список:", numbers)
