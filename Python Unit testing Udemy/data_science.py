#print('Jumboooo')

import numpy as np

"""
sports = ['Cricket', 'Football', 'Tennis', 'Golf', 'Baseball']
sports_new = np.array(sports)
print(sports_new)


mat = np.array([[1,2,1],[4,5,9],[1,8,9]])
print(mat)
"""

vec = np.arange(10, 20, 3)
print(vec)

vec1 = np.linspace(10,20,3)
print(vec1)

vec4 = np.zeros([2,3])
print(f'np zeros:- \n{vec4}')

exp1 = np.exp(1) #means e ** {num}
print(exp1)

n = 1
num_log = np.log(n)#by default it takes log base e
print(f'Log of {n} to base e  is:- {num_log}')

b = np.array([1,4,7])
print(b)

log_ten = np.log10(100)# log base 10
print(log_ten)

log_three = np.log2(8)
print(log_three)


vec1 = np.arange(0, 12)
print(f'Vec 1:- {vec1}')
vec2 = vec1.reshape(4, 3)
print(f'Vec 2:- \n{vec2}')



try:
    vec = np.arange(0, 5)
    print(vec.reshape((2, 3)))
except ValueError:
    print(f':- cannot reshape array of size 5 into shape (2,3)')
#except as e:

#vec1 = vec1.[::-1]   reverses it
print(f'Vec 1 after vec1.[::-1] is:- {vec1}')


#use @ sign for multiplication according to linear algebra
a1 = np.arange(1,10).reshape(3,3)
a2 = np.arange(11,20).reshape(3,3)
print(f'a1:- {a1}')
print(f'a2:- {a2}')
n_transpose = np.transpose(a1)
print(f'Tranpose of a1 is:- {n_transpose}')

mult = a1 @ a2
print(f'Dot multiplicvation:- {mult}')

n2_transpose = a2.T
print(f'Tranpose of a2 is:- {n2_transpose}')