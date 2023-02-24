numbers = [8, 9, 10, 11]
numbers[1] = 17
numbers.append(4)
numbers.append(5)
numbers.append(6)
del numbers[0]
numbers.extend(numbers)
numbers.insert(3, 25)
print(numbers)
