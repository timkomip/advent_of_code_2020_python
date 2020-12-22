def cross_product(list1, list2):
    for i in list1:
        for j in list2:
            yield (i, j)


with open('input.txt') as f:
    lines = f.readlines()

numbers = [int(line) for line in lines]
answer = None

for (i, j) in cross_product(numbers, numbers):
    if i + j == 2020:
        answer = i * j
        break

print(f"The answer for 2 entries is {answer}")

for ((x, y), z) in cross_product(cross_product(numbers, numbers), numbers):
    if x + y + z == 2020:
        answer = x * y * z
        break

print(f"The answer for 3 entries is {answer}")
