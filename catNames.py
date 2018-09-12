catNames = []
while True:
    print('Digite uma palavra ' + str(len(catNames) + 1) +
          ' (ou entre pra sair.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]  # list concatenation
print('The cat names are:')
for name in catNames:
    print('  ' + name)
