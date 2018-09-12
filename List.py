spam = ['cat', 'bat', 'rat', 'elephant']

print(spam[0:4])

spam = spam * 3

for i in range(len(spam)):
    print('index ' + str(i) + ' in spam is:' + spam[i])
