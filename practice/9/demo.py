from random import randint, choice
# result = randint(1, 6)
# print(result)

# books = ['tomas', 'sea', 'sun', 'fish', 'milk']
# random_book = choice(books)
# print(random_book)

class Die:
    """docstring for Die"""
    def __init__(self, sides=6):
        self.sides = sides

    """投骰子"""
    def roll_die(self):
        print(randint(1, self.sides))

def roll(die, count):
    for num in range(1, count + 1):
        die.roll_die()

die6 = Die()
roll(die6, 10)
print('-------------')

die10 = Die(10)
roll(die10, 10)
print('-------------')

die20 = Die(20)
roll(die20, 10)
print('-------------')