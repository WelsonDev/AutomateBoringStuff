import  sys

print('Digite um numero')

try:
    numero = int(input())

except ValueError:
       print('Digite um numero inteiro')

def collatz(numero):

    if numero % 2 == 0:
        numero = ( numero // 2)

        return print(int(numero))

    elif numero % 2 == 1:
        numero = (3 * numero + 1)

        return print(int(numero))


collatz(numero)
