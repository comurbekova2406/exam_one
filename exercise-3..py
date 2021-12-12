a = [45, 95, 'hello', 'cat']

a.insert(0, 'Start')
a.append('Finish')
a.insert(-1, 'Element')

print(a)

# 2-ая


def adder(*info):
    new_info = dict()

    for i, item in enumerate(info, start=1):
        new_info[item] = i

    return new_info


print(adder('x', 5, 'John'))

# 3-я


def func(items):
    even_number =[]
    squared_numbers =[]

    for item in items:
        if item % 2 == 0:
            even_number.append(item)
        squared_numbers.append(pow(item, 2))

    return even_number, squared_numbers


a, b = func((1, 2, 3, 4, 5))
print(a)
print(b)

