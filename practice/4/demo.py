#message = "I wait for you"
#   print(message)

# python使用缩进来控制是在循环内还是循环外，多余的缩进会编译报错，感觉又是一个失败的设计，层级多，代码量大的时候，根本搞不清

'''
pizzas = ["beef pizza", "milk pizza", "pork pizza"]
for pizza in pizzas:
    print(f"I like {pizza}")
print("I really love pizza")
'''

'''
animations = ['dog', 'cat', 'pig']
for pet in animations:
    print(f'a {pet} would make a great pet.')
print('all are pet')
'''


# for i in range(1, 5):
#     print(i)


'''
numbers = list(range(1, 5))
print(numbers)

numbers = list(range(1, 15, 2))
print(numbers)
'''

'''
squares = []
for number in range(1, 11):
    squares.append(number ** 2)
print(squares)
'''

# numbers = [2, 3, 1, 7, 4]
# result = min(numbers)
# print(result)

# numbers = [value ** 2 for value in range(1, 11)]
# print(numbers)

#这个牛逼，列表解析

# numbers = [value for value in range(1, 1_000_001)]
# for result in numbers:
#   print(result)

# numbers = list(range(1, 1_000_001))
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))

# numbers = list(range(3, 31, 3))
# for i in numbers:
#     print(i)

# numbers = [value ** 3 for value in range(1, 11)]
# for i in numbers:
#   print(i)

#下面的数组切片能力还是很方便的，相当于快速生成一个新数组了
# numbers = ['cat', 'dog', 'pig', 'pizza']
# print(numbers[:2])
# print(numbers[1:2])
# print(numbers[-2:])
# print(numbers[:])

numbers = ['cat', 'dog', 'pig', 'pizza', 'bag']
print('The first three items in the list are:')
for i in numbers[:3]:
  print(i)

# print('Three items from the middle of the list are:')
# for i in numbers[1:-1]:
#   print(i)

# print('The last three items in the list are:')
# for i in numbers[-3:]:
#   print(i)

# friends_numbers =numbers[:]
# numbers.append('chicken')
# friends_numbers.append('boy')
# print(f'numbers are:{numbers}')
# print(f'friends are:{friends_numbers}')

#元组，就是不可变数组
# numbers = ('cat', 'dog')
# print(numbers[0])
# numbers[0] = 'egg'

#定义单元素的元组，需要一个逗号做分割符，否则不按预期，愚蠢的设计
# values = ('cat', )

# numbers = []
# for value in numbers:
#     print(value)