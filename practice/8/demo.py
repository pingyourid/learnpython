# def say_hello():
#     print('we learn function')
# say_hello()

# def favorite_book(title):
#     print(f'One of my favorite books is {title.title()}')
# favorite_book('go away')

# def favorite_book(title, age = 10):
#     print(f'One of my favorite books is {title.title()}, and age is {age}')
# favorite_book(age=5, title = 'go away')
# favorite_book('go away', 5)
# favorite_book('go away')

# def get_your_name(firstname, lastname, middlename = None):
# # def get_your_name(firstname, lastname, middlename = ''):
#     fullname = ''
#     if middlename:
#         fullname = f'{firstname} {middlename} {lastname}'
#     else:
#         fullname = f'{firstname} {lastname}'
#     return fullname
# fullname = get_your_name('Zhang', 'Bin')
# print(fullname)

# fullname = get_your_name('Zhang', 'Bin', 'Niu')
# print(fullname)

#测试是否会改变实参,类似传地址和传值的区别
# def think_not_change(age):
#     age = 18
# age = 15
# think_not_change(age)
# print(age)

# def think_change(ages):
#     ages.append(20)
# ages = [18, 19]
# think_change(ages)
# print(ages)

# def need_something(who, *somethings):
#     print(somethings)
#     des = f'{who} need'
#     for thing in somethings:
#         des += f' {thing}'
#     print(des)

# need_something('Zhang Bin', 'banana', 'tool', 'play')


# def build_profile(who, **infos):
#     print(infos)
#     infos['name'] = who
#     return infos

# profile = build_profile('Zhang Bin', location = 'Shang Hai', car = 'Rong Wei', favorite = 'Play Games')
# print(profile)


# 调换顺序也不行,函数定义得在前面
# profile = build_profile('Zhang Bin', location = 'Shang Hai', car = 'Rong Wei', favorite = 'Play Games')
# print(profile)

# def build_profile(who, **infos):
#     print(infos)
#     infos['name'] = who
#     return infos

