
# from getpass import getpass
# password = getpass('this password will not be seen in the console")

#1-problem (zip,)
# names = ['Samandar','Ravshan']
# heroes = ['Spiderman','Betman']

# for hero,name in zip(names,heroes):
#     print(hero,name)


# x=2 
# x = 1 if x else 2
# ##print(x)

#2-problem
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



#Generators
# my_sentence = 'this is a test'
# def range(sentence):
#     words = sentence.split()
#     for word in words:
#         yield word

# sentence = range(my_sentence)



# Generators taks-2

def square_numbers(arr):
    for num in arr:
        yield num*num

arr = [1,2,3,4,5,6]
nums = square_numbers(arr)

[print(num) for num in nums]





people = ['S1mple','Ax1le','Hobbit','Nafany']


roles = ['AWP','RIFLER','Support','IGL']

def gen(people,role):
    for player,role in zip(people,roles):
        yield player + " is a " + role

def list_of(people,role):
    i = 1
    for player,role in zip(people,roles):
        person = {
            'id': i,
            'name': player,
            'role': role,
        }
        i+=1
        yield person

geners = gen(people,roles)
[print(g) for g in geners]

l = list_of(people,roles)
[print(g) for g in l]