

'''

i = '20'
if i > 20:
    print(1)
else:
    print(2)


a = 1
for i in range(1,6):
    print(f'The value of i is:- {i} and a is {a} therefore {a} * {i} is {a*i}')
    a = a * i
    if i == 4:
        print(f'a is:- {a}')
print(f'Final a is :- {a}')



n = [1,2,3,4]

print(n[-2])



alphabets = {'1':'A','2':'B','3': ['C','D','E']}

print(alphabets['3'][2])


list = ["Great", 51, True, 46, "Hi"]

p = list[2:-1]

print(p)



list_mul = ['2','2','2']
t = list_mul*2

print(t)

n =2

lambda_cube = lambda n: n*n*n

l = lambda_cube

print(l)



g = [7, 8.5, 9.5, 11, 10, 9, 11, 12.5, 13, 12, 13, 14]

sum = 0

i = 0
for i in g:
    sum = sum + i

av = sum / len(g)

print(av)

print("Intro to Python")


name = ['John', 'Nick', 'Summer', 'June', 'Jack', 'Mike']
print(name[2:4])


string = "How are you"
print(string[2:5])

print(float(78))

print(5/2 == 2)

'''
'''
name_age = {'Jack':20, 'Summer':25, 'June':30}
for i in name_age:
  print(i)

my_list = [34, "Great", 60.7, True, "Data"]
print(my_list[:])

a = 7/2
b = 3.5
c = a>b
print(c)



list_1 = [1, 2, 3, 4, 5]
mul = 1
for i in list_1:
  mul = mul*i
print("The multiplication is =", mul)
'''

i=1
while i<6:
  print("i is =", i)
  i+=1

sum = 0
i=1
while i<6:
  sum = sum + i
  i += 1
print("The sum is =", sum)