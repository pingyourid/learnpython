# with open('pi_digits.txt') as f:
#     result = f.read()
# print(result.rstrip())
# # print(result)

#----

# with open('pi_digits.txt') as f:
#     for line in f:
#         # print(line)
#         print(line.rstrip())

#----

# filename = 'pi_digits.txt'
# with open(filename) as f:
#     lines = f.readlines()
# print(lines)

# # for line in lines:
# #     print(line.rstrip())

# str = ''
# new_strip_lines = []
# new_rstrip_lines = []
# for line in lines:
#     new_strip_lines.append(line.strip())
#     new_rstrip_lines.append(line.rstrip())
# print(f'new_strip_lines:{new_strip_lines}')
# print(f'new_strip_lines:{new_rstrip_lines}')

# #strip()是移除头尾空字符串或者制表符等

#---

# finename = 'pi_million_digits.txt'

# with open(finename) as f:
#     pi = f.read()
# print(pi[:52])

# birth = '09090019'
# if birth in pi:
#     print('Yeah!,your birth in pi')
# else:
#     print('Not in')

#---

# finename = 'test_dogs.txt'
# dog_describe = 'I have a lot of dogs, and I like dog.\nI have a log of chikens, and I like chiken.'
# dog_describe = dog_describe.replace('dog', 'cat')

# # with open(finename, 'w') as f:
# with open(finename, 'a') as f:
#     f.write(dog_describe)

#---

# finename = 'can_not_find.txt'

# with open(finename) as f:
#     pi = f.read()
# print(pi)

#---

# # finename = 'can_not_find.txt'
# finename = 'pi_million_digits.txt'

# try:
#     with open(finename) as f:
#         pi = f.read()
#     print(pi[:52])
# except FileNotFoundError as e:
#     # print(f'Cannot find file:{finename}')
#     pass
# else:
#     print('try success')
# finally:
#     print('finally')

#---

# filename = 'alice.txt'
# try:
#     with open(filename, encoding='utf8') as f:
#         content = f.read()    
# except Exception as e:
#     print(e)
# else:
#     words = content.split()
#     count = len(words)
#     print(f'alice has {count} words')

#---

import json

filename = 'favorite_num.txt'
try:
    with open(filename) as f:
        num = json.load(f)
except Exception as e:
    num = input('input your favorite number:\n')
    with open(filename, 'w') as f:
        json.dump(num, f)
else:
    print(f'I know your favorite num, It is {num}')

#---
