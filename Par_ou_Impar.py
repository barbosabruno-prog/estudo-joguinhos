'''  PAR OU IMPAR: O JOGADOR ESCOLHE UM NÚMERO DE 0 A 10 PARA DISPUTAR CONTRA O CPU '''

def parOuImpar():

    import random

    comeco = input('Novo jogo? (S/N) ')

    while comeco.lower() == 's':

        PouI = input('Par ou impar? ').lower()
        playerChoice = int(input('Digite um número entre 0 e 10: '))
        cpuChoice = random.randint(0, 10)

        soma = playerChoice + cpuChoice

        if soma % 2 == 0:
            resultado = 'par'
        else:
            resultado = 'impar'

        print('Você escolheu {}'.format(PouI.upper()))
        print('Sua jogada: {}'.format(playerChoice))
        print('Jogada do CPU: {}'.format(cpuChoice))

        if PouI == resultado:
            print('\nVocê ganhou!')
        else:
            print('\nCPU ganhou!')

        comeco = input('\nDeseja jogar outra vez? (S/N) ')
        if comeco.lower() == 's':
            print('\n********************************\n')