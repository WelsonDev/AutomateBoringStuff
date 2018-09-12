# Jogo da adiviçao
import random

NumeroSecreto = random.randint(1, 20)
print('Estou pensando em um numero entre 1 e 20.')


for guessesTaken in range(1, 7):
    print('Digite um numero.')
    guess = int(input())

    if guess < NumeroSecreto:
        print('Seu valor e muito baixo')
    elif guess > NumeroSecreto:
        print('Seu valor e muito alto')
    else:
        break

if guess == NumeroSecreto:
    print('Otimo! voce adinviou em  ' + str(guessesTaken) + ' tentativas!')
else:
    print('Nao acertou! O numero que eu estava pensando era ' + str(NumeroSecreto))