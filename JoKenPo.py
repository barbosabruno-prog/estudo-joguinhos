'''  Jokenpo: O USUÁRIO ESCOLHE PEDRA, PAPEL OU TESOURA PARA DISPUTAR CONTRA O CPU '''

def jokenpo():

    import emoji.core

    import random

    placar = [0, 0]
    opcoes = {1:emoji.emojize(':raised_fist:'), 2:emoji.emojize(':raised_hand:'), 3:emoji.emojize(':victory_hand:')}

    print('******************************************************')
    print('*OOOOOO***OOOO***O**O**OOOOOO**O****O**OOOOO****OOOO**')
    print('****O****O****O**O*O***O*******OO***O**O****O**O****O*')
    print('****O****O****O**OO****O*******O*O**O**O****O**O****O*')
    print('****O****O****O**OO****OOOO****O**O*O**OOOOO***O****O*')
    print('*O**O****O****O**O*O***O*******O***OO**O*******O****O*')
    print('**OO******OOOO***O**O**OOOOOO**O****O**O********OOOO**')
    print('******************************************************')

    comeco = input('Novo jogo? (S/N) ')



    while comeco.lower() == 's':

        playerChoice = int(input(emoji.emojize('JO KEN PO!!!\n 1 = :raised_fist: | 2 = :raised_hand: | 3 = :victory_hand: \n')))

        if playerChoice < 1 or playerChoice > 3:
            print('Não é uma opção válida!!!\n')
            continue

        cpuChoice = random.randint(1, 3)

        print('Sua escolha: {}'.format(opcoes[playerChoice]))
        print('Escolha do CPU: {}'.format(opcoes[cpuChoice]))

        if playerChoice == cpuChoice:
            print('\nDeu empate!')
        elif playerChoice == 1 and cpuChoice == 3:
            print('\nVocê ganhou!')
            placar[0] += 1
        elif playerChoice == 2 and cpuChoice == 1:
            print('\nVocê ganhou!')
            placar[0] += 1
        elif playerChoice == 3 and cpuChoice == 2:
            print('\nVocê ganhou!')
            placar[0] += 1
        else:
            print('\nCPU ganhou!')
            placar[1] += 1

        comeco = input('\nDeseja jogar outra vez? (S/N) ')
        if comeco.lower() == 's':
            print('\n********************************\n')
        else:
            print('\n********** PLACAR **************\n')
            print('Jogador {} X {} CPU'.format(placar[0], placar[1]))