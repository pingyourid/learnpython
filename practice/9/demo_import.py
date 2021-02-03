# import car as c

# my_car = c.Car('subaru', 'outback', 2015)
# my_car.get_descriptive_name()

# 看起来就是代码替换，包括非类内的代码都执行了，要注意。建议在需要引入很多类时使用，优势是使用点语法不会造成类或函数混淆
# ------

from car import Car

my_car = Car('subaru', 'outback', 2015)
my_car.get_descriptive_name()

# 看起来就是代码替换，包括非类内的代码也执行了，奇葩！
# ------  推荐使用这种