"""
1.
print ("Hello,America!")
print ("Hello,World!")
print ("Hello,ddy123")

2.
a = 50
if a < 10:
   print("小于10")
else:
   print("大于等于10")

3.
a = 20
if a <= 10:
    print("小于等于10")
elif a <= 25:
    print("大于10且小于等于25")
else:
    print("大于25")

a = 100
b = 66
z = a % b
z1 = a // b
print (z)
print (z1)


age = 64
retirement = age - 65

if retirement < 10:
    print("You get to retire soon.")
else:
    print("You have a long time until you can retire!")
    


def squ(x):
    return x ** 2


print (squ(3))



def ch(c):
    print(c)

ch("Hello China")


3.
def test ( x , y , z , a = 2 , b = 4 ):
    return x + y + z + a + b

print(test(1,2,3,6,7))



4.
def first_2(x):
    return x // 2

y = first_2(10)


def first_4(y):
    return y * 4

print (first_4(y))





def sprint_float (c):
    try:
        return float(c)
    except (ZeroDivisionError,ValueError):
        print("Invalid input.")

print(sprint_float("56"))



# 1．创建一个你最喜欢歌手的列表。

singer = ["Jay","Angel","xietingfei"]
print(singer)


# 2．创建一个由元组构成的列表，每个元组包含居住过或旅游过的城市的经纬度。

lng = [("N22°32′43.86″","东经E114°03′10.40″"),("N23°22′43.86″","东经E154°03′60.70″")]
print(lng)


# 3．创建一个包含你的不同属性的字典：身高、最喜欢的颜色和最喜欢的作者等。
man = {"height":"173","color":"blue","author":"none"}
print(man)


# 4．编写一个程序，让用户询问你的身高、最喜欢的颜色或最喜欢的作者，并返回上一个挑战中创建的字典。
n = input ("Type a number:")
if n in man:
    print(man[n])
else:
    print("Not found.")



# 5．创建一个字典，将最喜欢的歌手映射至你最喜欢的歌曲。
song = {"height":"173",
       "color":"blue",
       "author":"none"}
print(song)


# 6．列表、元组和容器只是 Python 中内置容器的一部分。自行研究 Python 中的集合（也是一种容器）在什么情况下可以使用集合？

"""


"""
字符串

#  1．打印字符串"Camus"中的所有字符。
string = "Camus"
print(string[0])
print(string[1])
print(string[2])
print(string[3])
print(string[4])
print(string[-1])
print(string[-2])



# 2．编写程序，从用户处获取两个字符串，将其插入字符串"Yesterday I wrote a [用户输入 1]. I sent it to [用户输入 2]!"中，并打印新字符串。

guest1 = input ("用户输入1：")
guest2 = input ("用户输入2：")
string = "Yesterday I wrote a {}. I sent it to {}!".format(guest1,guest2)
print(string)



# 3．想办法将字符串"aldous Huxley was born in 1894."的第一个字符大写，从而使语法正确。



string = "aldous Huxley was born in 1894."
print(string.title())


# 4．对字符串"Where now? Who now? When now?"调用一个方法，返回如下述的列表["Where now?", "Who now?", "When now?"]。

string = "Where now? Who now? When now?".split("?")
print (string)




#5．对列表["The", "fox", "jumped", "over", "the", "fence", "."]
#进行处理，将其变成一个语法正确的字符串。每个单词间以空格符分隔，但是单词
#fence 和句号之间不能有空格符。（别忘了，我们之前已经学过将字符串列表连接为单
#个字符串的方法。）
one = ["The", "fox", "jumped", "over", "the", "fence", "."]
one = " ".join(one)
words = one[0:-2] + "."
print(words)



#  6．将字符串"A screaming comes across the sky."中所有的"s"字符替换为美元符号。

aa = "A screaming comes across the sky.".replace("s","$")
print (aa)




# 7．找到字符串"Hemingway"中字符"m"所在的第一个索引。

a = "Hemingway".index("m")
print (a)


# 8．在你最喜欢的书中找一段对话，将其变成一个字符串。


# 9．先后使用字符串拼接和字符串乘法，创建字符串"three three three"。
a = " three"
b = a + a + a
c = a*3
print (b,c)

# 10．对字符串"It was bright cold day in April, and the clocks were striking thirteen."进行切片，只保留逗号之前的字符。

a = "It was bright cold day in April, and the clocks were striking thirteen."[0:-2]
print(a)

"""


