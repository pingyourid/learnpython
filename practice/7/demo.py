# while True:
#     content = input('Please give what you want?\n')
#     if content == 'quit':
#         break
#     print(f'Pizza will add {content}')


# while True:
#     content = input('Please give your age?\n')
#     if content == 'quit':
#         break
#     age = int(content)
#     if age < 3:
#         print('free')
#     elif age < 12:
#         print('10')
#     else:
#         print('15')

# active = True
# while active:
#     content = input('Please give your age?\n')
#     if content == 'quit':
#         active = False
#     else:
#         age = int(content)
#         if age < 3:
#             print('free')
#         elif age < 12:
#             print('10')
#         else:
#             print('15')

unconfirmed_users = ['Alice', 'Bob', 'Tony']
while unconfirmed_users:
    print(unconfirmed_users.pop())
print(unconfirmed_users)

# python3看起来是可以遍历过程中修改数组的,感觉尽量不要这么做，容易出现逻辑问题
# 和if 数组含义一样，while 数组也是看内部是否还有值


