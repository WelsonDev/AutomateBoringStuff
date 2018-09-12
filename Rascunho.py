
# myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
# print(myCat)

# print(myCat['size'])

# print('My cat has ' + myCat['color'] + ' fur.')

# spam = {12345: 'Luggage Combination', 42: 'The Answer'}

# print(spam)

# print(spam)

#birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
#while True:
#       print('Enter a name: (blank to quit)')
#       name = input()
#       if name == '':
#           break
#       if name in birthdays:
#               print(birthdays[name] + ' is the birthday of ' + name)
#       else:
#           print('I do not have birthday information for ' + name)
#           print('What is their birthday?')
#           bday = input()
#           birthdays[name] = bday
#           print('Birthday database updated.')


# spam = {'color': 'red', 'age': 42}
#
# for v in spam.values():
#     print(v)
# print('-------')
#
# for k in spam.keys():
#     print(k)
# print('-------')
#
# for i in spam.items():
#     print(i)
#     print('-------')


# spam = {'color': 'red', 'age': 42}
# list = spam.keys()
# print(list())


# spam = {'color': 'red', 'age': 42}
# for k, v in spam.items():
#    print('Key: ' + k + ' Value: ' + str(v))

'''
picnicItems = {'apples': 5, 'cups': 2}
'I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.'
'I am bringing 2 cups.'
'I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.'
'I am bringing 0 eggs.'

picnicItems = {'apples': 5, 'cups': 2}
'I am bringing ' + str(picnicItems['eggs']) + ' eggs.'
'''


# spam = {'name': 'Pooka', 'age': 5}
# if 'color' not in spam:
#     spam['color'] = 'black'
#

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)