"""
循环

# 1．打印以下列表["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]中的每个元素。


a = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]
for show in a:
    print(show)
    


# 2．打印从 25 到 50 之间的所有数字。

for i in range(25,50):
    print(i)



# 3．打印第一个挑战练习中的每个元素及其索引。

a = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]
i = 0
for show in a:
    print(show,i)
    i+=1

shows = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]
for index, show in enumerate(shows):
    print(index)
    print(show)



# 4．编写一个包含死循环和数字列表的程序（可选择输入 q 退出）。每次循环时，请用户猜一个在列表中的数字，然后告知其猜测是否正确。

i=0
while True:
    num = input("Type a number:")
    if num == "q":
        break
    try:
        num = int(num)
    except ValueError:
        print("Error")
    if num == i:
        print("Right")
    else:
        i+=1
        
# 5．将列表[8, 19, 148, 4]中的所有数字，与列表[9, 1, 33, 83]中的所有数字相乘，并将结果添加到第 3 个列表中。

list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
list_sum = []
for i in list1:
    for j in list2:
        list_sum.append(i*j)
print(list_sum)




# 1．定义一个叫 Apple 的类，创建 4 个实例变量，表示苹果的 4 种属性。


class Apple:
    def __init__(self,w,c,k,a):
        self.weight = w
        self.color = c
        self.kind = k
        self.area = a
        print("111")


# 2．定义一个叫 Circle 的类，创建 area 方法计算其面积。然后创建一个 Circle对象，调用其 area 方法，打印结果。可使用 Python 内置的 math 模块中的 pi 函数。


import math

class Circle:
    def __init__(self,r):
        self.radius = r
        print("222")

    def area(self):
        print(self.radius ** 2 * math.pi)

c1 = Circle(4)
c1.area()




# 3．定义一个叫 Triangle 的类，创建 area 方法计算并返回面积。然后创建一个Triangle 对象，调用其 area 方法，打印结果。

class Triangle:
    def __init__(self,w,l):
        self.width = w
        self.length = l
        print("333")

    def area(self):
        print(self.width * self.length / 2)


t = Triangle(4,6)
t.area()


# 4．定义一个叫 Hexagon 的类，创建 cacculate_perimeter 方法，计算并返回其周长。然后创建一个 Hexagon 对象，调用其 calculate_perimeter 方法，并打印结果。


class Hexagon:
    def __init__(self,l):
        self.length = l
        print("444")

    def cacculate_perimeter(self):
        print(6 * self.length)


h = Hexagon(2)
h.cacculate_perimeter()

"""
"""

# 1．创建 Rectangle 和 Square 类，使它们均有一个叫 calculate_perimeter的方法，计算其所表示图形的周长。创建 Rectangle 和 Sqaure 对象，并调用二者的周长计算方法。

class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.length = l

    def calculate_perimeter(self):
        return self.width * self.length

class Square(Rectangle):
    pass

r = Rectangle(3,4)
s = Square(5,5)
print(r.calculate_perimeter())
print(s.calculate_perimeter())

        
# 2．在 Square 类中，定义一个叫 change_size 的方法，支持传入一个数字，增加或减少（数字为负时）Square 对象的边长。


class Square:
    def __init__(self, num):
        self.num = num
     

    def change_size(self):
        if self.num != 0:
            return 4 + self.num
        else:
            return 4

        
s = Square(0)
print(s.change_size())


# 3．创建一个叫 Shape 的类。在其中定义一个叫 what_am_i 的方法，被调用时打印"I am s shape"。调整上个挑战中的 Square 和 Rectangle 类，使其继承 Shape类，
# 然后创建 Sqaure 和 Rectangle 对象，并在二者上调用新方法。


class Shape:
    def __init__(self):
        pass

    def what_am_i(self):
        print("I am s shape")


class Square(Shape):
    pass
    
class Rectangle(Shape):
    pass


s_shape = Shape()
s_shape.what_am_i()

s_square = Square()
s_square.what_am_i()


s_rectangle = Rectangle()
s_rectangle.what_am_i()



# 4．创建一个叫 Horse 的类，以及一个叫 Rider 的类。使用组合，表示一批有骑手的马。

class Horse:
    def __init__(self,name,color,ower):
        self.name = name
        self.color = color
        self.ower = ower

        
class Rider:
    def __init__(self,name):
        self.name = name

    
rid = Rider("ddy")


hor = Horse("ww","yellow",rid)
print(hor.name)
print(hor.color)
print(hor.ower.name)




# 1．向 Square 类中添加一个 square_list 类变量，要求每次新创建一个 Square对象时，新对象会被自动添加到列表中。


class Square:
    square_list = []

    def __init__(self,name):
        self.name = name
        self.square_list.append((self.name))


a = Square("a1")
b = Square("b1")
c = Square("c1")
print(Square.square_list)


# 2．修改 Square 类，要求在打印 Square 对象时，打印的信息为图形 4 个边的长度。例如，假设创建一个 Square(29)，则应打印 29 by 29 by 29 by 29。

class Square:


    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return """{} by {} by {} by {}""".format(self.name,self.name,self.name,self.name)
  

a = Square("b")
print(a)


# 3．编写一个函数，接受两个对象作为参数，如果为相同的对象则返回 True，反之返回 False。

def comparetwo(x,y):
    return x is y



print(comparetwo("6","6"))


"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello,World!"

app.run(port='8000')








