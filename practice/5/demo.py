# car = 'aodi'
# if car == 'aodi':
#     print('same')
#     print('the same')
# else:
#     print('different')

# age = 22
# if age > 16 and age < 21:
#     print('success')
# else:
#     print('fail')

# fruit = 'banana'
# fruits = ['banana', 'apple', 'orange']
# if fruit not in fruits:
#     print('ok')
# else:
#     print('nope')
    
# peoples = ['Ann', 'Admin', 'Susan']
# peoples = []
# if peoples:
#     for people in peoples:
#         if people == 'Admin':
#             print(f'Hello {people}, would you like to see a status report?')
#         else:
#             print(f'Hello {people}, think you for logging in again.')
# else:
#     print('We need to find some users!')

#if peoples就代表是否为空数组，至少有一个元素才为True。errr,python的习惯吧，用起来比较简洁，对习惯了指针的人不习惯

# current_users = ['Zhang Bin', 'Li Jing', 'Hua Hua', 'Dou Dou', 'Ning Meng']
# current_users_lower = []
# new_users = ['Shu Shu', 'Dou dou', 'A Yi', 'Bo Bo']

# for current_user in current_users:
#     current_users_lower.append(current_user.lower())

# for new_user in new_users:   
#     if new_user.lower() in current_users_lower:
#         print(f'exist username called {new_user}')
#     else:
#         print(f'{new_user} can be use')
# print(f'test local variable {current_user}')

# python3一个函数中没有局部变量的概念，这点容易有坑，要小心

numbers = list(range(1, 10))

for number in numbers:
    if number == 1:
        print('1st')
    elif number == 2:
        print('2nd')
    elif number == 3:
        print('3rd')
    else:
        print(f'{number}th')

