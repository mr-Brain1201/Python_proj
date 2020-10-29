result = {}

for line in open('ex_6.txt', encoding="utf-8"):
    items = line.split(':')
    numbers = ''.join(filter(lambda n: (n.isdigit() or n == ' '), items[1]))
    result[items[0]] = sum([int(i) for i in numbers.split()])

print(result)
