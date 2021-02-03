dogs = ["yellow dog", "black dog", "white dog"]
message = f"I have a dog which is a {dogs[1].title()}"
print(message)

dogs[1] = "blue dog"
print(dogs)

dogs.append("black dog")
print(dogs)

#------del
del dogs[0]
print(dogs)

dogs.pop()
print(dogs)

poped = dogs.pop(0)
print(dogs)
print(poped)

#del足够

cats = ["yellow cat", "yellow cat", "black cat"]
print(cats)
cats.remove("yellow cat")
print(cats)

#remove只会查找到第一个匹配的内容，不是废物api是什么，不建议用

#----
cats.append("origin cat")
print(cats)
cats.sort()
print(cats)
cats.sort(reverse = True)
print(cats)

print(sorted(cats))
print(cats)

#sorted不会改变原数组顺序，sort会改变原数组顺序，sorted又是个废物api，容易误导

houses = ["big house", "small house", "middle house"]
houses.reverse()
print(houses)
length = len(houses)
print(length)