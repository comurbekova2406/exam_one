a = [45, 95, 'hello', 'cat']

a.insert(0, 'Start')
a.append('Finish')
a.insert(-1, 'Element')

print(a)

# 2-ая
#должна принимать производное количество аргументов и возвращать словарь,

def adder(*info):
    info

# где ключами являются принятые аргументы, а значениями числа от 1 до количества принятых аргументов
#
# Пример:
#
# print(func('x', 5, 'John')) # {'x':1, 5:2, 'John':3}
# 3-я должна принять кортеж. Превращать этот кортеж в список и, используя анономные функции, выдавать нам на выход 2 списка. 1-ый список должен состоять из всех чётных чисел введённого кортежа. 2-ой со всеми элементами введённого кортежа возведёнными в квадратную степень
#
# Пример:
#
# a, b = func((1,2,3,4,5)) print(a) #[2, 4] print(b) #[1, 4, 9, 16, 25]