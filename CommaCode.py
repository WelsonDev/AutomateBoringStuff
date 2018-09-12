# exercicio pratico chapter 4 #comma code
def spam():
    mylist = []
    while True:
        print('Digite o ' + str(len(mylist) + 1) + 'º item da sua lista' + ' ou digite enter para sair.')
        name = input()
        if name == '':
            break

        mylist = mylist + [name]
    if len(mylist) > 1:
        return print('{} and {}'.format(', '.join(mylist[:-1]), mylist[-1]))
    try:
        return print(mylist)
    except IndexError:
        raise ValueError(' ')


spam()
