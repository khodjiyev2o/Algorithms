# from getpass import getpass
# password = getpass('this password will not be seen in the console")

# 1-problem (zip,)
# names = ['Samandar','Ravshan']
# heroes = ['Spiderman','Betman']

# for hero,name in zip(names,heroes):
#     print(hero,name)


# x=2
# x = 1 if x else 2
# ##print(x)

# 2-problem
# a,b,*c = (1,2,3,4,5,6,7)
# ##print(a,b,c)


##3

# class Person:
#     pass


#     def __str__(self):
#         return self.last
# person = Person()
# person.first = 'Samandar'
# setattr(person,'last','Khodjiyev')
# last = getattr(person,'last')
# print(last)
# print(dir(getpass))


# Generators
# my_sentence = 'this is a test'
# def range(sentence):
#     words = sentence.split()
#     for word in words:
#         yield word

# sentence = range(my_sentence)


# Generators taks-2

# def square_numbers(arr):
#     for num in arr:
#         yield num*num

# arr = [1,2,3,4,5,6]
# nums = square_numbers(arr)

# [print(num) for num in nums]


# people = ['S1mple','Ax1le','Hobbit','Nafany']


# roles = ['AWP','RIFLER','Support','IGL']

# def gen(people,role):
#     for player,role in zip(people,roles):
#         yield player + " is a " + role

# def list_of(people,role):
#     i = 1
#     for player,role in zip(people,roles):
#         person = {
#             'id': i,
#             'name': player,
#             'role': role,
#         }
#         i+=1
#         yield person

# geners = gen(people,roles)
# [print(g) for g in geners]

# l = list_of(people,roles)
# [print(g) for g in l]


# #Fizzbuzz problem

# for i in range(1,105):
#     if i % 5 == 0 and i % 3 == 0:
#         print(f"{i} is Fizzbuz")
#     elif i % 3 == 0:
#          print(f"{i} is Fizz")
#     elif i % 5 == 0:
#          print(f"{i} is Buzz")
#     else:
#          print(f"{i} is nothing")


# set is a python data type which has no duplicates in it .Even if you insert duplicated while releasing it is not going to return one item two times


# Fibonacci sequence

# def fibonacci(num):
#     a,b = 0,1
#     for i in range(1,num):
#          a,b = b,a+b
#          yield a


# for item in fibonacci(10):
#     print(item)


# OOP revision
# class Person:
#     def __init__(self,name):
#         self.name = name


#     def intro(self):
#         print(self.name)

# class SuperHero(Person):
#     def __init__(self,name,ability):
#         super().__init__(name)
#         self.ability = ability

#     def intro(self):
#         super().intro()
#         print(f"... and i am {self.ability}")


# person = Person('samandar')
# hero = SuperHero('samandar','clever')

# person.intro()
# hero.intro()


list = []

#for i in range(2, 98):
 #   if i % 2 == 0:
  #      list.append(i)


#start = 0
#end = 49

#for i in range(start,end,4):
 #   print(list[i:i+4])
        
#def convert(string):
 #  count = 0
  # result = ''
   #for n,i in enumerate(string):
    #  count +=1
     # print(n,i)
     # if n == len(string)-1 or i != string[n+1]:
      #   result += f"{i}{count}"
       #  count = 0
   #return result

#print(convert('abbccc'))
