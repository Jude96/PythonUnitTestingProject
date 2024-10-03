'''

X= [10,"Range", "Great", -54, 11, 12]

print(X[2:4])
print(len(X[2:4]))

X= [10,"Range", "Great", -54, 11, 12]
print(X[2:-1])

X= [10,"Range", "Great", -54, 11, 12]
print(X[-2:-1])

X=(20,23,-50,5.6,98)
X.pop(2)
print(X)


X=(20,23,-50,5.6,98)
print(X[2:-1])


dictionary={1:"USA", 2:"India", 3:"China"}
dictionary.update({3:"Japan"})
print(dictionary)

dictionary={1:"USA", 2:"India", 3:"China"}
dictionary.pop(2)
print(dictionary)


a = b = TRUE
if (a == b):
  print("Hello")
else:
  print("Well done")



if 4 + 3 == 9:
 print("The addition of 4 and 3 is correct")
else:
 print("The addition of 4 and 3 is not correct")
print("Hello")


#print(range(5))

for i in range(1,5):
    print(i*2)


sum = 0
for number in range(1,5):
    sum = sum + number
print(sum)

x = [1, 2, 3, 4, 5]
while x:
  print(x.pop(0))
#print(x)


list_1 = [1, 2, 3, 4, 5]
list_comp = [ i for i in list_1 ]
print(list_comp)

print(range(5))

week_list = [ "Week" + str(i) for i in range(5)]
print(week_list)


def func(a):
  print(a)
A = [0,1,2,3]
func(A)


def say(message, times):
  print(message * times)


say("How are you", 2)



mul = lambda a,b: return a*b
mul(5,6)


a = 3
print(a + (33))



a = '5a'
int(a)



v = 10
w = 25
x = 70
y = 2
z = (v + w) * (x / y)
print(z)


a = 10
b = 5
print("A and B before swapping {},{}".format(a,b))
temp = a #create a third variable and assign the value of a to it

a = b

#write the missing code(code missing here)
b = temp #value of a is in third variable so assign the value to b
print("A and B after swapping {},{}".format(a,b))



repeated_list = [2] * 4
print(repeated_list)


a = 56
if a == 10:
 print("Hello")
else:
 print("Good Bye")


a = "I am a Data Scientist"
if "Data" in a:
 print("It is present")
else:
 print(False)



a = -99
if a > 0:
 print("Number is Positive")
else:
 print("Number is negative")




first = 25
second = 34
third = 45
if first >= second and first >= third:
 print(first)
elif second >= first and second >= third:
 print(second)
elif third >= first and third >= second:
 print(third)
else:
 print("All of the values are equal")


for i in range(-10, 0, 1):
 print(i)


n = 10
i = 1
while i <= n:
 print(i)
 i = i + 1



n = 8
for i in range(1, 11):
 print("{} ^ {} =".format(n, i), n**i)



for i in range(202, 321):
 if i % 7 == 0 and i % 5 ! 0:
     print(i)


a = "Data Science"
for i in range(0, 5):
 print(a)




def mths(a, b):
 print(a + b)
 print(a - b)
 print(a * b)
 print(a // b)


#mths(9, 5)

def num(x):
 y = x * x
 z = y + 5
 return z

print(num(5))


def area(base, height):
 return 0.5 * base * height
print(area(5, 10))



def convert(celsius):
 fah = 1.8 * celsius + 32
 print("Temperature in Fahrenheit =", fah)
convert(20)



def total_addition(*numbers):
 addition = 0
 for number in numbers:
  addition += number
 return addition


#print(total_addition(1, 2, 3))

def fun(*args):return args

print(fun(1, 2, 3))
print(fun(23, 24))



def fun(*int):
 result = 1
 for x in int:
  result *= x
 return result


print(fun(1, 2, 3, 4, 5))



def function(var1=2, var2=4):
 var2 = 6
 var1 = 5
 print(var1, var2)


print(function(10, 20))




def my_function(a, b, **kwargs, *args):
 return a + b


my_function(5, 6)


#name = input()
#age = int(input())


class Person:
 def __init__(self,name,age):
  # Write your code below
  self.name = name
  self.age = age

 def show_details(self):
  print(f'Name is:- {self.name}')
  print(f'Age is:- {self.age}')


# Create an object of the 'Person' class
person = Person('Mikee',22)
person.name = 'Mike'
#person.age = 21
person.show_details()



# You are given a class named 'Rectangle' with attributes 'length' and 'width'. Write a program to create an object of the 'Rectangle' class and set the attributes to the given values. Finally, calculate and print the area of the rectangle.

class Rectangle:
 def __init__(self, length, width):
  # Write your code below
  self.length = length
  self.width = width

 def get_area(self):
  area = self.length * self.width
  print(area)


# Create an object of the 'Rectangle' class
rectangle = Rectangle(2,1)
rectangle.length = 2
rectangle.width = 9

rectangle.get_area()




'''

r = 'Hello world'

t = 0

while t < len(r):
    print(r[t])
    t += 1

