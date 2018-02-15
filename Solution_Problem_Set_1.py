
# coding: utf-8

# In[1]:


cm = float(input('Centimeters: '))
print('Meters: ', cm*0.01,'m')
print('Kilometers: ', cm*1e-5,'km')


# In[2]:


c = float(input('Celsius: '))
print('Fahrenheit: ',c*1.8+32,'F')


# In[3]:


x = int(input('x: '))
y = int(input('y: '))
print('x^y: ',x**y)


# In[4]:


inputNumber = int(input('Enter the number: '))
if inputNumber % 2 == 0:
    print(inputNumber, 'is EVEN.')
else:
    print(inputNumber, 'is ODD.')


# In[5]:


ch = input()
ch.isalpha()


# In[6]:


max(9, 10, 8)


# In[7]:


import math
a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))
d = (b*b)-(4*a*c)
if d>0:
    e = math.sqrt(d)
    r1 = float(-b+e)/(2*a)
    r2 = float(-b-e)/(2*a)
    print('The roots are: ', r1, r2)
else:
    print('Complex roots.')


# In[8]:


len('1010101010')


# In[9]:


x = 'deeds'
x == x[::-1]


# In[10]:


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Input a number to compute the factiorial : "))
print(factorial(n))


# In[11]:


for i in range(1, 255):
    ch = chr(i)
    print(i, "=", ch)


# In[13]:


sen = 'count total number of vowels and consonants in a string'
vowels = list("aeiouy")
consonants = list("bcdfghjklmnpqrstvexz")
v = 0
c = 0
for i in sen:
    if i in vowels:
        v+=1
    elif i in consonants:
        c+=1
print('Vowel:',v,'consonants: ',c)


# In[14]:


def most_frequent(text):
    frequencies = [(c, text.count(c)) for c in set(text)]
    return max(frequencies, key=lambda x: x[1])[0]

s = 'ABBCCCDDDD'
print(most_frequent(s))


# In[18]:


foo = "SSYYNNOOPPSSIISS"


def rm_dup(input_str):
    newstring = foo[0]
    for i in range(len(input_str)):
        if newstring[(len(newstring) - 1 )] != input_str[i]:
            newstring += input_str[i]
        else:
            pass
    return newstring

print (rm_dup(foo))


# In[22]:


myName = 'Jisan'
print(myName)


# In[20]:


break = 50


# In[23]:


phoneNumber = 12345
name = 'Benny'
print(phoneNumber)
print(name)


# In[24]:


leapYear = (2016, 2020, 2024, 2028)
print(leapYear)


# In[25]:


leapYear = (2016, 2020, 2024, 2028)
leapYearList = list(leapYear)
print(leapYearList)


# In[33]:


leapYear = (2016, 2020, 2024, 2028)
leapYearList = list(leapYear)
del leapYearList[0]
convertedLeapYearTuple = tuple(leapYearList)
print(convertedLeapYearTuple)


# In[35]:


2+3*4


# In[36]:


print(2+3*4)


# In[37]:


print(5 > 2 and 10 < 20)


# In[38]:


oddNumbers = [1, 3, 5, 7, 9]
print(oddNumbers)
oddNumbers[2] = 15
print(oddNumbers)
evenNumbers = [2, 4, 6]
concatenatedList = oddNumbers + evenNumbers
print(concatenatedList)


# In[39]:


ageOfEmployees = {'Ben': 25, 'Matthew': 32, 'Mark': 28, 'Mary': 21, 'Leon': 23}
print(ageOfEmployees)
ageOfEmployees['Matthew'] = 35
print(ageOfEmployees)
copyOfAgeOfEmployees = ageOfEmployees.copy()
ageOfEmployees.clear()
print('copyOfAgeOfEmployees = {}'.format(copyOfAgeOfEmployees))
print('ageOfEmployees = {}'.format(ageOfEmployees))


# In[40]:


if 2 < 10:
  print('2 is less than 10')


# In[41]:


number = 11
if number % 2 is 0:
    print('Even number')
else:
    print('Odd number')


# In[42]:


number = 150
if number % 10 is 0 and number % 50 is 0:
    if number % 30 is 0:
        print('This number is divisible by 10, 50 and 30')
    else:
        print('This number is divisible by 10 and 50 but not 30')

